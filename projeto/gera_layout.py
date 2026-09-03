# -*- coding: utf-8 -*-
"""Layout do painel 11-4400-PEL-0301 com footprints reais dos catalogos WEG."""
import os
from folha import Folha

E = 10.0                      # escala 1:10
PW, PH, PD = 1000.0, 2200.0, 500.0     # painel do projeto original
BW, BH = 900.0, 2100.0                 # placa de montagem (premissa)

# footprints reais (mm): largura, altura, profundidade
CFW = (300.0, 550.0, 305.0)   # CFW11 0007 T6 - tamanho D
FSW = (89.0, 180.0, 81.0)     # FSW 100-3
MDW125 = (80.7, 90.0, 65.4)   # MDW 70-125 A, 3 polos
MDW3 = (54.0, 83.0, 67.0)     # MDWP/MDWS 3 polos
MDW2 = (36.0, 83.0, 67.0)     # MDWP/MDWS 2 polos
FOLGA_LAT, FOLGA_SUP, FOLGA_INF = 30.0, 110.0, 130.0   # nota do projeto original


def mm(v):
    return v / E


def vista_placa(f, x0, y0):
    """Vista da placa de montagem. x0,y0 = canto inferior esquerdo do painel."""
    f.rect(x0, y0, mm(PW), mm(PH), lw=35)                      # painel
    px, py = x0 + mm(50), y0 + mm(50)
    f.rect(px, py, mm(BW), mm(BH), "COMP", lw=18)              # placa

    def peca(xr, yr, w, h, tag, layer="ESQUEMA", lw=25):
        f.rect(px + mm(xr), py + mm(yr), mm(w), mm(h), layer, lw=lw)
        return px + mm(xr) + mm(w) / 2, py + mm(yr) + mm(h) / 2

    # canaletas verticais
    for xr in (0.0, 850.0):
        f.rect(px + mm(xr), py, mm(50), mm(BH), "FANTASMA", lw=13)
    # trilho DIN 1 - protecoes
    xr = 70.0
    peca(xr, 2010, *MDW125[:2], "Q1")
    xr += MDW125[0] + 20
    for k in range(4):
        peca(xr, 2010, *MDW3[:2], "Q%d" % (k + 2))
        xr += MDW3[0] + 12
    xr += 20
    for k in range(2):
        peca(xr, 2010, *MDW2[:2], "Q%d" % (k + 6))
        xr += MDW2[0] + 12
    f.text("TRILHO DIN 1", px + mm(620), py + mm(2055), 1.9, "TEXTO",
           "left", (px + mm(615), px + mm(840)))
    # trilho DIN 2 - comando
    f.rect(px + mm(70), py + mm(1900), mm(420), mm(90), "ESQUEMA", lw=18)
    f.text("G1 / K1 / RELES / STG", px + mm(80), py + mm(1945), 1.8, "TEXTO",
           "left", (px + mm(72), px + mm(500)))
    # canaleta horizontal
    f.rect(px + mm(50), py + mm(1840), mm(800), mm(60), "FANTASMA", lw=13)
    # seccionadoras
    passo = (BW - 100 - 4 * FSW[0]) / 3.0
    for k in range(4):
        xr = 50 + k * (FSW[0] + passo)
        peca(xr, 1660, *FSW[:2], "F%d" % (k + 1))
    f.rect(px + mm(50), py + mm(1600), mm(800), mm(60), "FANTASMA", lw=13)
    # inversores 2 x 2
    bx = (BW - (2 * CFW[0] + 2 * FOLGA_LAT)) / 2.0
    for lin in range(2):
        yb = 940.0 - lin * (CFW[1] + FOLGA_INF)
        for col in range(2):
            xr = bx + col * (CFW[0] + 2 * FOLGA_LAT)
            f.rect(px + mm(xr), py + mm(yb), mm(CFW[0]), mm(CFW[1]), lw=30)
            f.rect(px + mm(xr - FOLGA_LAT), py + mm(yb - FOLGA_INF),
                   mm(CFW[0] + 2 * FOLGA_LAT), mm(CFW[1] + FOLGA_INF + FOLGA_SUP),
                   "FANTASMA", dashed=True, lw=13)
            f.text("U%d" % (2 * lin + col + 1), px + mm(xr + CFW[0] / 2),
                   py + mm(yb + CFW[1] / 2), 3.4, "TAGS", "center", None)
    # canaleta e bornes
    f.rect(px + mm(50), py + mm(120), mm(800), mm(60), "FANTASMA", lw=13)
    f.rect(px + mm(70), py + mm(40), mm(700), mm(70), "ESQUEMA", lw=18)
    f.text("REGUAS X / Y", px + mm(80), py + mm(75), 1.9, "TEXTO", "left",
           (px + mm(72), px + mm(760)))
    return px, py


