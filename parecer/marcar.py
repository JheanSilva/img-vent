# -*- coding: utf-8 -*-
"""Carimba as notas de revisao sobre o MF00965787 rev.1 e monta o parecer."""
import io
import textwrap
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from pypdf import PdfReader, PdfWriter
from notas import FOLHAS, CRIT, IMP, INFO, PEND

W, H = 1191.0, 842.0
DPI = 50.0
PXPT = DPI / 72.0

VERM = HexColor("#B3261E")
LAR = HexColor("#8A5A00")
AZUL = HexColor("#1F4E79")
ROXO = HexColor("#6A2E87")
CINZA = HexColor("#4A4A4A")
COR = {CRIT: VERM, IMP: LAR, INFO: AZUL, PEND: ROXO}
SIGLA = {CRIT: "CRITICO", IMP: "IMPORTANTE", INFO: "INFO", PEND: "PENDENCIA"}


# ------------------------------------------------------------ area livre
def mapa_tinta(png):
    im = Image.open(png).convert("L")
    px = im.load()
    w, h = im.size
    ii = [[0] * (w + 1) for _ in range(h + 1)]
    for y in range(h):
        lin = 0
        for x in range(w):
            lin += 1 if px[x, y] < 235 else 0
            ii[y + 1][x + 1] = ii[y][x + 1] + lin
    return ii, w, h


def tinta(ii, x0, y0, x1, y1):
    return ii[y1][x1] - ii[y0][x1] - ii[y1][x0] + ii[y0][x0]


def area_livre(png, hpt, larguras=(575, 520, 465, 410, 360)):
    """Retorna (x, y, w, h) em pontos PDF para o painel de notas."""
    ii, wpx, hpx = mapa_tinta(png)
    hpx_need = int(hpt * PXPT)
    melhor, melhor_tinta = None, None
    for wpt in larguras:
        wpx_need = int(wpt * PXPT)
        if wpx_need >= wpx - 20 or hpx_need >= hpx - 20:
            continue
        cands = []
        for yy in range(10, hpx - hpx_need - 10, 6):
            for xx in range(10, wpx - wpx_need - 10, 6):
                t = tinta(ii, xx, yy, xx + wpx_need, yy + hpx_need)
                cands.append((t, xx, yy, wpt))
        if not cands:
            continue
        cands.sort(key=lambda c: (c[0], -(c[1] + c[2])))
        t, xx, yy, wpt = cands[0]
        if t == 0:
            x = xx / PXPT
            y = H - (yy + hpx_need) / PXPT
            return (x, y, wpt, hpt)
        if melhor is None or t < melhor_tinta:
            melhor, melhor_tinta = (xx / PXPT, H - (yy + hpx_need) / PXPT, wpt, hpt), t
    return melhor or (20.0, 20.0, 400.0, hpt)


# ------------------------------------------------------------ utilitarios
def wrap(txt, fonte, tam, larg):
    out, linha = [], ""
    for p in txt.split():
        t = (linha + " " + p).strip()
        if stringWidth(t, fonte, tam) <= larg:
            linha = t
        else:
            if linha:
                out.append(linha)
            linha = p
    if linha:
        out.append(linha)
    return out


def corta(txt, fonte, tam, larg):
    if stringWidth(txt, fonte, tam) <= larg:
        return txt
    palavras = txt.split()
    saida = ""
    for p in palavras:
        t = (saida + " " + p).strip()
        if stringWidth(t + " ...", fonte, tam) > larg:
            break
        saida = t
    return (saida + " ...") if saida else txt[:3] + "..."


