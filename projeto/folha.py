"""
Motor de desenho de folhas A3 para o projeto 11-4400-PEL-0301 rev.2.

Regras de construcao (impedem o desenho "embolado"):
  * cada texto declara a ZONA (faixa x) em que pode viver;
  * a largura vem da metrica REAL da fonte, nunca de estimativa;
  * o validador acusa texto x texto, texto x geometria e estouro de zona;
  * a folha so e' salva quando o validador retorna zero ocorrencias.
"""
import math
import string
import ezdxf
from ezdxf.enums import TextEntityAlignment as TA
from ezdxf.fonts import fonts

SHEET_W, SHEET_H = 420.0, 297.0
MARGIN = 10.0
PAD = 0.9
FONT = "DejaVuSans.ttf"
REV = "02"
DATA_REV = "27/08/2026"

PAGINAS = [
    ("01", "Capa"),
    ("02", "Indice"),
    ("03", "Legenda e Convencoes"),
    ("04", "Esquema de Forca - Entrada 690 V e Acionamentos"),
    ("05", "Esquema de Forca - Servicos Auxiliares 220 V / 24 Vcc"),
    ("06", "Esquema de Comando - Sinalizacao e Intertravamento"),
    ("07", "Ligacao de Controlador I - Pressao e Acionamentos 01 e 02"),
    ("08", "Ligacao de Controlador II - Acionamentos 03 e 04 e DCS"),
    ("09", "Layout Mecanico - Forma 4b"),
    ("10", "Lista de Bornes"),
    ("11", "Lista de Materiais"),
]