def vista_porta(f, x0, y0):
    f.rect(x0, y0, mm(PW), mm(PH), lw=35)
    f.rect(x0 + mm(30), y0 + mm(30), mm(PW - 60), mm(PH - 60), lw=13)
    for c in range(4):
        for r in range(3):
            f.circle(x0 + mm(200 + c * 200), y0 + mm(1500 - r * 150), mm(22) / 2)
    f.circle(x0 + mm(200), y0 + mm(1000), mm(22) / 2)
    f.circle(x0 + mm(600), y0 + mm(1000), mm(22) / 2)
    f.circle(x0 + mm(800), y0 + mm(1000), mm(22) / 2)


def vista_lateral(f, x0, y0):
    f.rect(x0, y0, mm(PD), mm(PH), lw=35)
    f.rect(x0 + mm(60), y0 + mm(1750), mm(300), mm(250), lw=13)


def folha_1():
    f = Folha("L1", "Layout do Painel - Vistas", total="2",
              nota_rev="ESTUDO DE LAYOUT SOBRE O PROJETO REV.1  -  FOOTPRINTS WEG  -  NAO SUBSTITUI O PROJETO")
    XA, XB, XC, Y0 = 32.0, 152.0, 282.0, 56.0
    vista_placa(f, XA, Y0)
    vista_porta(f, XB, Y0)
    vista_lateral(f, XC, Y0)
    for x, w, nome in ((XA, PW, "VISTA A - PLACA DE MONTAGEM"),
                       (XB, PW, "VISTA B - PORTA"),
                       (XC, PD, "VISTA C - LATERAL - PROF. 500")):
        f.text(nome, x + mm(w) / 2, 281, 2.3, "TEXTO", "center",
               (x - 26, x + mm(w) + 26))
    # cotas principais
    for x, w, txt in ((XA, PW, "1000"),):
        y = Y0 - 6
        f.line((x, y), (x + mm(w), y), lw=13)
        f.line((x, y - 2), (x, y + 2), lw=13)
        f.line((x + mm(w), y - 2), (x + mm(w), y + 2), lw=13)
        f.text(txt, x + mm(w) / 2, y - 4, 2.2, "TEXTO", "center",
               (x - 12, x + mm(w) + 12))
    f.line((XA - 7, Y0), (XA - 7, Y0 + mm(PH)), lw=13)
    f.line((XA - 9, Y0), (XA - 5, Y0), lw=13)
    f.line((XA - 9, Y0 + mm(PH)), (XA - 5, Y0 + mm(PH)), lw=13)
    f.text("2200", XA - 9, Y0 + mm(PH) / 2, 2.2, "TEXTO", "right", (11, XA - 8))

    f.bloco(345, 60, 408, 274, "NOTAS", [
        "ESCALA 1:10",
        "COTAS EM mm",
        "",
        "PAINEL 1000 x 2200",
        "x 500 (PROJETO REV.1)",
        "",
        "PLACA DE MONTAGEM",
        "900 x 2100 (PREMISSA)",
        "",
        "TRACEJADO EM VOLTA",
        "DOS INVERSORES =",
        "AFASTAMENTO DE",
        "VENTILACAO",
        "30 mm LATERAL,",
        "110 mm SUPERIOR,",
        "130 mm INFERIOR",
        "(NOTA DA FOLHA 09",
        "DO PROJETO REV.1)",
        "",
        "FOOTPRINTS REAIS",
        "DOS CATALOGOS WEG",
        "- VER FOLHA L2",
    ], h=1.9, lh=4.3)
    return f