# ------------------------------------------------------------ carimbo
def desenha_carimbo(c, num, titulo, itens, rect):
    x, y, w, h = rect
    c.saveState()
    c.setFillColor(Color(1, 1, 1, alpha=0.94))
    c.setStrokeColor(VERM)
    c.setLineWidth(1.6)
    c.roundRect(x, y, w, h, 5, stroke=1, fill=1)
    c.setFillColor(VERM)
    c.roundRect(x, y + h - 17, w, 17, 5, stroke=0, fill=1)
    c.rect(x, y + h - 17, w, 8, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x + 7, y + h - 12.5, "NOTAS DE REVISAO  -  FOLHA %s/11  -  %s" % (num, titulo))
    c.setFont("Helvetica", 7)
    c.drawRightString(x + w - 7, y + h - 12.5, "STORGE ENG.")
    yy = y + h - 29
    for it in itens:
        cor = COR[it["p"]]
        c.setFillColor(cor)
        c.setFont("Helvetica-Bold", 7.4)
        c.drawString(x + 7, yy, it["id"])
        c.circle(x + 4, yy + 2.4, 1.7, stroke=0, fill=1)
        c.setFillColor(CINZA)
        c.setFont("Helvetica", 6.4)
        c.drawString(x + 30, yy, "[" + SIGLA[it["p"]][:4] + "]")
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica-Bold", 7.2)
        onde = it["onde"] + "  -  "
        c.drawString(x + 55, yy, onde)
        wo = stringWidth(onde, "Helvetica-Bold", 7.2)
        c.setFont("Helvetica", 7.2)
        c.drawString(x + 55 + wo, yy, corta(it["acao"], "Helvetica", 7.2, w - 62 - wo))
        yy -= 10.4
    c.setFillColor(CINZA)
    c.setFont("Helvetica-Oblique", 6.6)
    c.drawString(x + 7, y + 6, "Por que / como fazer: ver a pagina seguinte deste caderno.  "
                               "Ref.: Relatorio de Conformidade do MF00965787.")
    c.restoreState()
    # selo no canto
    c.saveState()
    c.setFillColor(VERM)
    c.setStrokeColor(VERM)
    c.setLineWidth(1.2)
    c.rect(14, H - 34, 118, 20, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(73, H - 27.5, "REVISAO EXIGIDA")
    c.restoreState()


# ------------------------------------------------------------ pagina detalhe
def pagina_detalhe(c, num, titulo, itens):
    def cab():
        c.setFillColor(VERM)
        c.rect(0, H - 46, W, 46, stroke=0, fill=1)
        c.setFillColorRGB(1, 1, 1)
        c.setFont("Helvetica-Bold", 15)
        c.drawString(34, H - 30, "FOLHA %s  -  %s" % (num, titulo))
        c.setFont("Helvetica", 9)
        c.drawRightString(W - 34, H - 29, "PARECER TECNICO DE REVISAO  -  11-4400-PEL-0301 / MF00965787 rev.1")

    cab()
    colw = (W - 100) / 2.0
    cols = [(34, colw), (34 + colw + 32, colw)]
    ci, y = 0, H - 68
    for it in itens:
        blocos = [("t", "%s   %s" % (it["id"], SIGLA[it["p"]])),
                  ("o", "ONDE: " + it["onde"]),
                  ("a", "ACAO: " + it["acao"]),
                  ("p", "POR QUE: " + it["porque"]),
                  ("c", "COMO: " + it["como"]),
                  ("r", "REF.: " + it["ref"])]
        linhas = []
        for k, txt in blocos:
            fonte = "Helvetica-Bold" if k in ("t", "a") else "Helvetica"
            tam = 9.5 if k == "t" else (8.2 if k == "a" else 7.8)
            for ln in wrap(txt, fonte, tam, cols[ci][1] - 10):
                linhas.append((k, ln, fonte, tam))
        alt = sum(11.5 if k == "t" else 9.6 for k, _, _, _ in linhas) + 9
        if y - alt < 40:
            ci += 1
            if ci > 1:
                c.showPage()
                cab()
                ci, y = 0, H - 68
            else:
                y = H - 68
        x0 = cols[ci][0]
        c.setStrokeColor(COR[it["p"]])
        c.setLineWidth(2.2)
        c.line(x0 - 5, y + 8, x0 - 5, y - alt + 14)
        for k, ln, fonte, tam in linhas:
            if k == "t":
                c.setFillColor(COR[it["p"]])
                c.setFont("Helvetica-Bold", 9.5)
                c.drawString(x0, y, ln)
                y -= 11.5
            else:
                c.setFillColorRGB(0.1, 0.1, 0.1) if k == "a" else c.setFillColor(CINZA)
                c.setFont(fonte, tam)
                c.drawString(x0, y, ln)
                y -= 9.6
        y -= 9
    c.showPage()


# ------------------------------------------------------------ capa e checklist
def pagina_capa(c):
    c.setFillColor(VERM)
    c.rect(0, H - 120, W, 120, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(46, H - 60, "PARECER TECNICO DE REVISAO")
    c.setFont("Helvetica", 15)
    c.drawString(46, H - 84, "Painel de pressurizacao das escadas da Caldeira de Recuperacao")
    c.setFont("Helvetica", 11)
    c.drawString(46, H - 104, "11-4400-PEL-0301  /  Valmet MF00965787 rev.1  -  Arauco Projeto Sucuriu, Inocencia/MS")

    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(46, H - 152, "O QUE E ESTE DOCUMENTO")
    c.setFont("Helvetica", 9.6)
    y = H - 170
    for ln in ["Este caderno reproduz as 11 folhas do esquema eletrico na revisao 1 com as notas de revisao carimbadas sobre cada folha.",
               "Depois de cada folha vem uma pagina de detalhamento explicando, item a item, o que precisa ser incluido ou modificado,",
               "por que (com a norma ou o documento contratual que obriga) e como fazer. Ao final ha um checklist para acompanhamento.",
               "As notas nasceram do Relatorio de Conformidade do MF00965787, que confrontou o projeto com a EN-ITE-839 (NR-10/NR-12),",
               "a ETC MF00857651, a planilha de equalizacao (ATN) e as normas Arauco aplicaveis."]:
        c.drawString(46, y, ln)
        y -= 14

    c.setFont("Helvetica-Bold", 12)
    c.drawString(46, y - 14, "COMO LER AS MARCACOES")
    y -= 34
    for cor, nome, desc in [(VERM, "CRITICO", "reprova na analise do cliente ou infringe norma - tem de ser resolvido nesta revisao"),
                            (LAR, "IMPORTANTE", "exigencia normativa ou contratual nao atendida - resolver nesta revisao"),
                            (AZUL, "INFO", "inconsistencia documental ou ajuste editorial - corrigir ao revisar"),
                            (ROXO, "PENDENCIA", "depende de informacao do cliente - registrar a consulta e nao emitir sem resposta")]:
        c.setFillColor(cor)
        c.circle(50, y + 3, 3.6, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 9.6)
        c.drawString(60, y, nome)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.setFont("Helvetica", 9.6)
        c.drawString(132, y, "- " + desc)
        y -= 16

    # resumo por folha
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(660, H - 152, "RESUMO POR FOLHA")
    yy = H - 174
    c.setFont("Helvetica-Bold", 8.6)
    for t, x in (("FOLHA", 660), ("DESCRICAO", 700), ("CRIT", 900), ("IMP", 940), ("INFO", 978), ("PEND", 1020), ("TOTAL", 1064)):
        c.drawString(x, yy, t)
    yy -= 4
    c.setLineWidth(0.8)
    c.setStrokeColor(CINZA)
    c.line(660, yy, 1110, yy)
    yy -= 12
    tot = [0, 0, 0, 0]
    for num, titulo, itens in FOLHAS:
        n = [sum(1 for i in itens if i["p"] == p) for p in (CRIT, IMP, INFO, PEND)]
        tot = [a + b for a, b in zip(tot, n)]
        c.setFont("Helvetica-Bold", 8.4)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(660, yy, num)
        c.setFont("Helvetica", 8.4)
        c.drawString(700, yy, titulo[:34])
        for v, x, cor in zip(n, (900, 940, 978, 1020), (VERM, LAR, AZUL, ROXO)):
            c.setFillColor(cor if v else CINZA)
            c.drawString(x + 6, yy, str(v) if v else "-")
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica-Bold", 8.4)
        c.drawString(1070, yy, str(sum(n)))
        yy -= 13
    c.line(660, yy + 5, 1110, yy + 5)
    yy -= 8
    c.setFont("Helvetica-Bold", 8.6)
    c.drawString(700, yy, "TOTAL")
    for v, x in zip(tot, (900, 940, 978, 1020)):
        c.drawString(x + 6, yy, str(v))
    c.drawString(1070, yy, str(sum(tot)))

    # comentarios do cliente e pendencias
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(46, 452, "COMENTARIOS DO CLIENTE NA REV.1  -  ONDE FORAM TRATADOS")
    yy = 432
    for txt, ids in [("Compartimentar painel para se adequar a categoria 4B", "C1  (folhas 04 e 09)"),
                     ("Chave de manobra do disjuntor de entrada na porta, para bloqueio", "C2  (folhas 04 e 09)"),
                     ("IHM dos VFD na porta do painel", "C3  (folhas 07, 08 e 09)"),
                     ("Identificar todas as sinalizacoes por tag das cargas", "C4  (folhas 07, 08 e 09)"),
                     ("Bloqueio individual de todas as cargas por metodo mecanico na porta", "C5  (folhas 04 e 09)"),
                     ("Entrada de cabos somente pela parte inferior do painel", "C6  (folhas 04 e 09)")]:
        c.setFillColor(VERM)
        c.setFont("Helvetica-Bold", 8.6)
        c.drawString(50, yy, "-")
        c.setFillColorRGB(0.1, 0.1, 0.1)
        c.setFont("Helvetica", 8.8)
        c.drawString(60, yy, txt)
        c.setFillColor(VERM)
        c.setFont("Helvetica-Bold", 8.8)
        c.drawString(420, yy, ids)
        yy -= 15
    c.setFillColorRGB(0.25, 0.25, 0.25)
    c.setFont("Helvetica-Oblique", 8.4)
    c.drawString(50, yy - 4, "Os seis comentarios da rev.1 continuam pendentes; as demais notas deste parecer o cliente ainda nao apontou.")

    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(660, 452, "CONSULTAR A VALMET ANTES DE EMITIR")
    yy = 432
    for q, txt in [("Q1", "Icc no ponto de alimentacao (saida do CCM 11-4400-QSA-0003)"),
                   ("Q2", "Origem 690 V e 220 V: barra normal, de emergencia ou UPS"),
                   ("Q3", "Folha de dados do motor: 660 V, IP66, PTC e aquecedor"),
                   ("Q4", "Vendor list do cliente para protecoes, inversores e acessorios"),
                   ("Q5", "Grau IP exigido para o painel na casa de maquinas"),
                   ("Q6", "Lista de sinais definitiva com o DCS (contato seco ou analogico)"),
                   ("Q7", "Padrao de cores de sinalizacao e de fiacao"),
                   ("Q10", "Apreciacao de riscos NR-12 e necessidade de botao de emergencia"),
                   ("Q11", "Aceitacao da interface sem fio do controlador de pressao"),
                   ("Q12", "Modelo do ventilador: PF630 da proposta x PF560 do projeto")]:
        c.setFillColor(ROXO)
        c.setFont("Helvetica-Bold", 8.8)
        c.drawString(664, yy, q)
        c.setFillColorRGB(0.1, 0.1, 0.1)
        c.setFont("Helvetica", 8.8)
        c.drawString(692, yy, txt)
        yy -= 15

    c.setStrokeColor(VERM)
    c.setLineWidth(1.2)
    c.rect(46, 46, 1099, 74, stroke=1, fill=0)
    c.setFillColor(VERM)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(58, 100, "ANTES DE EMITIR")
    c.setFillColorRGB(0.15, 0.15, 0.15)
    c.setFont("Helvetica", 9)
    c.drawString(58, 84, "Pela ATN (itens 9 e 21) e pela ETC 3.3, o comentario ou a aceitacao da Valmet nao exime o fornecedor: desvio nao levantado vale como cumprimento integral,")
    c.drawString(58, 71, "e a correcao e exigivel a qualquer tempo, mesmo apos a instalacao. Todo item deste parecer que nao for atendido precisa ser formalizado como desvio e aceito por escrito.")
    c.drawString(58, 58, "Este parecer e documento de apoio a revisao; a emissao do projeto exige verificacao e ART de profissional legalmente habilitado.")
    c.showPage()


def pagina_checklist(c):
    c.setFillColor(VERM)
    c.rect(0, H - 46, W, 46, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(34, H - 30, "CHECKLIST DE REVISAO")
    c.setFont("Helvetica", 9)
    c.drawRightString(W - 34, H - 29, "marcar a medida que cada item for incorporado a revisao 2")
    linhas = []
    for num, titulo, itens in FOLHAS:
        for it in itens:
            linhas.append((num, it))
    meio = (len(linhas) + 1) // 2
    for ci, bloco in enumerate((linhas[:meio], linhas[meio:])):
        x0 = 34 + ci * (W - 68) / 2.0
        y = H - 70
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(x0 + 18, y, "FL")
        c.drawString(x0 + 38, y, "ITEM")
        c.drawString(x0 + 76, y, "ACAO")
        y -= 4
        c.setStrokeColor(CINZA)
        c.setLineWidth(0.7)
        c.line(x0, y, x0 + (W - 68) / 2.0 - 24, y)
        y -= 13
        for num, it in bloco:
            c.setStrokeColorRGB(0.35, 0.35, 0.35)
            c.setLineWidth(0.8)
            c.rect(x0, y - 1.5, 8, 8, stroke=1, fill=0)
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Helvetica", 7.6)
            c.drawString(x0 + 18, y, num)
            c.setFillColor(COR[it["p"]])
            c.setFont("Helvetica-Bold", 7.6)
            c.drawString(x0 + 38, y, it["id"])
            c.setFillColorRGB(0.1, 0.1, 0.1)
            c.setFont("Helvetica", 7.6)
            c.drawString(x0 + 76, y, corta(it["acao"], "Helvetica", 7.6, (W - 68) / 2.0 - 100))
            y -= 12.4
    c.showPage()


# ------------------------------------------------------------ montagem
def main():
    # 1) overlays dos carimbos
    buf_ov = io.BytesIO()
    c = canvas.Canvas(buf_ov, pagesize=(W, H))
    rects = []
    for num, titulo, itens in FOLHAS:
        hpt = 29 + len(itens) * 10.4 + 12
        r = area_livre("pg-%s.png" % num, hpt)
        rects.append(r)
        desenha_carimbo(c, num, titulo, itens, r)
        c.showPage()
    c.save()
    buf_ov.seek(0)

    # 2) capa, detalhes e checklist
    buf_tx = io.BytesIO()
    c = canvas.Canvas(buf_tx, pagesize=(W, H))
    pagina_capa(c)
    marcas = [1]
    for num, titulo, itens in FOLHAS:
        antes = c.getPageNumber()
        pagina_detalhe(c, num, titulo, itens)
        marcas.append(c.getPageNumber() - antes)
    pagina_checklist(c)
    c.save()
    buf_tx.seek(0)

    base = PdfReader("original.pdf")
    ov = PdfReader(buf_ov)
    tx = PdfReader(buf_tx)
    out = PdfWriter()
    out.add_page(tx.pages[0])                      # capa
    p = 1
    for i in range(11):
        pg = base.pages[i]
        pg.merge_page(ov.pages[i])
        out.add_page(pg)
        for _ in range(marcas[i + 1]):
            out.add_page(tx.pages[p])
            p += 1
    out.add_page(tx.pages[p])                      # checklist
    with open("PARECER_MF00965787_rev1.pdf", "wb") as fh:
        out.write(fh)
    print("paginas:", len(out.pages))
    for (num, _, itens), r in zip(FOLHAS, rects):
        print("  folha %s: %2d notas  painel em x=%4.0f y=%4.0f  %3.0f x %3.0f pt"
              % (num, len(itens), r[0], r[1], r[2], r[3]))


main()