class Folha:
    def __init__(self, pagina, descricao):
        self.pagina, self.descricao = pagina, descricao
        self.doc = ezdxf.new("R2010", setup=True)
        self.doc.header["$INSUNITS"] = 4
        self.doc.header["$LTSCALE"] = 4.0
        self.doc.header["$LWDISPLAY"] = 1
        self.doc.styles.add("TXT", font=FONT)
        for nm, col in (("MOLDURA", 8), ("ESQUEMA", 7), ("TAGS", 1), ("TEXTO", 7),
                        ("NOTAS", 7), ("FANTASMA", 8), ("CARIMBO", 7), ("COMP", 5)):
            self.doc.layers.add(nm, color=col)
        self.msp = self.doc.modelspace()
        self.segments, self.tboxes = [], []
        self._fc = {}
        self._moldura()
        self._carimbo()

    # ------------------------------------------------------------- medicao
    def w(self, s, h):
        f = self._fc.get(h) or self._fc.setdefault(h, fonts.make_font(FONT, h))
        return f.text_width(s)

    # ---------------------------------------------------------- primitivas
    def line(self, p1, p2, layer="ESQUEMA", dashed=False, lw=25, check=True):
        e = self.msp.add_line(p1, p2, dxfattribs={"layer": layer, "lineweight": lw})
        if dashed:
            e.dxf.linetype = "DASHED"
        if check:
            self.segments.append((p1, p2, layer))

    def rect(self, x, y, w, h, layer="ESQUEMA", dashed=False, lw=25, check=True):
        p = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        e = self.msp.add_lwpolyline(p, close=True,
                                    dxfattribs={"layer": layer, "lineweight": lw})
        if dashed:
            e.dxf.linetype = "DASHED"
        if check:
            for i in range(4):
                self.segments.append((p[i], p[(i + 1) % 4], layer))

    def circle(self, x, y, r, layer="ESQUEMA", lw=25, check=True):
        self.msp.add_circle((x, y), r, dxfattribs={"layer": layer, "lineweight": lw})
        if check:
            pts = [(x + r * math.cos(a * math.pi / 8), y + r * math.sin(a * math.pi / 8))
                   for a in range(16)]
            for i in range(16):
                self.segments.append((pts[i], pts[(i + 1) % 16], layer))

    def text(self, s, x, y, h=2.2, layer="TEXTO", align="left", zona=None, check=True):
        wd = self.w(s, h)
        if align == "left":
            x0, ta = x, TA.MIDDLE_LEFT
        elif align == "right":
            x0, ta = x - wd, TA.MIDDLE_RIGHT
        else:
            x0, ta = x - wd / 2, TA.MIDDLE_CENTER
        self.msp.add_text(s, dxfattribs={"layer": layer, "height": h,
                                         "style": "TXT"}).set_placement((x, y), align=ta)
        if check:
            self.tboxes.append({"box": (x0 - PAD, y - h / 2 - PAD,
                                        x0 + wd + PAD, y + h / 2 + PAD),
                                "raw": (x0, x0 + wd), "s": s, "z": zona})
        return x0 + wd

    # -------------------------------------------------------------- helpers
    def bloco(self, x0, y0, x1, y1, titulo, linhas, h=2.25, lh=4.6, layer="NOTAS"):
        """Caixa com titulo e linhas de texto alinhadas a esquerda."""
        z = (x0 + 2.0, x1 - 2.0)
        self.rect(x0, y0, x1 - x0, y1 - y0, "MOLDURA", lw=18)
        self.line((x0, y1 - 8.5), (x1, y1 - 8.5), "MOLDURA", lw=18)
        self.text(titulo, (x0 + x1) / 2, y1 - 4.2, 2.6, "TEXTO", "center", z)
        for k, ln in enumerate(linhas):
            if ln:
                self.text(ln, x0 + 3.0, y1 - 13.5 - k * lh, h, layer, "left", z)

    def chamada(self, x_ini, y, x_fim, linhas, zona, x_txt=None, h=2.2, lh=4.4):
        """Linha de chamada horizontal + bloco de texto na coluna de anotacao."""
        self.line((x_ini, y), (x_fim, y), lw=13)
        xt = x_txt if x_txt is not None else x_fim + 2.0
        y0 = y + (len(linhas) - 1) * lh / 2.0
        for k, ln in enumerate(linhas):
            self.text(ln, xt, y0 - k * lh, h, "TEXTO", "left", zona)

    def tabela(self, x0, y_top, headers, rows, widths=None, h=2.1, row_h=5.6,
               hdr_h=6.6, aligns=None, layers=None):
        """Tabela com largura de coluna calculada a partir do conteudo real."""
        n = len(headers)
        if widths is None:
            widths = []
            for i in range(n):
                mx = self.w(headers[i], h)
                for r in rows:
                    mx = max(mx, self.w(str(r[i]), h))
                widths.append(mx + 5.0)
        xs = [x0]
        for wd in widths:
            xs.append(xs[-1] + wd)
        y_bot = y_top - hdr_h - row_h * len(rows)
        self.rect(x0, y_bot, xs[-1] - x0, y_top - y_bot, "MOLDURA", lw=18)
        self.line((x0, y_top - hdr_h), (xs[-1], y_top - hdr_h), "MOLDURA", lw=18)
        for x in xs[1:-1]:
            self.line((x, y_bot), (x, y_top), "MOLDURA", lw=18)
        for k in range(1, len(rows)):
            y = y_top - hdr_h - k * row_h
            self.line((x0, y), (xs[-1], y), "MOLDURA", lw=13)
        for i, ht in enumerate(headers):
            self.text(ht, (xs[i] + xs[i + 1]) / 2, y_top - hdr_h / 2, h, "TEXTO",
                      "center", (xs[i] + 1, xs[i + 1] - 1))
        al = aligns or ["center"] * n
        lay = layers or ["TEXTO"] * n
        for k, r in enumerate(rows):
            y = y_top - hdr_h - row_h * (k + 0.5)
            for i, v in enumerate(r):
                z = (xs[i] + 1, xs[i + 1] - 1)
                if al[i] == "left":
                    self.text(str(v), xs[i] + 2.0, y, h, lay[i], "left", z)
                else:
                    self.text(str(v), (xs[i] + xs[i + 1]) / 2, y, h, lay[i], "center", z)
        return y_bot, xs[-1]

    # -------------------------------------------------------------- simbolos
    def s_disjuntor(self, x, y, polos=3, pitch=6.0, meia=4.0):
        """Disjuntor: quadrado com X por polo + ligacao mecanica tracejada."""
        offs = [(i - (polos - 1) / 2) * pitch for i in range(polos)]
        for dx in offs:
            px = x + dx
            self.line((px, y + meia + 5), (px, y + meia))
            self.rect(px - 2.6, y - 2.6, 5.2, 5.2)
            self.line((px - 2.6, y - 2.6), (px + 2.6, y + 2.6), lw=13, check=False)
            self.line((px - 2.6, y + 2.6), (px + 2.6, y - 2.6), lw=13, check=False)
            self.line((px, y - meia), (px, y - meia - 5))
        if polos > 1:
            self.line((x + offs[0], y + 3.4), (x + offs[-1], y + 3.4),
                      dashed=True, lw=13, check=False)

    def s_secc_fusivel(self, x, y, polos=3, pitch=6.0):
        """Seccionadora-fusivel: lamina + fusivel por polo, com link mecanico."""
        offs = [(i - (polos - 1) / 2) * pitch for i in range(polos)]
        for dx in offs:
            px = x + dx
            self.line((px, y + 12), (px, y + 8))
            self.line((px, y + 8), (px + 3.4, y + 4.6))          # lamina
            self.line((px - 1.8, y + 3.2), (px + 1.8, y + 3.2))  # contato fixo
            self.line((px, y + 3.2), (px, y + 2.4))
            self.rect(px - 1.9, y - 4.0, 3.8, 6.4)               # fusivel
            self.line((px, y - 4.0), (px, y - 8))
        if polos > 1:
            self.line((x + offs[0] + 3.4, y + 4.6), (x + offs[-1] + 3.4, y + 4.6),
                      dashed=True, lw=13, check=False)

    def s_inversor(self, x, yb, yt, w=30.0):
        self.rect(x - w / 2, yb, w, yt - yb)
        self.line((x - w / 2, yb), (x + w / 2, yt), lw=18, check=False)
        self.text("~", x - w / 4, yt - (yt - yb) * 0.22, 3.4, "ESQUEMA", "center", check=False)
        self.text("~", x + w / 4, yb + (yt - yb) * 0.22, 3.4, "ESQUEMA", "center", check=False)

    def s_motor(self, x, y, r=8.0):
        self.circle(x, y, r)
        self.text("M", x, y + r * 0.24, r * 0.55, "ESQUEMA", "center", check=False)
        self.text("3~", x, y - r * 0.42, r * 0.32, "ESQUEMA", "center", check=False)

    def s_borne(self, x, y, r=1.5):
        self.circle(x, y, r, check=False)

    def s_bobina(self, x, y, w=9.0, h=6.0):
        self.rect(x - w / 2, y - h / 2, w, h)
        self.line((x, y + h / 2 + 4), (x, y + h / 2))
        self.line((x, y - h / 2), (x, y - h / 2 - 4))

    def s_contato_na(self, x, y):
        self.line((x, y + 5), (x, y + 2.2))
        self.line((x, y + 2.2), (x + 3.6, y - 1.6))
        self.line((x, y - 2.2), (x, y - 5))
        self.line((x - 1.8, y - 2.2), (x + 1.8, y - 2.2))

    def s_contato_nf(self, x, y):
        self.line((x, y + 5), (x, y + 2.2))
        self.line((x, y + 2.2), (x + 3.6, y - 1.6))
        self.line((x, y - 2.2), (x, y - 5))
        self.line((x - 1.8, y - 2.2), (x + 1.8, y - 2.2))
        self.line((x + 3.2, y - 2.8), (x + 3.2, y - 0.4))

    def s_sinaleiro(self, x, y, r=3.2):
        self.circle(x, y, r)
        d = r * 0.72
        self.line((x - d, y - d), (x + d, y + d), lw=13, check=False)
        self.line((x - d, y + d), (x + d, y - d), lw=13, check=False)
        self.line((x, y + r), (x, y + r + 4))
        self.line((x, y - r), (x, y - r - 4))

    def s_botao(self, x, y, nf=False):
        self.line((x, y + 5), (x, y + 2.2))
        self.line((x, y + 2.2), (x + 3.6, y - 1.6))
        self.line((x, y - 2.2), (x, y - 5))
        self.line((x - 1.8, y - 2.2), (x + 1.8, y - 2.2))
        self.line((x + 1.8, y + 2.6), (x + 1.8, y + 4.4), lw=13)
        self.line((x + 0.4, y + 4.4), (x + 3.2, y + 4.4), lw=13)
        if nf:
            self.line((x + 3.2, y - 2.8), (x + 3.2, y - 0.4))

    def s_fonte(self, x, yb, yt, w=26.0):
        self.rect(x - w / 2, yb, w, yt - yb)
        self.line((x - w / 2, yb), (x + w / 2, yt), lw=18, check=False)
        self.text("~", x - w / 4, yt - (yt - yb) * 0.25, 3.2, "ESQUEMA", "center", check=False)
        self.line((x + w / 8, yb + (yt - yb) * 0.30), (x + w / 8 + 5, yb + (yt - yb) * 0.30),
                  lw=18, check=False)
        self.line((x + w / 8, yb + (yt - yb) * 0.22), (x + w / 8 + 5, yb + (yt - yb) * 0.22),
                  lw=13, check=False)

    # -------------------------------------------------------- moldura/carimbo
    def _moldura(self):
        self.rect(0, 0, SHEET_W, SHEET_H, "MOLDURA", lw=35, check=False)
        self.rect(MARGIN, MARGIN, SHEET_W - 2 * MARGIN, SHEET_H - 2 * MARGIN,
                  "MOLDURA", lw=35, check=False)
        NC, NR = 9, 6
        cw, rh = (SHEET_W - 2 * MARGIN) / NC, (SHEET_H - 2 * MARGIN) / NR
        for i in range(NC):
            x = MARGIN + cw * (i + 0.5)
            self.text(str(i + 1), x, SHEET_H - MARGIN / 2, 3.0, "MOLDURA", "center", check=False)
            self.text(str(i + 1), x, MARGIN / 2, 3.0, "MOLDURA", "center", check=False)
            if i:
                xx = MARGIN + cw * i
                self.line((xx, SHEET_H - MARGIN), (xx, SHEET_H), "MOLDURA", lw=18, check=False)
                self.line((xx, 0), (xx, MARGIN), "MOLDURA", lw=18, check=False)
        for i in range(NR):
            y = MARGIN + rh * (i + 0.5)
            ch = string.ascii_uppercase[NR - 1 - i]
            self.text(ch, MARGIN / 2, y, 3.0, "MOLDURA", "center", check=False)
            self.text(ch, SHEET_W - MARGIN / 2, y, 3.0, "MOLDURA", "center", check=False)
            if i:
                yy = MARGIN + rh * i
                self.line((0, yy), (MARGIN, yy), "MOLDURA", lw=18, check=False)
                self.line((SHEET_W - MARGIN, yy), (SHEET_W, yy), "MOLDURA", lw=18, check=False)

    def _carimbo(self):
        CX, CY, CW, CH = SHEET_W - MARGIN - 185.0, MARGIN, 185.0, 42.0
        self.CX, self.CY, self.CW, self.CH = CX, CY, CW, CH
        self.rect(CX, CY, CW, CH, "CARIMBO", lw=35)
        for dy in (10.5, 21.0, 31.5):
            self.line((CX, CY + dy), (CX + CW, CY + dy), "CARIMBO", lw=18)
        self.line((CX + 130.0, CY + 10.5), (CX + 130.0, CY + 31.5), "CARIMBO", lw=18)
        z = (CX + 2, CX + CW - 2)
        self.text("STORGE ENGENHARIA  |  VALMET  |  ARAUCO - PROJETO SUCURIU - INOCENCIA/MS",
                  CX + CW / 2, CY + 36.7, 2.5, "CARIMBO", "center", z)
        self.text("ESQUEMA ELETRICO - PRESSURIZACAO DAS ESCADAS DA CALDEIRA",
                  CX + 65.0, CY + 26.2, 2.4, "CARIMBO", "center", (CX + 2, CX + 128))
        self.text("11-4400-PEL-0301", CX + 157.5, CY + 28.7, 2.6, "CARIMBO", "center",
                  (CX + 132, CX + CW - 2))
        self.text("REV. " + REV + "  (MINUTA)", CX + 157.5, CY + 23.6, 2.2, "CARIMBO",
                  "center", (CX + 132, CX + CW - 2))
        self.text(self.descricao, CX + 65.0, CY + 15.7, 2.4, "CARIMBO", "center",
                  (CX + 2, CX + 128))
        self.text("FOLHA " + self.pagina + " DE 11", CX + 157.5, CY + 15.7, 2.4, "CARIMBO",
                  "center", (CX + 132, CX + CW - 2))
        self.text(REV + "  " + DATA_REV + "  STORGE  -  REVISADO CONFORME RELATORIO DE CONFORMIDADE",
                  CX + CW / 2, CY + 5.2, 2.3, "CARIMBO", "center", z)

    # ------------------------------------------------------------ validacao
    @staticmethod
    def _hit(p1, p2, r):
        x0, y0, x1, y1 = r
        (ax, ay), (bx, by) = p1[:2], p2[:2]
        if x0 <= ax <= x1 and y0 <= ay <= y1:
            return True
        if x0 <= bx <= x1 and y0 <= by <= y1:
            return True
        dx, dy = bx - ax, by - ay
        t0, t1 = 0.0, 1.0
        for p, q in ((-dx, ax - x0), (dx, x1 - ax), (-dy, ay - y0), (dy, y1 - ay)):
            if p == 0:
                if q < 0:
                    return False
            else:
                t = q / p
                if p < 0:
                    if t > t1:
                        return False
                    t0 = max(t0, t)
                else:
                    if t < t0:
                        return False
                    t1 = min(t1, t)
        return t0 <= t1

    def validate(self):
        out = []
        n = len(self.tboxes)
        for i in range(n):
            a = self.tboxes[i]["box"]
            for j in range(i + 1, n):
                b = self.tboxes[j]["box"]
                if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                    out.append("TEXTO x TEXTO: '%s' <-> '%s'"
                               % (self.tboxes[i]["s"][:30], self.tboxes[j]["s"][:30]))
        for t in self.tboxes:
            for p1, p2, lay in self.segments:
                if self._hit(p1, p2, t["box"]):
                    out.append("TEXTO x LINHA[%s]: '%s'" % (lay, t["s"][:38]))
                    break
            z = t["z"]
            if z and (t["raw"][0] < z[0] - 0.01 or t["raw"][1] > z[1] + 0.01):
                out.append("ZONA %s: '%s' (%.1f..%.1f)"
                           % (str(z), t["s"][:34], t["raw"][0], t["raw"][1]))
        return out

    def save(self, path):
        self.doc.set_modelspace_vport(height=SHEET_H * 1.06,
                                      center=(SHEET_W / 2, SHEET_H / 2))
        self.doc.saveas(path)
