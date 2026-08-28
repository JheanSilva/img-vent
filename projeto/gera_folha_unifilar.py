"""
Folha-piloto do unifilar 11-4400-PEL-0301 (conceito rev.2).

Metodo anti-sobreposicao:
  1. cada texto declara a ZONA em que pode viver (faixa x permitida);
  2. a largura vem da metrica REAL da fonte (ezdxf.fonts), nao de estimativa;
  3. um validador acusa texto x texto, texto x geometria e estouro de zona.
O desenho so e' exportado depois que o validador retorna zero ocorrencias.
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

# --------------------------------------------------------------- zonas (x0,x1)
Z_ANNOT = (96.0, 204.0)     # coluna de anotacoes do esquema
Z_GHOST = (209.0, 257.0)    # caixa dos alimentadores 02..04
Z_NOTES = (266.0, 406.0)    # bloco de notas
Z_FREE = None

X_TAG_R = 43.0              # tags alinhadas a direita nesta borda
X_IN = 45.0                 # prumada da entrada
X_FD = 60.0                 # prumada do alimentador 01
X_LEADER = 94.0             # fim da linha de chamada
X_ANNOT = 96.0              # inicio do texto de anotacao
Y_BUS = 232.0


class Sheet:
    def __init__(self, doc):
        self.doc, self.msp = doc, doc.modelspace()
        self.segments, self.tboxes = [], []
        self._fc = {}

    def width(self, s, h):
        f = self._fc.get(h) or self._fc.setdefault(h, fonts.make_font(FONT, h))
        return f.text_width(s)

    # ------------------------------------------------------------ primitivas
    def line(self, p1, p2, layer="ESQUEMA", dashed=False, lw=25, check=True):
        e = self.msp.add_line(p1, p2, dxfattribs={"layer": layer, "lineweight": lw})
        if dashed:
            e.dxf.linetype = "DASHED"
        if check:
            self.segments.append((p1, p2, layer))
        return e

    def rect(self, x, y, w, h, layer="ESQUEMA", dashed=False, lw=25, check=True):
        p = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        e = self.msp.add_lwpolyline(p, close=True,
                                    dxfattribs={"layer": layer, "lineweight": lw})
        if dashed:
            e.dxf.linetype = "DASHED"
        if check:
            for i in range(4):
                self.segments.append((p[i], p[(i + 1) % 4], layer))
        return e

    def circle(self, x, y, r, layer="ESQUEMA", lw=25, check=True):
        self.msp.add_circle((x, y), r, dxfattribs={"layer": layer, "lineweight": lw})
        if check:
            pts = [(x + r * math.cos(a * math.pi / 8), y + r * math.sin(a * math.pi / 8))
                   for a in range(16)]
            for i in range(16):
                self.segments.append((pts[i], pts[(i + 1) % 16], layer))

    def text(self, s, x, y, h=2.2, layer="TEXTO", align="left", zone=Z_FREE, check=True):
        w = self.width(s, h)
        if align == "left":
            x0, ta = x, TA.MIDDLE_LEFT
        elif align == "right":
            x0, ta = x - w, TA.MIDDLE_RIGHT
        else:
            x0, ta = x - w / 2, TA.MIDDLE_CENTER
        self.msp.add_text(s, dxfattribs={"layer": layer, "height": h,
                                         "style": "TXT"}).set_placement((x, y), align=ta)
        if check:
            self.tboxes.append({"box": (x0 - PAD, y - h / 2 - PAD, x0 + w + PAD, y + h / 2 + PAD),
                                "raw": (x0, x0 + w), "s": s, "zone": zone})

    # ------------------------------------------------------------- validacao
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
                    out.append(f"TEXTO x TEXTO: '{self.tboxes[i]['s'][:32]}' <-> "
                               f"'{self.tboxes[j]['s'][:32]}'")
        for t in self.tboxes:
            for p1, p2, lay in self.segments:
                if self._hit(p1, p2, t["box"]):
                    out.append(f"TEXTO x LINHA[{lay}]: '{t['s'][:40]}'")
                    break
            z = t["zone"]
            if z and (t["raw"][0] < z[0] - 0.01 or t["raw"][1] > z[1] + 0.01):
                out.append(f"ESTOURO DE ZONA {z}: '{t['s'][:40]}' "
                           f"({t['raw'][0]:.1f}..{t['raw'][1]:.1f})")
        return out


# ------------------------------------------------------------------ documento
doc = ezdxf.new("R2010", setup=True)
doc.header["$INSUNITS"] = 4
doc.header["$LTSCALE"] = 4.0
doc.header["$LWDISPLAY"] = 1
doc.styles.add("TXT", font=FONT)
for nm, col in (("MOLDURA", 8), ("ESQUEMA", 7), ("TAGS", 1), ("TEXTO", 7),
                ("NOTAS", 7), ("FANTASMA", 8), ("CARIMBO", 7)):
    doc.layers.add(nm, color=col)
s = Sheet(doc)

# -------------------------------------------------------------------- moldura
s.rect(0, 0, SHEET_W, SHEET_H, "MOLDURA", lw=35, check=False)
s.rect(MARGIN, MARGIN, SHEET_W - 2 * MARGIN, SHEET_H - 2 * MARGIN, "MOLDURA", lw=35, check=False)
NC, NR = 9, 6
cw, rh = (SHEET_W - 2 * MARGIN) / NC, (SHEET_H - 2 * MARGIN) / NR
for i in range(NC):
    x = MARGIN + cw * (i + 0.5)
    s.text(str(i + 1), x, SHEET_H - MARGIN / 2, 3.0, "MOLDURA", "center", check=False)
    s.text(str(i + 1), x, MARGIN / 2, 3.0, "MOLDURA", "center", check=False)
    if i:
        xx = MARGIN + cw * i
        s.line((xx, SHEET_H - MARGIN), (xx, SHEET_H), "MOLDURA", lw=18, check=False)
        s.line((xx, 0), (xx, MARGIN), "MOLDURA", lw=18, check=False)
for i in range(NR):
    y = MARGIN + rh * (i + 0.5)
    ch = string.ascii_uppercase[NR - 1 - i]
    s.text(ch, MARGIN / 2, y, 3.0, "MOLDURA", "center", check=False)
    s.text(ch, SHEET_W - MARGIN / 2, y, 3.0, "MOLDURA", "center", check=False)
    if i:
        yy = MARGIN + rh * i
        s.line((0, yy), (MARGIN, yy), "MOLDURA", lw=18, check=False)
        s.line((SHEET_W - MARGIN, yy), (SHEET_W, yy), "MOLDURA", lw=18, check=False)

# --------------------------------------------------------------------- titulo
s.text("DIAGRAMA UNIFILAR - ENTRADA 690 V E ALIMENTADOR 01 (PILOTO)",
       200.0, 281.5, 3.4, "TEXTO", "center")

# ------------------------------------------------------ entrada + disjuntor Q1
s.text("VEM DO CCM 11-4400-QSA-0003", 52.0, 276.0, 2.6, "TAGS", "left")
s.text("690 VCA - 3F+PE - CABO 35 mm2 CLASSE 0,6/1 kV", 52.0, 271.0, 2.4, "TEXTO", "left")
s.line((X_IN, 272.0), (X_IN, 256.0))
s.line((X_IN - 3, 263.0), (X_IN + 3, 267.0))
s.text("3", X_IN + 4.5, 265.0, 2.2, "TEXTO", "left")
s.rect(X_IN - 4, 248.0, 8, 8)
s.line((X_IN - 4, 248.0), (X_IN + 4, 256.0), check=False)
s.line((X_IN - 4, 256.0), (X_IN + 4, 248.0), check=False)
s.line((X_IN, 248.0), (X_IN, Y_BUS))
s.text("Q1", 39.0, 252.0, 3.4, "TAGS", "right")
s.line((X_IN + 5, 252.0), (X_LEADER, 252.0), lw=13)
for k, ln in enumerate(["DISJUNTOR EM CAIXA MOLDADA 63 A - Ue >= 690 V",
                        "Icu CONFORME ESTUDO DE Icc (PEND. Q1 DO RELATORIO)",
                        "MANOPLA ROTATIVA NA PORTA COM BLOQUEIO (LOTO)"]):
    s.text(ln, X_ANNOT, 256.4 - k * 4.4, 2.2, "TEXTO", "left", Z_ANNOT)

# ----------------------------------------------------------------- barramento
s.line((35.0, Y_BUS), (260.0, Y_BUS), lw=60)
s.line((35.0, Y_BUS - 1.8), (260.0, Y_BUS - 1.8), lw=60)
s.text("BARRAMENTO 690 V - Cu - FORMA 4b (SEGREGADO)",
       X_ANNOT, Y_BUS + 4.2, 2.2, "TEXTO", "left", Z_ANNOT)

# -------------------------------------------------------------- alimentador 01
s.line((X_FD, Y_BUS - 1.8), (X_FD, 222.0))
s.line((X_FD, 222.0), (X_FD + 5.5, 215.5))          # lamina
s.line((X_FD - 2.5, 213.0), (X_FD + 2.5, 213.0))    # contato fixo
s.line((X_FD, 213.0), (X_FD, 212.0))
s.rect(X_FD - 2.4, 200.0, 4.8, 12.0)                # fusivel
s.line((X_FD, 200.0), (X_FD, 178.0))
s.text("F1", X_TAG_R, 210.0, 3.4, "TAGS", "right")
s.line((X_FD + 6.5, 210.0), (X_LEADER, 210.0), lw=13)
for k, ln in enumerate(["SECCIONADORA-FUSIVEL 100 A - MANOPLA NA PORTA (BLOQUEAVEL)",
                        "FUSIVEL NH000 aR - Un >= 690 V (TABELA WEG CFW11)"]):
    s.text(ln, X_ANNOT, 212.2 - k * 4.4, 2.2, "TEXTO", "left", Z_ANNOT)

s.rect(X_FD - 15, 145.0, 30.0, 33.0)
s.line((X_FD - 15, 145.0), (X_FD + 15, 178.0), lw=18, check=False)
s.text("~", X_FD - 8.5, 170.0, 3.6, "ESQUEMA", "center", check=False)
s.text("~", X_FD + 8.5, 153.0, 3.6, "ESQUEMA", "center", check=False)
s.text("U1", X_TAG_R, 161.5, 3.4, "TAGS", "right")
s.line((X_FD + 15.5, 161.5), (X_LEADER, 161.5), lw=13)
for k, ln in enumerate(["INVERSOR CFW11 7,5 cv - 690 V - TROPICALIZADO (G3)",
                        "IHM REMOTA NA PORTA DO COMPARTIMENTO",
                        "CONFIGURAR PARA REDE IT/HRG (JUMPER RFI)",
                        "PE DEDICADO >= 10 mm2 (FUGA > 10 mA)",
                        "PLACA: AGUARDE 10 min APOS DESENERGIZAR"]):
    s.text(ln, X_ANNOT, 170.3 - k * 4.4, 2.2, "TEXTO", "left", Z_ANNOT)

s.line((X_FD, 145.0), (X_FD, 136.6))
s.circle(X_FD, 135.0, 1.6, check=False)
s.line((X_FD, 133.4), (X_FD, 117.0))
s.line((X_FD - 3, 122.0), (X_FD + 3, 126.0))
s.text("3", X_FD + 4.5, 124.0, 2.2, "TEXTO", "left")
s.text("X1..X4", X_TAG_R, 135.0, 2.6, "TAGS", "right")
s.line((X_FD + 3.0, 135.0), (X_LEADER, 135.0), lw=13)
s.text("BORNES DE SAIDA NO PROPRIO COMPARTIMENTO (FORMA 4b)",
       X_ANNOT, 135.0, 2.2, "TEXTO", "left", Z_ANNOT)

s.circle(X_FD, 108.0, 9.0)
s.text("M", X_FD, 110.2, 4.6, "ESQUEMA", "center", check=False)
s.text("3~", X_FD, 103.5, 2.7, "ESQUEMA", "center", check=False)
s.text("V1", X_TAG_R, 108.0, 3.4, "TAGS", "right")
s.line((X_FD + 9.5, 108.0), (X_LEADER, 108.0), lw=13)
s.text("STG-PF560AC - 5,5 kW - 660 V - IP66 - INVERTER DUTY",
       X_ANNOT, 110.2, 2.2, "TEXTO", "left", Z_ANNOT)
s.text("11-4412-VNT-2941-MT1", X_ANNOT, 105.8, 2.4, "TAGS", "left", Z_ANNOT)

# ---------------------------------------------- alimentadores 02..04 (fantasma)
GX0, GX1, GY0, GY1 = 208.0, 258.0, 142.0, 226.0
GXC = (GX0 + GX1) / 2
s.rect(GX0, GY0, GX1 - GX0, GY1 - GY0, "FANTASMA", dashed=True, lw=13)
s.line((GXC, Y_BUS - 1.8), (GXC, GY1), "FANTASMA", dashed=True, lw=13)
ghost = ["ALIMENTADORES 02, 03 E 04", "IGUAIS AO ALIMENTADOR 01", "",
         "11-4412-VNT-2942-MT1", "11-4412-VNT-2943-MT1", "11-4412-VNT-2944-MT1",
         "", "CADA UM EM SEU PROPRIO", "COMPARTIMENTO (FORMA 4b)"]
for k, ln in enumerate(ghost):
    if ln:
        s.text(ln, GXC, 196.0 - k * 5.6, 2.1, "FANTASMA", "center", Z_GHOST)

# ----------------------------------------------------------- legenda / simbolos
LX0, LY0, LX1, LY1 = 30.0, 28.0, 205.0, 88.0
s.rect(LX0, LY0, LX1 - LX0, LY1 - LY0, "MOLDURA", lw=18)
s.line((LX0, LY1 - 9.0), (LX1, LY1 - 9.0), "MOLDURA", lw=18)
s.text("LEGENDA / SIMBOLOGIA", (LX0 + LX1) / 2, LY1 - 4.5, 2.7, "TEXTO", "center",
       (LX0 + 2, LX1 - 2))
CA_S, CA_T, CB_S, CB_T = 42.0, 52.0, 130.0, 140.0
ZA, ZB = (CA_T, 126.0), (CB_T, LX1 - 2)
ROWS = (70.0, 56.0, 42.0)

# coluna A
y = ROWS[0]                                   # disjuntor
s.line((CA_S, y + 5), (CA_S, y + 3.2)); s.line((CA_S, y - 3.2), (CA_S, y - 5))
s.rect(CA_S - 3.2, y - 3.2, 6.4, 6.4)
s.line((CA_S - 3.2, y - 3.2), (CA_S + 3.2, y + 3.2), check=False)
s.line((CA_S - 3.2, y + 3.2), (CA_S + 3.2, y - 3.2), check=False)
s.text("DISJUNTOR EM CAIXA MOLDADA", CA_T, y, 2.2, "TEXTO", "left", ZA)
y = ROWS[1]                                   # seccionadora-fusivel
s.line((CA_S, y + 6.0), (CA_S, y + 3.6))
s.line((CA_S, y + 3.6), (CA_S + 3.6, y + 0.9))          # lamina
s.line((CA_S - 1.8, y - 0.4), (CA_S + 1.8, y - 0.4))    # contato fixo
s.line((CA_S, y - 0.4), (CA_S, y - 1.4))
s.rect(CA_S - 1.8, y - 5.4, 3.6, 4.0)                   # fusivel
s.line((CA_S, y - 5.4), (CA_S, y - 6.4))
s.text("SECCIONADORA-FUSIVEL", CA_T, y, 2.2, "TEXTO", "left", ZA)
y = ROWS[2]                                   # inversor
s.rect(CA_S - 5, y - 5, 10.0, 10.0)
s.line((CA_S - 5, y - 5), (CA_S + 5, y + 5), lw=13, check=False)
s.text("INVERSOR DE FREQUENCIA", CA_T, y, 2.2, "TEXTO", "left", ZA)

# coluna B
y = ROWS[0]                                   # motor
s.circle(CB_S, y, 5.0)
s.text("M", CB_S, y + 0.8, 3.0, "ESQUEMA", "center", check=False)
s.text("MOTOR TRIFASICO", CB_T, y, 2.2, "TEXTO", "left", ZB)
y = ROWS[1]                                   # borne
s.line((CB_S, y + 5), (CB_S, y + 1.6)); s.line((CB_S, y - 1.6), (CB_S, y - 5))
s.circle(CB_S, y, 1.6, check=False)
s.text("BORNE DE PASSAGEM", CB_T, y, 2.2, "TEXTO", "left", ZB)
y = ROWS[2]                                   # barramento
s.line((CB_S - 6, y + 0.9), (CB_S + 6, y + 0.9), lw=60)
s.line((CB_S - 6, y - 0.9), (CB_S + 6, y - 0.9), lw=60)
s.text("BARRAMENTO PRINCIPAL", CB_T, y, 2.2, "TEXTO", "left", ZB)

# ----------------------------------------------------------------- bloco notas
NX0, NX1, NY0, NY1 = 264.0, 408.0, 196.0, 272.0
s.rect(NX0, NY0, NX1 - NX0, NY1 - NY0, "MOLDURA", lw=18)
s.line((NX0, NY1 - 9.0), (NX1, NY1 - 9.0), "MOLDURA", lw=18)
s.text("NOTAS (CONCEITO REV.2)", (NX0 + NX1) / 2, NY1 - 4.5, 2.9, "NOTAS", "center", Z_NOTES)
for k, ln in enumerate([
        "1. PAINEL EM FORMA CONSTRUTIVA 4b (NBR IEC 61439-2),",
        "     CONFORME ELE-NRM-0001 ITEM 6.5.2.",
        "2. ENTRADA DE CABOS SOMENTE PELA PARTE INFERIOR,",
        "     COM PRENSA-CABOS PG, PRESERVANDO O GRAU IP.",
        "3. REDE 690 V ATERRADA POR ALTA RESISTENCIA (2 A 5 A).",
        "4. FORCA CLASSE 0,6/1 kV; COMANDO 1,0 mm2 NO MINIMO.",
        "5. SINALIZACAO: VERMELHO = LIGADO, VERDE = DESLIGADO,",
        "     AMARELO = FALHA (NR-10 / ELE-NRM-0008).",
        "6. SECCIONAMENTO BLOQUEAVEL EM TODAS AS FONTES (NR-12);",
        "     PAINEL COM MAIS DE UMA FONTE - VER PLACA.",
        "7. GRAU DE PROTECAO DO CONJUNTO: IP55 (PRC-0001 ITEM 6).",
        "8. Icc / Icu / Icw: CONFORME ESTUDO DE COORDENACAO."]):
    s.text(ln, NX0 + 3.0, NY1 - 14.5 - k * 4.7, 2.3, "NOTAS", "left", Z_NOTES)

# --------------------------------------------------------------- tabela cargas
s.text("TABELA DE CARGAS - ALIMENTADORES DO PAINEL", NX0, 166.0, 2.3, "TEXTO", "left",
       (NX0, NX1))
TX = [264.0, 282.0, 334.0, 368.0, 408.0]
TY1, TROW, THD = 160.0, 6.4, 7.4
s.rect(TX[0], TY1 - THD - 4 * TROW, TX[-1] - TX[0], THD + 4 * TROW, "MOLDURA", lw=18)
s.line((TX[0], TY1 - THD), (TX[-1], TY1 - THD), "MOLDURA", lw=18)
for x in TX[1:-1]:
    s.line((x, TY1 - THD - 4 * TROW), (x, TY1), "MOLDURA", lw=18)
for k in range(1, 4):
    y = TY1 - THD - k * TROW
    s.line((TX[0], y), (TX[-1], y), "MOLDURA", lw=18)
for i, htxt in enumerate(["ALIM.", "TAG DO MOTOR", "POTENCIA", "INVERSOR"]):
    s.text(htxt, (TX[i] + TX[i + 1]) / 2, TY1 - THD / 2, 2.3, "TEXTO", "center",
           (TX[i] + 1, TX[i + 1] - 1))
for k in range(4):
    y = TY1 - THD - TROW * (k + 0.5)
    for i, v in enumerate([f"0{k+1}", f"11-4412-VNT-294{k+1}-MT1",
                           "5,5 kW / 660 V", "CFW11 7,5 cv 690 V"]):
        s.text(v, (TX[i] + TX[i + 1]) / 2, y, 2.2, "TAGS" if i == 1 else "TEXTO",
               "center", (TX[i] + 1, TX[i + 1] - 1))

# ------------------------------------------------------------------ pendencias
PX0, PY0, PX1, PY1 = 264.0, 70.0, 408.0, 118.0
ZP = (PX0 + 2, PX1 - 2)
s.rect(PX0, PY0, PX1 - PX0, PY1 - PY0, "MOLDURA", lw=18)
s.line((PX0, PY1 - 9.0), (PX1, PY1 - 9.0), "MOLDURA", lw=18)
s.text("PENDENCIAS QUE AFETAM ESTA FOLHA", (PX0 + PX1) / 2, PY1 - 4.5, 2.6,
       "TEXTO", "center", ZP)
for k, ln in enumerate(["Q1 - Icc NO PONTO DE ALIMENTACAO (QSA-0003)",
                        "Q5 - GRAU IP EXIGIDO NA CASA DE MAQUINAS",
                        "Q7 - PADRAO DE CORES DE SINALIZACAO",
                        "REF.: RELATORIO DE CONFORMIDADE MF00965787"]):
    s.text(ln, PX0 + 3.0, PY1 - 15.0 - k * 6.0, 2.3,
           "TAGS" if k < 3 else "TEXTO", "left", ZP)

# --------------------------------------------------------------------- carimbo
CX, CY, CW, CH = SHEET_W - MARGIN - 185.0, MARGIN, 185.0, 52.0
s.rect(CX, CY, CW, CH, "CARIMBO", lw=35)
for dy in (13.0, 26.0, 39.0):
    s.line((CX, CY + dy), (CX + CW, CY + dy), "CARIMBO", lw=18)
s.line((CX + 118.0, CY + 26.0), (CX + 118.0, CY + 39.0), "CARIMBO", lw=18)
ZTB = (CX + 2, CX + CW - 2)
s.text("STORGE ENGENHARIA   |   VALMET   |   ARAUCO - PROJETO SUCURIU",
       CX + CW / 2, CY + 45.5, 2.6, "CARIMBO", "center", ZTB)
s.text("ESQUEMA ELETRICO - PRESSURIZACAO DAS ESCADAS",
       CX + 59.0, CY + 32.5, 2.5, "CARIMBO", "center", (CX + 2, CX + 116))
s.text("11-4400-PEL-0301  REV.2 (MINUTA)",
       CX + 151.5, CY + 32.5, 2.3, "CARIMBO", "center", (CX + 120, CX + CW - 2))
s.text("FOLHA-PILOTO GERADA POR CODIGO (ezdxf) - PROVA DE CONCEITO",
       CX + CW / 2, CY + 19.5, 2.4, "CARIMBO", "center", ZTB)
s.text("SUBSTITUIR PELO CARIMBO OFICIAL: Formato_A3_Valmet.dwg",
       CX + CW / 2, CY + 6.5, 2.4, "CARIMBO", "center", ZTB)

# ------------------------------------------------------------------- validacao
probs = s.validate()
print(f"textos verificados: {len(s.tboxes)} | segmentos: {len(s.segments)}")
if probs:
    print(f"*** {len(probs)} OCORRENCIAS ***")
    for p in probs[:40]:
        print("   -", p)
    raise SystemExit(1)
print(">>> LAYOUT LIMPO: 0 sobreposicoes, 0 estouros de zona.")

doc.set_modelspace_vport(height=SHEET_H * 1.06, center=(SHEET_W / 2, SHEET_H / 2))
doc.saveas("PEL-0301_unifilar_piloto.dxf")

from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
for out in ("PEL-0301_unifilar_piloto.png", "PEL-0301_unifilar_piloto.pdf"):
    fig = plt.figure(figsize=(16.54, 11.69), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ctx = RenderContext(doc)
    ctx.set_current_layout(s.msp)
    Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(s.msp, finalize=True)
    fig.savefig(out, facecolor="white")
    plt.close(fig)
print("gerado: DXF + PNG + PDF")