def folha_2():
    f = Folha("L2", "Layout do Painel - Componentes e Fontes", total="2",
              nota_rev="ESTUDO DE LAYOUT SOBRE O PROJETO REV.1  -  FOOTPRINTS WEG  -  NAO SUBSTITUI O PROJETO")
    f.text("COMPONENTES E ORIGEM DAS DIMENSOES", 15, 268, 3.0, "TEXTO", "left", (15, 250))
    linhas = [
        ("U1..U4", "CFW11 0007 T6 - inversor 7 A / 7,5 cv - tamanho D", "300", "550", "305",
         "placa", "Catalogo CFW11 (pt) - Dimensoes e Pesos"),
        ("F1..F4", "FSW 100-3 - seccionadora fusivel NH000 100 A", "89", "180", "81",
         "placa", "Catalogo Chaves Seccionadoras - pag. 8"),
        ("Q1", "MDW-C125-3 - minidisjuntor 125 A 3 polos", "80,7", "90", "65,4",
         "trilho DIN", "Cat. Solucoes Integradas - pag. 29"),
        ("Q2..Q5", "MDW-C10-3 - minidisjuntor 10 A 3 polos", "54", "83", "67",
         "trilho DIN", "Cat. Solucoes Integradas - pag. 29"),
        ("Q6, Q7", "MDW-C10-2 - minidisjuntor 10 A 2 polos", "36", "83", "67",
         "trilho DIN", "Cat. Solucoes Integradas - pag. 29"),
        ("G1", "Fonte 24 Vcc", "A CONF.", "A CONF.", "A CONF.",
         "trilho DIN", "NAO E WEG - confirmar no fabricante"),
        ("K1", "Contator auxiliar CWCA0", "A CONF.", "A CONF.", "A CONF.",
         "trilho DIN", "Nao extraido - confirmar no catalogo"),
        ("K2, K4, K5", "Borne rele 24 Vcc", "A CONF.", "A CONF.", "A CONF.",
         "trilho DIN", "Nao extraido - confirmar no catalogo"),
        ("STG", "Controlador de pressao", "A CONF.", "A CONF.", "A CONF.",
         "trilho DIN", "Produto Storge - dado interno"),
        ("H1..H13", "Sinaleiro LED 22 mm", "22", "22", "-",
         "porta", "Furo padrao 22 mm"),
        ("S1, S2", "Botao 22 mm", "22", "22", "-",
         "porta", "Furo padrao 22 mm"),
        ("X, Y", "Bornes Phoenix PT4 / PT2,5", "A CONF.", "A CONF.", "A CONF.",
         "trilho DIN", "NAO E WEG - confirmar no fabricante"),
    ]
    f.tabela(15, 258, ["TAG", "COMPONENTE", "L", "A", "P", "MONTAGEM", "ORIGEM DA DIMENSAO"],
             linhas, h=2.1, row_h=6.4,
             widths=[26.0, 118.0, 18.0, 18.0, 18.0, 26.0, 96.0],
             aligns=["center", "left", "center", "center", "center", "center", "left"],
             layers=["TAGS", "TEXTO", "TEXTO", "TEXTO", "TEXTO", "TEXTO", "TEXTO"])

    f.bloco(15, 60, 205, 158, "VERIFICACAO DE OCUPACAO", [
        "ALTURA (placa util 2100 mm):",
        "   trilho DIN 1 (protecoes) ................  90",
        "   trilho DIN 2 (comando) ..................  90",
        "   canaleta horizontal .....................  60",
        "   seccionadoras F1..F4 .................... 180",
        "   canaleta horizontal .....................  60",
        "   inversores 2 x 2 com afastamentos ....... 1470",
        "   canaleta e reguas de bornes ............. 150",
        "   TOTAL OCUPADO .......................... 2100",
        "",
        "LARGURA (placa util 900 mm):",
        "   dois inversores lado a lado com",
        "   afastamento lateral de 30 mm ............ 720",
        "   FOLGA REMANESCENTE ...................... 180",
    ], h=2.0, lh=4.6)
    f.bloco(215, 60, 405, 158, "OBSERVACOES", [
        "1. O ARRANJO 2 x 2 DOS INVERSORES DO PROJETO REV.1 CABE",
        "   NO PAINEL DE 1000 x 2200, MAS SEM FOLGA VERTICAL: A SOMA",
        "   DAS ZONAS DA ESQUERDA FECHA EXATAMENTE OS 2100 mm.",
        "2. QUALQUER ACRESCIMO (RESERVA, SEGREGACAO 4b, CLIMATIZACAO)",
        "   EXIGE PAINEL MAIOR OU SEGUNDA COLUNA.",
        "3. A PROFUNDIDADE DO INVERSOR E 305 mm EM UM PAINEL DE 500 mm.",
        "4. A ALAVANCA DA FSW 100 PROJETA 211 mm A PARTIR DA PLACA.",
        "5. AS LINHAS TRACEJADAS SAO OS AFASTAMENTOS DE VENTILACAO,",
        "   NAO PODEM SER OCUPADAS POR CANALETA OU COMPONENTE.",
        "6. ESTE ESTUDO E DE LAYOUT: NAO TRATA DE ADEQUACAO TECNICA",
        "   NEM SUBSTITUI OS ITENS DO PARECER DE REVISAO.",
    ], h=2.0, lh=4.6)
    return f


if __name__ == "__main__":
    os.makedirs("dxf_layout", exist_ok=True)
    for nome, fn in (("L1", folha_1), ("L2", folha_2)):
        f = fn()
        pr = f.validate()
        if pr:
            print("FOLHA %s: %d ocorrencias" % (nome, len(pr)))
            for p in pr[:10]:
                print("   -", p)
        else:
            f.save("dxf_layout/LAYOUT_%s.dxf" % nome)
            print("FOLHA %s: OK (%d textos, %d segmentos)" % (nome, len(f.tboxes), len(f.segments)))
