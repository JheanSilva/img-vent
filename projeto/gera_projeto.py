# -*- coding: utf-8 -*-
"""Gera as 11 folhas da rev.02 do 11-4400-PEL-0301 (minuta)."""
import os
import sys
from folha import Folha, PAGINAS

OUT = "dxf"
MOTORES = ["11-4412-VNT-2941-MT1", "11-4412-VNT-2942-MT1",
           "11-4412-VNT-2943-MT1", "11-4412-VNT-2944-MT1"]


# ============================================================ 01 CAPA
def p01():
    f = Folha("01", "Capa")
    f.text("ESQUEMA ELETRICO", 210, 266, 8.0, "TEXTO", "center", (15, 405))
    f.text("PAINEL DE PRESSURIZACAO DAS ESCADAS - CALDEIRA DE RECUPERACAO",
           210, 255, 4.2, "TEXTO", "center", (15, 405))
    f.text("11-4400-PEL-0301   -   REVISAO 02   (MINUTA PARA APROVACAO)",
           210, 246, 3.2, "TAGS", "center", (15, 405))

    f.tabela(20, 234,
             ["DADOS PRINCIPAIS DO PAINEL", ""],
             [("TAG DO PAINEL", "11-4400-PEL-0301"),
              ("SISTEMA", "PRESSURIZACAO DAS ESCADAS - CALDEIRA REC."),
              ("AREA", "4400 - CALDEIRA DE RECUPERACAO"),
              ("ALIMENTACAO PRINCIPAL", "690 VCA - 3F + PE - 60 Hz"),
              ("ORIGEM", "CCM 11-4400-QSA-0003"),
              ("ALIMENTACAO AUXILIAR", "220 VCA - 1F+N+PE (PLT-0011-1 / DJ-84)"),
              ("CORRENTE NOMINAL", "63 A (CONFIRMAR NO ESTUDO - PEND. Q1)"),
              ("SUPORTABILIDADE Icw", "CONFORME ESTUDO DE CURTO (PEND. Q1)"),
              ("FORMA CONSTRUTIVA", "FORMA 4b (NBR IEC 61439-2)"),
              ("GRAU DE PROTECAO", "IP55 (CONFIRMAR - PEND. Q5)"),
              ("TENSAO DE COMANDO", "24 VCC - EXTRABAIXA TENSAO"),
              ("CARGAS", "4 x 5,5 kW - 660 V - VIA INVERSOR"),
              ("DIMENSOES", "A DEFINIR COM O INVOLUCRO FORMA 4b"),
              ("PINTURA", "CINZA CLARO MUNSELL N 6,5")],
             h=2.15, row_h=5.6, aligns=["left", "left"])

    f.bloco(215, 150, 405, 234, "NORMAS E DOCUMENTOS DE REFERENCIA", [
        "NBR IEC 61439-1 / -2  - CONJUNTOS DE MANOBRA E COMANDO BT",
        "NBR 5410  - INSTALACOES ELETRICAS DE BAIXA TENSAO",
        "NBR IEC 60529  - GRAUS DE PROTECAO (CODIGO IP)",
        "IEC 60204-1  - SEGURANCA DE MAQUINAS - EQUIPAMENTO ELETRICO",
        "NR-10  E  NR-12  (PORTARIAS SEPRT 915 E 916 / 2019)",
        "EN-ITE-839-REV2019  - PADRAO DE SEGURANCA VALMET - PAINEIS",
        "1000-1000-ELE-NRM-0001  - CRITERIOS DE PROJETO ELETRICO",
        "1000-1000-ELE-NRM-0008  - PAINEIS AUXILIARES",
        "11-0055-PRC-0001-NRM  - CRITERIOS DE PROJETO HVAC",
        "MF00857651  - ETC DO SISTEMA DE VENTILACAO FORCADA",
        "NBR 14880 / NT 13 CBMMS  - PRESSURIZACAO DE ESCADAS",
        "10-0000-CIV-0002-NRM  - ESPECIFICACAO DE PINTURA"], h=2.25, lh=5.4)

    f.bloco(215, 58, 405, 144, "PRINCIPAIS ALTERACOES DA REVISAO 02", [
        "1. SEGREGACAO INTERNA EM FORMA 4b .................... C1",
        "2. DISJUNTOR GERAL Ue >= 690 V, MANOPLA NA PORTA ..... C2 / C7",
        "3. IHM REMOTA POR INVERSOR NA PORTA .................. C3",
        "4. SINALIZACAO IDENTIFICADA POR TAG DA CARGA ......... C4",
        "5. SECCIONAMENTO INDIVIDUAL BLOQUEAVEL POR CARGA ..... C5",
        "6. ENTRADA DE CABOS SOMENTE PELA PARTE INFERIOR ...... C6",
        "7. FUSIVEIS ULTRARRAPIDOS aR COM Un >= 690 V ......... C8",
        "8. CORES DE SINALIZACAO CONFORME NR-10 .............. C9",
        "9. GRAU DE PROTECAO IP55 ............................ C10",
        "10. LOGICA DE DOIS ESTAGIOS 15 Pa / 50 Pa ........... C12",
        "11. FORCA CLASSE 0,6/1 kV E PE DEDICADO ............. C14 / M1",
        "12. REGUA Z, RESERVAS, ACESSORIOS E PLACAS .......... M4 / M7 / M10 / M11",
        "13. LISTA DE MATERIAIS CORRIGIDA .................... M14"], h=2.2, lh=5.0)

    f.bloco(20, 58, 205, 140, "ADVERTENCIAS DE SEGURANCA", [
        "PAINEL ALIMENTADO POR MAIS DE UMA FONTE:",
        "   690 V - CCM 11-4400-QSA-0003",
        "   220 V - PAINEL 11-4400-PLT-0011-1 / DISJUNTOR DJ-84",
        "ABRIR OS DOIS SECCIONAMENTOS E APLICAR BLOQUEIO (LOTO)",
        "ANTES DE QUALQUER INTERVENCAO.",
        "",
        "APOS DESENERGIZAR AGUARDAR 10 MINUTOS ANTES DE ABRIR OS",
        "COMPARTIMENTOS DE ACIONAMENTO (BARRAMENTO CC DOS INVERSORES).",
        "",
        "OS CIRCUITOS DE INCENDIO E DCS PERMANECEM ENERGIZADOS POR",
        "FONTE EXTERNA - FIACAO LARANJA, REGUA DE BORNES Z.",
        "",
        "SISTEMA DE SEGURANCA CONTRA INCENDIO:",
        "NAO DESLIGAR SEM AUTORIZACAO DA OPERACAO."], h=2.2, lh=4.9)
    return f


# ============================================================ 02 INDICE
def p02():
    f = Folha("02", "Indice")
    f.text("INDICE DE FOLHAS", 210, 262, 5.0, "TEXTO", "center", (15, 405))
    f.tabela(95, 248, ["FOLHA", "DESCRICAO"],
             [(n, d) for n, d in PAGINAS], h=2.6, row_h=8.0, hdr_h=8.5,
             widths=[26.0, 200.0], aligns=["center", "left"])
    f.bloco(95, 58, 321, 140, "OBSERVACOES", [
        "ESTA REVISAO 02 INCORPORA OS COMENTARIOS DO CLIENTE NA REV.01 E AS NAO",
        "CONFORMIDADES LEVANTADAS NO RELATORIO DE CONFORMIDADE DO MF00965787.",
        "",
        "OS VALORES DEPENDENTES DE INFORMACAO EXTERNA APARECEM COMO",
        "'CONFORME ESTUDO' OU 'PEND. Qx' E DEVEM SER FECHADOS ANTES DA EMISSAO",
        "PARA FABRICACAO. VER QUADRO DE PENDENCIAS NA FOLHA 03.",
        "",
        "DOCUMENTO EM CARATER DE MINUTA - REQUER VERIFICACAO E ART DE",
        "PROFISSIONAL LEGALMENTE HABILITADO ANTES DA EMISSAO."], h=2.35, lh=5.2)
    return f


# ============================================================ 03 LEGENDA
def p03():
    f = Folha("03", "Legenda e Convencoes")
    f.tabela(18, 268, ["LETRA", "IDENTIFICACAO"],
             [("Q", "DISJUNTOR"), ("F", "SECCIONADORA-FUSIVEL / FUSIVEL"),
              ("U", "INVERSOR DE FREQUENCIA"), ("M", "MOTOR"),
              ("G", "FONTE DE ALIMENTACAO"), ("H", "SINALEIRO"),
              ("S", "BOTAO"), ("K", "CONTATOR / RELE"),
              ("STG", "CONTROLADOR DE PRESSAO - STORGE"),
              ("V", "VENTILADOR DO SISTEMA"), ("VT", "VENTILACAO DO PAINEL"),
              ("TS", "TERMOSTATO"), ("X", "BORNE DE FORCA"),
              ("Y", "BORNE DE COMANDO 24 VCC"),
              ("Z", "BORNE DE FONTE EXTERNA")],
             h=2.1, row_h=5.4, widths=[16.0, 78.0], aligns=["center", "left"])

    f.tabela(215, 268, ["COR", "SINALIZACAO", "OBS."],
             [("BRANCO", "PAINEL ENERGIZADO", "H1"),
              ("VERMELHO", "CARGA LIGADA", "NR-10"),
              ("VERDE", "CARGA DESLIGADA", "NR-10"),
              ("AMARELO", "FALHA", "NR-10")],
             h=2.1, row_h=5.6, widths=[26.0, 52.0, 22.0],
             aligns=["center", "left", "center"])
    f.text("CORRIGIDO NA REV.02 CONFORME ELE-NRM-0008 (ITEM C9)",
           215, 232, 2.1, "TAGS", "left", (215, 405))

    f.tabela(215, 226, ["COR DO CABO", "CIRCUITO"],
             [("PRETO", "FORCA CA / CC"),
              ("VERMELHO", "COMANDO CA"),
              ("AZUL ESCURO", "COMANDO CC (24 V)"),
              ("LARANJA", "ALIMENTADO POR FONTE EXTERNA"),
              ("AZUL CLARO", "NEUTRO"),
              ("VERDE / AMARELO", "CONDUTOR DE PROTECAO (PE)")],
             h=2.1, row_h=5.6, widths=[36.0, 74.0], aligns=["center", "left"])
    f.text("IEC 60204-1 ITEM 13.2.4 (ITEM M3)", 215, 178, 2.1, "TAGS", "left", (215, 405))

    # simbologia
    LX0, LY0, LX1, LY1 = 18, 60, 200, 176
    f.rect(LX0, LY0, LX1 - LX0, LY1 - LY0, "MOLDURA", lw=18)
    f.line((LX0, LY1 - 8.5), (LX1, LY1 - 8.5), "MOLDURA", lw=18)
    f.text("SIMBOLOGIA", (LX0 + LX1) / 2, LY1 - 4.2, 2.6, "TEXTO", "center",
           (LX0 + 2, LX1 - 2))
    ca_s, ca_t, cb_s, cb_t = 32, 42, 122, 132
    za, zb = (ca_t, 116), (cb_t, LX1 - 3)
    ys = (155, 133, 111, 89)
    f.s_disjuntor(ca_s, ys[0], polos=1, meia=3.0)
    f.text("DISJUNTOR", ca_t, ys[0], 2.2, "TEXTO", "left", za)
    f.s_secc_fusivel(ca_s, ys[1], polos=1)
    f.text("SECCIONADORA-FUSIVEL", ca_t, ys[1], 2.2, "TEXTO", "left", za)
    f.s_inversor(ca_s, ys[2] - 6, ys[2] + 6, w=13)
    f.text("INVERSOR DE FREQUENCIA", ca_t, ys[2], 2.2, "TEXTO", "left", za)
    f.s_motor(ca_s, ys[3], r=6)
    f.text("MOTOR TRIFASICO", ca_t, ys[3], 2.2, "TEXTO", "left", za)
    f.s_sinaleiro(cb_s, ys[0])
    f.text("SINALEIRO", cb_t, ys[0], 2.2, "TEXTO", "left", zb)
    f.s_botao(cb_s, ys[1])
    f.text("BOTAO", cb_t, ys[1], 2.2, "TEXTO", "left", zb)
    f.s_bobina(cb_s, ys[2])
    f.text("BOBINA DE RELE / CONTATOR", cb_t, ys[2], 2.2, "TEXTO", "left", zb)
    f.line((cb_s, ys[3] + 5), (cb_s, ys[3] + 1.5))
    f.line((cb_s, ys[3] - 1.5), (cb_s, ys[3] - 5))
    f.s_borne(cb_s, ys[3])
    f.text("BORNE", cb_t, ys[3], 2.2, "TEXTO", "left", zb)

    f.bloco(215, 60, 405, 170, "PENDENCIAS - FECHAR ANTES DA EMISSAO PARA FABRICACAO", [
        "Q1  Icc NO PONTO DE ALIMENTACAO (SAIDA DO QSA-0003)",
        "Q2  ORIGEM 690 V / 220 V EM BARRA DE EMERGENCIA OU UPS",
        "Q3  FOLHA DE DADOS DO MOTOR (660 V / IP66 / PTC / AQUECEDOR)",
        "Q4  VENDOR LIST ARAUCO",
        "Q5  GRAU IP EXIGIDO NA CASA DE MAQUINAS",
        "Q6  LISTA DE SINAIS DEFINITIVA COM O DCS",
        "Q7  PADRAO DE CORES (SINALIZACAO E FIACAO)",
        "Q10 APRECIACAO DE RISCOS NR-12 / BOTAO DE EMERGENCIA",
        "Q11 ACEITACAO DA INTERFACE WIFI DO CONTROLADOR",
        "Q12 MODELO DO VENTILADOR (PF630 x PF560)",
        "",
        "REFERENCIA: RELATORIO DE CONFORMIDADE DO MF00965787."], h=2.2, lh=5.0)
    return f


# ============================================================ 10 BORNES
def p10():
    f = Folha("10", "Lista de Bornes")
    xr = []
    for k in range(4):
        n = k * 4
        xr += [("X%d" % (n + 1), "U%d:U" % (k + 1), "V%d:U" % (k + 1), "4 mm2 PT"),
               ("X%d" % (n + 2), "U%d:V" % (k + 1), "V%d:V" % (k + 1), "4 mm2 PT"),
               ("X%d" % (n + 3), "U%d:W" % (k + 1), "V%d:W" % (k + 1), "4 mm2 PT"),
               ("X%d" % (n + 4), "U%d:PE" % (k + 1), "V%d:PE" % (k + 1), "10 mm2 VD/AM")]
    f.text("REGUA X  -  FORCA 690 V", 15, 270, 2.6, "TEXTO", "left", (15, 130))
    f.tabela(15, 265, ["BORNE", "INTERNO", "CAMPO", "CABO"], xr,
             h=2.0, row_h=5.0, widths=[18.0, 24.0, 24.0, 30.0])

    yr = [("Y1", "G1:+", "H1:X1", "AZUL"), ("Y2", "G1:-", "H1:X2", "AZUL"),
          ("Y3", "G1:+", "S2:3", "AZUL"), ("Y4", "S2:4", "K1:A1", "AZUL"),
          ("Y5", "S1:1", "K1:A1", "AZUL"), ("Y6", "K1:A2", "G1:-", "AZUL"),
          ("Y7", "K1:13", "STG1:DI0", "AZUL"), ("Y8", "STG1:AO0", "U1:AI1+", "AZUL"),
          ("Y9", "STG1:AO0", "U2:AI1+", "AZUL"), ("Y10", "STG1:AO0", "U3:AI1+", "AZUL"),
          ("Y11", "STG1:AO0", "U4:AI1+", "AZUL"), ("Y12", "STG1:GND", "U1:REF-", "AZUL"),
          ("Y13", "U1:NA1", "H2:X1", "AZUL"), ("Y14", "U1:NA2", "H3:X1", "AZUL"),
          ("Y15", "U1:NF3", "H4:X1", "AZUL"), ("Y16", "U2:NA1", "H5:X1", "AZUL"),
          ("Y17", "U2:NA2", "H6:X1", "AZUL"), ("Y18", "U2:NF3", "H7:X1", "AZUL"),
          ("Y19", "U3:NA1", "H8:X1", "AZUL"), ("Y20", "U3:NA2", "H9:X1", "AZUL"),
          ("Y21", "U3:NF3", "H10:X1", "AZUL"), ("Y22", "U4:NA1", "H11:X1", "AZUL"),
          ("Y23", "U4:NA2", "H12:X1", "AZUL"), ("Y24", "U4:NF3", "H13:X1", "AZUL"),
          ("Y25", "K2:A1", "STG1:DI1", "AZUL"), ("Y26", "K3:A1", "K1:A2", "AZUL"),
          ("Y27..Y32", "RESERVA", "RESERVA", "-")]
    f.text("REGUA Y  -  COMANDO 24 VCC", 148, 270, 2.6, "TEXTO", "left", (148, 258))
    f.tabela(148, 265, ["BORNE", "ORIGEM", "DESTINO", "COR"], yr,
             h=2.0, row_h=4.6, widths=[22.0, 26.0, 26.0, 22.0])

    zr = [("Z1", "ALARME GERAL INCENDIO", "PAINEL INC.", "LARANJA"),
          ("Z2", "ALARME GERAL INCENDIO", "PAINEL INC.", "LARANJA"),
          ("Z3", "FUMACA CASA DE MAQ.", "PAINEL INC.", "LARANJA"),
          ("Z4", "FUMACA CASA DE MAQ.", "PAINEL INC.", "LARANJA"),
          ("Z5", "PARTIDA REMOTA HX-7910A", "DCS", "LARANJA"),
          ("Z6", "PARTIDA REMOTA HX-7910A", "DCS", "LARANJA"),
          ("Z7", "EM EXECUCAO HS-7910B", "DCS", "LARANJA"),
          ("Z8", "EM EXECUCAO HS-7910B", "DCS", "LARANJA"),
          ("Z9", "ALARME INCENDIO HS-7910C", "DCS", "LARANJA"),
          ("Z10", "ALARME INCENDIO HS-7910C", "DCS", "LARANJA"),
          ("Z11", "FALHA CONTROL. HS-7910D", "DCS", "LARANJA"),
          ("Z12", "FALHA CONTROL. HS-7910D", "DCS", "LARANJA"),
          ("Z13", "BOTAO REMOTO GUARITA", "CAMPO", "LARANJA"),
          ("Z14", "BOTAO REMOTO GUARITA", "CAMPO", "LARANJA"),
          ("Z15..Z18", "RESERVA", "-", "-")]
    f.text("REGUA Z  -  FONTES EXTERNAS", 268, 270, 2.6, "TEXTO", "left", (268, 405))
    f.tabela(268, 265, ["BORNE", "SINAL", "ORIGEM", "COR"], zr,
             h=2.0, row_h=5.0, widths=[22.0, 50.0, 26.0, 24.0],
             aligns=["center", "left", "center", "center"])
    f.bloco(268, 58, 405, 176, "NOTAS DA REGUA DE BORNES", [
        "1. REGUAS SEPARADAS POR GRUPO: FORCA (X), COMANDO 24 VCC (Y)",
        "    E FONTES EXTERNAS (Z) - EN-ITE-839 ITEM 5.5.5 / M4.",
        "2. A REGUA Z PERMANECE ENERGIZADA COM O PAINEL SECCIONADO;",
        "    INSTALAR TAMPA E PLACA DE ADVERTENCIA.",
        "3. BORNES A NO MINIMO 200 mm ACIMA DA BASE.",
        "4. RESERVA MINIMA DE 20% POR REGUA (M7).",
        "5. PE DE CADA ACIONAMENTO EM 10 mm2 (M1).",
        "6. ENTRADA DE CABOS SOMENTE PELA PARTE INFERIOR (C6)."], h=2.15, lh=4.8)
    return f


# ============================================================ 11 MATERIAIS
def p11():
    f = Folha("11", "Lista de Materiais")
    rows = [
        ("Q1", "1", "DISJUNTOR CAIXA MOLDADA 3P 63 A - Ue 690 V - Icu CONF. ESTUDO",
         "A DEFINIR - PEND. Q1/Q4", "MANOPLA NA PORTA"),
        ("-", "1", "MECANISMO ROTATIVO COM MANOPLA NA PORTA E BLOQUEIO POR CADEADO",
         "ACESSORIO DO Q1", "C2"),
        ("F1..F4", "4", "SECCIONADORA-FUSIVEL 3P 100 A COM ACIONAMENTO NA PORTA",
         "A DEFINIR - PEND. Q4", "BLOQUEAVEL - C5"),
        ("F1.1..F4.3", "12", "FUSIVEL ULTRARRAPIDO aR NH000 25 A - Un >= 690 V",
         "CONF. TABELA WEG CFW11", "C8"),
        ("U1..U4", "4", "INVERSOR DE FREQUENCIA 7,5 cv - 690 V - TROPICALIZADO",
         "CFW11 (BRCFW110007T6OYZ)", "WEG"),
        ("-", "4", "KIT IHM REMOTA PARA PORTA - UM POR INVERSOR",
         "ACESSORIO CFW11", "C3"),
        ("Q6", "1", "DISJUNTOR BIPOLAR 10 A - 220 V - COM TRAVA PARA CADEADO",
         "MDW-C10-2 + TRAVA", "C11"),
        ("Q7", "1", "DISJUNTOR BIPOLAR 10 A - 220 V - CIRCUITO RESERVA",
         "MDW-C10-2", "M7"),
        ("Q8", "1", "DISJUNTOR DIFERENCIAL RESIDUAL 2P 16 A - 30 mA",
         "TOMADA DE SERVICO", "M10"),
        ("G1", "1", "FONTE CHAVEADA 24 VCC - 2,5 A - COM PROTECAO DE SAIDA",
         "A DEFINIR - PEND. Q4", "M12"),
        ("K1", "1", "CONTATOR AUXILIAR 24 VCC - 4 CONTATOS", "CWCA0-40-00C03", "WEG"),
        ("K2, K3", "2", "RELE DE INTERFACE 1 REVERSIVEL 24 VCC - COM LED",
         "BORNE RELE", "INCENDIO"),
        ("K4..K7", "4", "RELE DE INTERFACE 1 REVERSIVEL 24 VCC - SINAIS DCS",
         "BORNE RELE", "DCS"),
        ("STG1", "1", "CONTROLADOR DE PRESSAO 0-500 Pa - IHM 4,3 pol - 2 ESTAGIOS",
         "STG01 - STORGE", "C12"),
        ("H1", "1", "SINALEIRO LED 22 mm BRANCO - PAINEL ENERGIZADO", "CEW-SM0-E26", "WEG"),
        ("H2, H5, H8, H11", "4", "SINALEIRO LED 22 mm VERMELHO - CARGA LIGADA",
         "CEW-SM1-E26", "C9"),
        ("H3, H6, H9, H12", "4", "SINALEIRO LED 22 mm VERDE - CARGA DESLIGADA",
         "CEW-SM2-E26", "C9"),
        ("H4, H7, H10, H13", "4", "SINALEIRO LED 22 mm AMARELO - FALHA",
         "CEW-SM3-E26", "C9"),
        ("S1", "1", "BOTAO PULSANTE VERMELHO - DESLIGA (1 NF)", "CSW-BF1 + BC01F", "WEG"),
        ("S2", "1", "BOTAO PULSANTE VERDE - LIGA (1 NA)", "CSW-BF2 + BC10F", "WEG"),
        ("X", "16", "BORNE DE PASSAGEM 4 mm2 - REGUA DE FORCA", "PT 4", "PHOENIX"),
        ("X-PE", "4", "BORNE TERRA 10 mm2 - UM POR ACIONAMENTO", "PT 10 PE", "M1"),
        ("Y", "32", "BORNE DE PASSAGEM 2,5 mm2 - COMANDO 24 VCC", "PT 2,5", "PHOENIX"),
        ("Z", "18", "BORNE DE PASSAGEM 2,5 mm2 - FONTES EXTERNAS", "PT 2,5", "M4"),
        ("PE", "1", "BARRA DE TERRA DE COBRE 16 mm2 - 12 POSICOES", "-", "M1"),
        ("N", "1", "BARRA DE NEUTRO 220 V - 6 POSICOES", "-", "M16"),
        ("VT1", "1", "CONJUNTO DE VENTILACAO FORCADA COM FILTRO - IP55",
         "A DEFINIR - PEND. Q5", "C10 / M6"),
        ("TS1", "1", "TERMOSTATO DE PAINEL - AJUSTE 20 A 60 C", "-", "M6"),
        ("-", "1", "TOMADA DE SERVICO 2P+T PADRAO BRASILEIRO", "-", "M10"),
        ("-", "1", "LUMINARIA LED INTERNA COM ACIONAMENTO AUTOMATICO", "-", "M10"),
        ("-", "1", "PORTA-DOCUMENTOS E PLACA DE IDENTIFICACAO NR-12", "-", "M10"),
        ("-", "1", "CONJUNTO DE PLACAS DE SEGURANCA (EN-ITE-774)", "-", "M11"),
        ("-", "1", "INVOLUCRO COM SEGREGACAO INTERNA FORMA 4b - IP55",
         "A DEFINIR - PEND. Q4/Q5", "C1 / C10"),
    ]
    f.text("LISTA DE MATERIAIS - REVISAO 02", 15, 270, 2.8, "TEXTO", "left", (15, 200))
    f.tabela(15, 265, ["TAG", "QTD", "DESCRICAO", "REFERENCIA", "OBS."], rows,
             h=1.95, row_h=4.6, widths=[30.0, 12.0, 128.0, 52.0, 32.0],
             aligns=["center", "center", "left", "left", "center"],
             layers=["TAGS", "TEXTO", "TEXTO", "TEXTO", "TAGS"])
    f.text("REFERENCIAS 'A DEFINIR' DEPENDEM DA VENDOR LIST (Q4) E DO ESTUDO DE CURTO (Q1).",
           15, 60, 2.2, "TAGS", "left", (15, 260))
    return f


# ============================================================ 04 FORCA 690 V
def p04():
    f = Folha("04", "Esquema de Forca - Entrada 690 V e Acionamentos")
    YR, YS, YT, YPE = 246.0, 242.0, 238.0, 232.0
    f.rect(20, 228, 354, 56, "COMP", dashed=True, lw=13)
    f.text("COMPARTIMENTO DE ENTRADA E BARRAMENTO - SEGREGADO (FORMA 4b)",
           205, 280.5, 2.2, "COMP", "center", (140, 372))
    for px in (39, 45, 51):
        f.line((px, 287), (px, 281.6))
    f.s_disjuntor(45, 274, polos=3, pitch=6.0, meia=2.6)
    for px, yb in ((39, YR), (45, YS), (51, YT)):
        f.line((px, 271.4), (px, yb))
    f.text("Q1", 57, 274, 3.0, "TAGS", "left", (55, 140))
    f.text("63 A - Ue 690 V", 57, 269.5, 2.1, "TEXTO", "left", (55, 140))
    for y, nome in ((YR, "R"), (YS, "S"), (YT, "T"), (YPE, "PE")):
        f.line((30, y), (372, y), lw=50)
        f.text(nome, 26, y, 2.0, "TAGS", "right", (14, 28))
    for k, xc in enumerate((110.0, 185.0, 260.0, 335.0)):
        z = (xc - 33, xc + 33)
        f.rect(xc - 32, 144, 64, 84, "COMP", dashed=True, lw=13)
        f.text("COMP. %02d" % (k + 1), xc - 30, 225.5, 1.9, "COMP", "left",
               (xc - 31, xc - 12))
        for dx, yb in ((-6, YR), (0, YS), (6, YT)):
            f.line((xc + dx, yb), (xc + dx, 224))
        f.s_secc_fusivel(xc, 212, polos=3, pitch=6.0)
        f.text("F%d" % (k + 1), xc - 18, 212, 2.8, "TAGS", "right", (xc - 31, xc - 17))
        for dx in (-6, 0, 6):
            f.line((xc + dx, 204), (xc + dx, 196))
        f.s_inversor(xc, 160, 196, w=30)
        f.text("U%d" % (k + 1), xc - 18, 178, 2.8, "TAGS", "right", (xc - 31, xc - 17))
        for dx in (-6, 0, 6):
            f.line((xc + dx, 160), (xc + dx, 153.5))
            f.s_borne(xc + dx, 152)
            f.line((xc + dx, 150.5), (xc + dx, 145))
        f.line((xc + 22, YPE), (xc + 22, 156))
        f.line((xc + 22, 156), (xc + 14, 156))
        f.line((xc + 14, 156), (xc + 14, 153.5))
        f.s_borne(xc + 14, 152)
        f.line((xc + 14, 150.5), (xc + 14, 140))
        f.line((xc + 22, 178), (xc + 15, 178))
        f.line((xc + 11, 140), (xc + 17, 140))
        f.line((xc + 12.2, 138), (xc + 15.8, 138))
        f.text("X%d-X%d" % (4 * k + 1, 4 * k + 4), xc - 18, 152, 1.9, "TAGS",
               "right", (xc - 31, xc - 17))
        f.line((xc - 6, 145), (xc - 6, 129.3))
        f.line((xc, 145), (xc, 132))
        f.line((xc + 6, 145), (xc + 6, 129.3))
        f.s_motor(xc, 124, r=8)
        f.text("V%d" % (k + 1), xc - 18, 124, 2.8, "TAGS", "right", (xc - 31, xc - 17))
        f.text("STG-PF560AC", xc, 112, 2.1, "TEXTO", "center", z)
        f.text("5,5 kW - 660 V - IP66", xc, 107.5, 2.1, "TEXTO", "center", z)
        f.text(MOTORES[k], xc, 103, 2.2, "TAGS", "center", z)
    f.bloco(15, 48, 218, 98, "NOTAS DE FORCA", [
        "ENTRADA: CCM 11-4400-QSA-0003 - 690 VCA 3F+PE - 60 Hz.",
        "CABO 3 x 35 mm2 + PE 16 mm2 - CLASSE 0,6/1 kV (C14).",
        "Q1 COM MANOPLA ROTATIVA NA PORTA E BLOQUEIO POR CADEADO (C2).",
        "F1..F4: SECCIONADORA-FUSIVEL 100 A COM MANOPLA NA PORTA,",
        "   BLOQUEAVEL INDIVIDUALMENTE (C5), FUSIVEIS aR NH000 25 A",
        "   COM Un >= 690 V CONFORME TABELA WEG DO CFW11 (C8).",
        "ENTRADA FISICA DOS CABOS SOMENTE PELA PARTE INFERIOR (C6)."],
        h=2.15, lh=4.9)
    f.bloco(225, 55, 405, 98, "COORDENACAO E ATERRAMENTO", [
        "COORDENACAO TIPO 2 (IEC 60947-4-1) CONFORME TABELA DO",
        "FABRICANTE DO INVERSOR - VALIDAR NO ESTUDO DE CURTO (Q1).",
        "PE DEDICADO DE 10 mm2 POR ACIONAMENTO - CORRENTE DE FUGA",
        "SUPERIOR A 10 mA (M1). BARRA DE TERRA GERAL DE 16 mm2.",
        "REDE 690 V ATERRADA POR ALTA RESISTENCIA: CONFIGURAR OS",
        "INVERSORES PARA REDE IT/HRG ANTES DA ENERGIZACAO (M9)."],
        h=2.15, lh=4.9)
    return f


# ============================================================ 05 AUXILIARES
def p05():
    f = Folha("05", "Esquema de Forca - Servicos Auxiliares 220 V / 24 Vcc")
    YF, YN, YPE = 252.0, 248.0, 242.0
    f.line((40, 287), (40, 279.6))
    f.line((48, 287), (48, 279.6))
    f.line((56, 287), (56, YPE))
    f.s_disjuntor(44, 272, polos=2, pitch=8.0, meia=2.6)
    f.line((40, 269.4), (40, YF))
    f.line((48, 269.4), (48, YN))
    f.text("Q6", 62, 274, 2.8, "TAGS", "left", (60, 150))
    f.text("10 A - COM TRAVA PARA CADEADO (C11)", 62, 269.5, 2.1, "TEXTO", "left", (60, 190))
    for y, nome in ((YF, "F"), (YN, "N"), (YPE, "PE")):
        f.line((30, y), (392, y), lw=40)
        f.text(nome, 26, y, 2.0, "TAGS", "right", (14, 28))

    def ramal(xc, tag):
        f.line((xc - 5, YF), (xc - 5, 233))
        f.line((xc + 5, YN), (xc + 5, 233))
        f.s_disjuntor(xc, 228, polos=2, pitch=10.0, meia=2.6)
        f.text(tag, xc - 14, 228, 2.6, "TAGS", "right", (xc - 34, xc - 13))
        f.line((xc - 5, 225.4), (xc - 5, 218))
        f.line((xc + 5, 225.4), (xc + 5, 218))

    # G1 - fonte 24 Vcc
    xc = 85.0
    ramal(xc, "Q9")
    f.s_fonte(xc, 192, 218, w=30)
    f.line((xc - 8, 192), (xc - 8, 150))
    f.line((xc + 8, 192), (xc + 8, 145))
    f.text("G1", xc - 20, 205, 2.6, "TAGS", "right", (xc - 34, xc - 19))
    f.text("FONTE 24 VCC - 2,5 A", 104, 188, 2.1, "TEXTO", "left", (104, 150))
    f.text("RESERVA DE 20% (M12)", 104, 183.4, 2.1, "TEXTO", "left", (104, 150))

    def descr(xc, linhas, y0=186.0):
        z = (xc - 34, xc + 34)
        for k, ln in enumerate([l for l in linhas if l]):
            f.text(ln, xc, y0 - k * 4.6, 2.1, "TEXTO", "center", z)

    xc = 160.0
    ramal(xc, "Q7")
    f.s_borne(xc - 5, 216.5)
    f.s_borne(xc + 5, 216.5)
    f.line((xc - 5, 215), (xc - 5, 206))
    f.line((xc + 5, 215), (xc + 5, 206))
    descr(xc, ["CIRCUITO RESERVA", "PARA MANUTENCAO (M7)"], 198)

    xc = 235.0
    ramal(xc, "Q8")
    f.rect(xc - 9, 202, 18, 12)
    f.text("2P+T", xc, 208, 2.2, "ESQUEMA", "center", check=False)
    f.line((xc - 5, 218), (xc - 5, 214))
    f.line((xc + 5, 218), (xc + 5, 214))
    descr(xc, ["TOMADA DE SERVICO 220 V", "PROTEGIDA POR DR 30 mA (M10)"], 196)

    xc = 310.0
    ramal(xc, "Q10")
    f.s_contato_na(xc - 5, 212)
    f.text("TS1", xc - 12, 212, 2.1, "TAGS", "right", (xc - 34, xc - 11))
    f.line((xc - 5, 207), (xc - 5, 200))
    f.line((xc + 5, 218), (xc + 5, 200))
    f.circle(xc, 194, 6)
    f.text("VT1", xc, 194, 2.3, "ESQUEMA", "center", check=False)
    descr(xc, ["VENTILACAO FORCADA IP55", "COMANDADA POR TERMOSTATO (M6)"], 182)

    xc = 375.0
    ramal(xc, "Q11")
    f.s_contato_na(xc - 5, 212)
    f.line((xc - 5, 207), (xc - 5, 202))
    f.line((xc + 5, 218), (xc + 5, 202))
    f.rect(xc - 9, 194, 18, 8)
    f.text("LED", xc, 198, 2.2, "ESQUEMA", "center", check=False)
    descr(xc, ["ILUMINACAO INTERNA", "CHAVE DE PORTA (M10)"], 186)

    f.line((60, 150), (392, 150), lw=40)
    f.line((60, 145), (392, 145), lw=40)
    f.text("+24 VCC", 56, 150, 2.2, "TAGS", "right", (30, 58))
    f.text("0 VCC", 56, 145, 2.2, "TAGS", "right", (30, 58))
    f.text("PARA AS FOLHAS 06, 07 E 08", 396, 155, 2.2, "TAGS", "right", (300, 404))

    f.bloco(15, 48, 205, 136, "NOTAS DOS SERVICOS AUXILIARES", [
        "ALIMENTACAO 220 VCA VINDA DO PAINEL 11-4400-PLT-0011-1,",
        "DISJUNTOR DJ-84 - CONFIRMAR ORIGEM ESSENCIAL / UPS (Q2).",
        "Q6 E O SECCIONAMENTO GERAL DOS AUXILIARES E DEVE PERMITIR",
        "BLOQUEIO POR CADEADO - O PAINEL TEM MAIS DE UMA FONTE (C11).",
        "TOMADA DE SERVICO PROTEGIDA POR DIFERENCIAL DE 30 mA (M10).",
        "VENTILACAO FORCADA COM FILTRO IP55 COMANDADA POR TERMOSTATO;",
        "DIMENSIONAR PELO MEMORIAL TERMICO A 40 C (M6).",
        "TENSAO DE COMANDO EM EXTRABAIXA TENSAO 24 VCC (NR-12)."],
        h=2.15, lh=4.9)
    f.bloco(215, 55, 405, 136, "PLACAS DE ADVERTENCIA (M11)", [
        "PORTA: RISCO DE CHOQUE ELETRICO / PESSOAL AUTORIZADO.",
        "PORTA: PAINEL ALIMENTADO POR MAIS DE UMA FONTE -",
        "   690 V (QSA-0003) E 220 V (PLT-0011-1 / DJ-84).",
        "COMPARTIMENTOS DE ACIONAMENTO: AGUARDE 10 MINUTOS APOS",
        "   DESENERGIZAR (TENSAO RESIDUAL - M2).",
        "REGUA Z: CIRCUITOS ENERGIZADOS POR FONTE EXTERNA.",
        "PLACA DE ARCO ELETRICO CONFORME NR-10 ANEXO II E NFPA 70E.",
        "PLACA DE IDENTIFICACAO NR-12 E PLACA DIAGRAMATICA."],
        h=2.15, lh=4.9)
    return f


# ============================================================ 06 COMANDO
def p06():
    f = Folha("06", "Esquema de Comando - Sinalizacao e Intertravamento")
    YP, YN = 268.0, 112.0
    f.line((22, YP), (398, YP), lw=40)
    f.line((22, YN), (398, YN), lw=40)
    f.text("+24 VCC", 24, 272, 2.2, "TAGS", "left", (14, 60))
    f.text("0 VCC", 24, 116, 2.2, "TAGS", "left", (14, 60))

    def rotulo(x, linhas, meia=26.0):
        z = (x - meia, x + meia)
        for k, ln in enumerate(linhas):
            f.text(ln, x, 102 - k * 4.3, 1.9, "TEXTO", "center", z)

    xA = 40.0
    f.line((xA, YP), (xA, 187.2))
    f.s_sinaleiro(xA, 180)
    f.line((xA, 172.8), (xA, YN))
    f.text("H1", xA - 6, 180, 2.4, "TAGS", "right", (18, xA - 5))
    rotulo(xA, ["PAINEL ENERGIZADO", "(BRANCO)"], 22)

    xB = 88.0
    f.line((xB, YP), (xB, 251))
    f.s_botao(xB, 246, nf=True)
    f.text("S1", xB - 6, 246, 2.4, "TAGS", "right", (66, xB - 5))
    f.line((xB, 241), (xB, 221))
    f.line((xB, 221), (xB + 30, 221))
    for dx, tag in ((0, "S2"), (15, "K1"), (30, "K4")):
        f.line((xB + dx, 221), (xB + dx, 215))
        if dx == 0:
            f.s_botao(xB + dx, 210)
        else:
            f.s_contato_na(xB + dx, 210)
        f.text(tag, xB + dx - 5, 210, 2.1, "TAGS", "right", (60 + dx, xB + dx - 4))
        f.line((xB + dx, 205), (xB + dx, 199))
    f.line((xB, 199), (xB + 30, 199))
    f.line((xB, 199), (xB, 180))
    f.s_contato_nf(xB, 175)
    f.text("K3", xB - 6, 175, 2.1, "TAGS", "right", (66, xB - 5))
    f.line((xB, 170), (xB, 155))
    f.s_bobina(xB, 148)
    f.text("K1", xB - 8, 148, 2.4, "TAGS", "right", (66, xB - 7))
    f.line((xB, 141), (xB, YN))
    rotulo(xB + 15, ["HABILITACAO DO SISTEMA", "S1 DESLIGA / S2 LIGA",
                     "K4 = PARTIDA REMOTA (DCS)", "K3 = FUMACA (BLOQUEIA)"], 30)

    def rung_ext(x, tag, cx, rot, bornes):
        f.line((x, YP), (x, 249.5))
        f.s_borne(x, 248)
        f.line((x, 246.5), (x, 238))
        f.rect(x - 16, 220, 32, 18, "FANTASMA", dashed=True, lw=13)
        for k, ln in enumerate(cx):
            f.text(ln, x, 232 - k * 4.4, 1.8, "FANTASMA", "center", (x - 15, x + 15))
        f.line((x, 220), (x, 213.5))
        f.s_borne(x, 212)
        f.line((x, 210.5), (x, 155))
        f.s_bobina(x, 148)
        f.text(tag, x - 8, 148, 2.4, "TAGS", "right", (x - 26, x - 7))
        f.line((x, 141), (x, YN))
        f.text(bornes[0], x + 4, 248, 1.9, "TAGS", "left", (x + 3, x + 24))
        f.text(bornes[1], x + 4, 212, 1.9, "TAGS", "left", (x + 3, x + 24))
        rotulo(x, rot)

    rung_ext(160, "K4", ["PARTIDA REMOTA", "DCS HX-7910A"],
             ["PARTIDA REMOTA", "PELO DCS"], ("Z5", "Z6"))
    rung_ext(215, "K2", ["ALARME GERAL", "PAINEL INCENDIO"],
             ["ALARME GERAL", "COMUTA PARA 50 Pa"], ("Z1", "Z2"))
    rung_ext(270, "K3", ["FUMACA NA CASA", "DE MAQUINAS"],
             ["FUMACA NA CASA DE MAQ.", "BLOQUEIA O SISTEMA"], ("Z3", "Z4"))

    def rung_dcs(x, ctag, btag, rot, bornes):
        f.line((x, YP), (x, 251))
        f.s_contato_na(x, 246)
        f.text(ctag, x - 6, 246, 2.1, "TAGS", "right", (x - 26, x - 5))
        f.line((x, 241), (x, 155))
        f.s_bobina(x, 148)
        f.text(btag, x - 8, 148, 2.4, "TAGS", "right", (x - 26, x - 7))
        f.line((x, 141), (x, 125.5))
        f.s_borne(x, 124)
        f.line((x, 122.5), (x, YN))
        f.text(bornes, x + 4, 124, 1.9, "TAGS", "left", (x + 3, x + 26))
        rotulo(x, rot)

    rung_dcs(325, "K1", "K5", ["SISTEMA EM EXECUCAO", "DCS HS-7910B"], "Z7/Z8")
    rung_dcs(380, "K2", "K6", ["ALARME DE INCENDIO", "DCS HS-7910C"], "Z9/Z10")

    f.bloco(15, 42, 218, 84, "NOTAS DE COMANDO", [
        "COMANDO EM 24 VCC - EXTRABAIXA TENSAO (NR-12 ITEM 12.4.13).",
        "DOIS ESTAGIOS DE PRESSURIZACAO (C12): EM OPERACAO NORMAL O",
        "   CONTROLADOR MANTEM 15 Pa; COM O ALARME GERAL DE INCENDIO O",
        "   CONTATO K2 COMUTA O SET POINT PARA 50 Pa (VER FOLHA 07).",
        "FUMACA NA CASA DE MAQUINAS (K3) BLOQUEIA O SISTEMA PARA NAO",
        "   INSUFLAR FUMACA NA ESCADA."], h=2.1, lh=4.7)
    return f


# ------------------------------------------------- blocos de terminais comuns
ENT = [256.0, 247.0, 238.0, 229.0, 220.0]
SAI = [211.0, 202.0, 193.0, 184.0, 175.0]
NOM_INV_E = ["24V", "COM", "DI1", "AI1+", "REF-"]
NOM_INV_S = ["C1", "NA1", "NF1", "C3", "NF3"]
Y0V, YBUS_A, YBUS_R = 156.0, 166.0, 162.0


def bloco_inversor(f, x0, x1, tag, desc):
    f.rect(x0, 170, x1 - x0, 98)
    f.text(tag, (x0 + x1) / 2, 263, 3.0, "TAGS", "center", (x0 + 2, x1 - 2))
    f.text(desc, (x0 + x1) / 2, 272, 1.9, "TEXTO", "center", (x0 - 4, x1 + 4))
    for y, nm in zip(ENT, NOM_INV_E):
        f.text(nm, x0 + 3, y, 1.9, "TEXTO", "left", (x0 + 2, x0 + 24))
        f.line((x0 - 6, y), (x0, y))
    for y, nm in zip(SAI, NOM_INV_S):
        f.text(nm, x1 - 3, y, 1.9, "TEXTO", "right", (x1 - 24, x1 - 2))
        f.line((x1, y), (x1 + 6, y))


def ligacoes_inversor(f, x0):
    f.line((x0 - 6, ENT[0]), (x0 - 12, ENT[0]))
    f.line((x0 - 12, ENT[0]), (x0 - 12, 276))
    f.line((x0 - 6, ENT[1]), (x0 - 16, ENT[1]))
    f.line((x0 - 16, ENT[1]), (x0 - 16, Y0V))
    f.line((x0 - 6, ENT[2]), (x0 - 20, ENT[2]))
    f.line((x0 - 20, ENT[2]), (x0 - 20, 276))
    f.line((x0 - 6, ENT[3]), (x0 - 24, ENT[3]))
    f.line((x0 - 24, ENT[3]), (x0 - 24, YBUS_A))
    f.line((x0 - 6, ENT[4]), (x0 - 28, ENT[4]))
    f.line((x0 - 28, ENT[4]), (x0 - 28, YBUS_R))


def ladder_lampadas(f, grupos):
    f.line((30, 146), (398, 146), lw=40)
    f.line((30, 102), (398, 102), lw=40)
    f.text("+24 VCC", 340, 150.5, 2.0, "TAGS", "left", (338, 398))
    f.text("0 VCC", 340, 106.5, 2.0, "TAGS", "left", (338, 398))
    for xb, titulo, itens in grupos:
        f.text(titulo, xb + 20, 151, 2.1, "TAGS", "center", (xb - 4, xb + 44))
        for i, (ct, lt, cor) in enumerate(itens):
            x = xb + i * 20
            f.line((x, 146), (x, 141))
            f.s_contato_na(x, 136)
            f.text(ct, x - 5, 136, 1.8, "TAGS", "right", (x - 19, x - 4))
            f.line((x, 131), (x, 125.2))
            f.s_sinaleiro(x, 118)
            f.text(lt, x - 5, 118, 1.9, "TAGS", "right", (x - 19, x - 4))
            f.text(cor, x - 5, 113, 1.6, "TEXTO", "right", (x - 19, x - 4))
            f.line((x, 110.8), (x, 102))


def rails(f):
    f.line((30, 276), (398, 276), lw=40)
    f.line((30, Y0V), (398, Y0V), lw=40)
    f.text("+24 VCC", 340, 280.5, 2.0, "TAGS", "left", (338, 398))
    f.text("0 VCC", 340, 160.5, 2.0, "TAGS", "left", (338, 398))
    f.line((18, 276), (18, 146))
    f.line((22, Y0V), (22, 102))


# ============================================================ 07 CONTROLADOR I
def p07():
    f = Folha("07", "Ligacao de Controlador I - Pressao e Acionamentos 01 e 02")
    rails(f)
    f.rect(25, 170, 65, 98)
    f.text("STG1", 57.5, 263, 3.0, "TAGS", "center", (27, 88))
    f.text("CONTROLADOR DE PRESSAO 0-500 Pa", 57.5, 272, 1.9, "TEXTO", "center", (24, 92))
    for y, nm in zip(ENT + SAI,
                     ["24V", "0V", "AI0", "AO0", "AGND", "DI0", "DI1", "NA", "COM", "485"]):
        f.text(nm, 87, y, 1.9, "TEXTO", "right", (66, 88))
        f.line((90, y), (96, y))
    f.text("SENSOR INTEGRADO", 28, ENT[2], 1.7, "TEXTO", "left", (27, 64))

    bloco_inversor(f, 150, 215, "U1", "INVERSOR CFW11 - ACIONAMENTO 01")
    bloco_inversor(f, 265, 330, "U2", "INVERSOR CFW11 - ACIONAMENTO 02")
    ligacoes_inversor(f, 150)
    ligacoes_inversor(f, 265)

    f.line((96, ENT[0]), (96, 276))
    f.line((96, ENT[1]), (100, ENT[1]))
    f.line((100, ENT[1]), (100, Y0V))
    f.line((96, ENT[3]), (96, YBUS_A))
    f.line((96, YBUS_A), (241, YBUS_A))
    f.line((96, ENT[4]), (100, ENT[4]))
    f.line((100, ENT[4]), (100, YBUS_R))
    f.line((100, YBUS_R), (237, YBUS_R))

    for x, y, tag in ((112, SAI[0], "K1"), (126, SAI[1], "K2")):
        f.line((x, 276), (x, 251))
        f.s_contato_na(x, 246)
        f.text(tag, x - 5, 246, 2.1, "TAGS", "right", (x - 18, x - 4))
        f.line((x, 241), (x, y))
        f.line((x, y), (96, y))

    ladder_lampadas(f, [
        (160, "MOTOR 01", [("U1:NA1", "H2", "VERMELHO"), ("U1:NF1", "H3", "VERDE"),
                           ("U1:NF3", "H4", "AMARELO")]),
        (285, "MOTOR 02", [("U2:NA1", "H5", "VERMELHO"), ("U2:NF1", "H6", "VERDE"),
                           ("U2:NF3", "H7", "AMARELO")])])

    f.bloco(15, 42, 218, 96, "NOTAS DO CONTROLADOR", [
        "K1 (FOLHA 06) HABILITA O SISTEMA PELA ENTRADA DI0 DO STG1.",
        "K2 (FOLHA 06) COMUTA O SET POINT PELA ENTRADA DI1: EM",
        "   OPERACAO NORMAL 15 Pa; COM ALARME GERAL DE INCENDIO 50 Pa.",
        "   DOIS ESTAGIOS EXIGIDOS NA ATN ITENS 38 E 63 (C12).",
        "SAIDA ANALOGICA 0-10 V COMUM AOS QUATRO INVERSORES.",
        "SINALIZACAO POR CARGA CONFORME NR-10 (C9) E IDENTIFICADA",
        "   COM O TAG DA CARGA (C4).",
        "CONFIRMAR LISTA DE SINAIS COM O DCS (Q6) E ACEITACAO DA",
        "   INTERFACE SEM FIO DO CONTROLADOR (Q11)."], h=2.05, lh=4.5)
    f.tabela(225, 96, ["TAG", "COR", "FUNCAO", "ORIGEM"],
             [("H2", "VERMELHO", "MOTOR 01 LIGADO", "U1:NA1"),
              ("H3", "VERDE", "MOTOR 01 DESLIGADO", "U1:NF1"),
              ("H4", "AMARELO", "MOTOR 01 EM FALHA", "U1:NF3"),
              ("H5", "VERMELHO", "MOTOR 02 LIGADO", "U2:NA1"),
              ("H6", "VERDE", "MOTOR 02 DESLIGADO", "U2:NF1"),
              ("H7", "AMARELO", "MOTOR 02 EM FALHA", "U2:NF3")],
             h=2.0, row_h=5.4, widths=[14.0, 30.0, 62.0, 28.0],
             aligns=["center", "center", "left", "center"])
    return f


# ============================================================ 08 CONTROLADOR II
def p08():
    f = Folha("08", "Ligacao de Controlador II - Acionamentos 03 e 04 e DCS")
    rails(f)
    bloco_inversor(f, 60, 125, "U3", "INVERSOR CFW11 - ACIONAMENTO 03")
    bloco_inversor(f, 175, 240, "U4", "INVERSOR CFW11 - ACIONAMENTO 04")
    ligacoes_inversor(f, 60)
    ligacoes_inversor(f, 175)
    f.line((36, YBUS_A), (151, YBUS_A))
    f.line((32, YBUS_R), (147, YBUS_R))

    xk = 300.0
    f.line((xk, 276), (xk, 251))
    f.s_contato_na(xk, 246)
    f.text("STG1", xk - 5, 246, 2.0, "TAGS", "right", (xk - 24, xk - 4))
    f.line((xk, 241), (xk, 202))
    f.s_bobina(xk, 195)
    f.text("K7", xk - 8, 195, 2.4, "TAGS", "right", (xk - 24, xk - 7))
    f.line((xk, 188), (xk, 176.5))
    f.s_borne(xk, 175)
    f.line((xk, 173.5), (xk, Y0V))
    f.text("Z11 / Z12", xk + 8, 175, 2.0, "TAGS", "left", (xk + 7, 398))
    f.text("FALHA DO CONTROLADOR", xk + 8, 246, 2.0, "TEXTO", "left", (xk + 7, 398))
    f.text("DCS 11-4412-HS-7910D", xk + 8, 241, 2.0, "TEXTO", "left", (xk + 7, 398))

    ladder_lampadas(f, [
        (48, "MOTOR 03", [("U3:NA1", "H8", "VERMELHO"), ("U3:NF1", "H9", "VERDE"),
                          ("U3:NF3", "H10", "AMARELO")]),
        (173, "MOTOR 04", [("U4:NA1", "H11", "VERMELHO"), ("U4:NF1", "H12", "VERDE"),
                           ("U4:NF3", "H13", "AMARELO")])])

    f.tabela(240, 96, ["SINAL", "TAG DCS", "BORNES"],
             [("PARTIDA REMOTA", "11-4412-HX-7910A", "Z5 / Z6"),
              ("SISTEMA EM EXECUCAO", "11-4412-HS-7910B", "Z7 / Z8"),
              ("ALARME DE INCENDIO", "11-4412-HS-7910C", "Z9 / Z10"),
              ("FALHA DO CONTROLADOR", "11-4412-HS-7910D", "Z11 / Z12")],
             h=2.0, row_h=5.4, widths=[46.0, 44.0, 26.0],
             aligns=["left", "center", "center"])
    f.bloco(15, 42, 230, 96, "NOTAS", [
        "A REFERENCIA 0-10 V E O AGND VEM DA FOLHA 07 (STG1).",
        "OS QUATRO INVERSORES RECEBEM A MESMA REFERENCIA DO",
        "STG1 (FOLHA 07) E SAO HABILITADOS PELO CONTATO K1 (FOLHA 06).",
        "SINALIZACAO POR CARGA CONFORME NR-10: VERMELHO = LIGADO,",
        "VERDE = DESLIGADO E AMARELO = FALHA (C9).",
        "TODOS OS SINALEIROS IDENTIFICADOS COM O TAG DA CARGA (C4).",
        "CONTATOS SECOS PARA O DCS NA REGUA Z; CONFIRMAR SE O CLIENTE",
        "   EXIGE VARIAVEL ANALOGICA DE PRESSAO (PEND. Q6).",
        "IHM DE CADA INVERSOR INSTALADA NA PORTA DO COMPARTIMENTO (C3)."],
        h=2.05, lh=4.5)
    return f


# ============================================================ 09 LAYOUT
def p09():
    f = Folha("09", "Layout Mecanico - Forma 4b")
    E = 15.0
    W, H, D = 1000.0 / E, 2200.0 / E, 500.0 / E
    YB, YT = 75.0, 75.0 + H

    def dim_h(x0, x1, y, txt, z):
        f.line((x0, y), (x1, y), lw=13)
        f.line((x0, y - 2), (x0, y + 2), lw=13)
        f.line((x1, y - 2), (x1, y + 2), lw=13)
        f.text(txt, (x0 + x1) / 2, y + 4, 2.2, "TEXTO", "center", z)

    FX = 32.0
    f.rect(FX, YB, W, H, lw=35)
    f.rect(FX + 1.5, YB + 1.5, W - 3, H - 3, lw=13)
    dim_h(FX, FX + W, YT + 6, "1000", (FX - 10, FX + W + 10))
    f.line((FX - 7, YB), (FX - 7, YT), lw=13)
    f.line((FX - 9, YB), (FX - 5, YB), lw=13)
    f.line((FX - 9, YT), (FX - 5, YT), lw=13)
    f.text("2200", FX - 9, (YB + YT) / 2, 2.2, "TEXTO", "right", (14, FX - 8))
    f.rect(FX + W - 12, YT - 14, 8, 6)
    f.text("Q1", FX + W - 14, YT - 11, 1.8, "TAGS", "right", (FX + 30, FX + W - 13))
    for i, (dx, dy) in enumerate(((10, 108), (30, 108), (10, 88), (30, 88))):
        f.rect(FX + dx, YB + dy, 10, 13)
        f.text("IHM %d" % (i + 1), FX + dx + 5, YB + dy + 6.5, 1.6, "TEXTO",
               "center", None, check=False)
    for c in range(4):
        for r in range(3):
            f.circle(FX + 9 + c * 14, YB + 68 - r * 7, 1.6)
    f.circle(FX + 9, YB + 40, 1.6)
    f.circle(FX + 37, YB + 40, 1.6)
    f.circle(FX + 51, YB + 40, 1.6)
    f.text("VISTA FRONTAL - PORTA", FX + W / 2, 68, 2.3, "TEXTO", "center",
           (FX - 12, FX + W + 12))

    IX = 128.0
    f.rect(IX, YB, W, H, lw=35)
    for y0, y1, col, nome in [(201.7, 221.7, None, "ENTRADA E BARRAMENTO"),
                              (161.7, 201.7, 0, "ACION. 01"), (161.7, 201.7, 1, "ACION. 02"),
                              (121.7, 161.7, 0, "ACION. 03"), (121.7, 161.7, 1, "ACION. 04"),
                              (95.0, 121.7, None, "COMANDO E CONTROLADOR"),
                              (75.0, 95.0, None, "BORNES E CANALETAS")]:
        if col is None:
            f.rect(IX, y0, W, y1 - y0, "COMP", lw=18)
            f.text(nome, IX + W / 2, (y0 + y1) / 2, 1.9, "COMP", "center",
                   (IX + 2, IX + W - 2))
        else:
            f.rect(IX + col * W / 2, y0, W / 2, y1 - y0, "COMP", lw=18)
            f.text(nome, IX + col * W / 2 + W / 4, (y0 + y1) / 2, 1.9, "COMP",
                   "center", (IX + col * W / 2 + 2, IX + (col + 1) * W / 2 - 2))
    f.text("VISTA INTERNA - SEGREGACAO FORMA 4b", IX + W / 2, 68, 2.3, "TEXTO",
           "center", (IX - 22, IX + W + 22))

    LX = 232.0
    f.rect(LX, YB, D, H, lw=35)
    f.rect(LX + 6, YB + 118, 21, 16)
    f.text("VT1", LX + 16.5, YB + 126, 1.8, "TEXTO", "center", None, check=False)
    dim_h(LX, LX + D, YT + 6, "500", (LX - 10, LX + D + 10))
    f.text("VISTA LATERAL", LX + D / 2, 68, 2.3, "TEXTO", "center",
           (LX - 20, LX + D + 20))

    f.bloco(280, 150, 405, 228, "LEGENDA DA PORTA", [
        "Q1   MANOPLA DO DISJUNTOR GERAL COM BLOQUEIO",
        "IHM 1..4   INTERFACES DOS INVERSORES U1..U4",
        "COLUNA 1..4   SINALIZACAO POR MOTOR:",
        "     VERMELHO = LIGADO",
        "     VERDE = DESLIGADO",
        "     AMARELO = FALHA",
        "H1   PAINEL ENERGIZADO (BRANCO)",
        "S1   DESLIGA  /  S2   LIGA",
        "TODAS COM PLAQUETA DE TAG (C4)"], h=2.0, lh=4.6)
    f.bloco(280, 56, 405, 144, "NOTAS DO LAYOUT", [
        "ESCALA 1:15 - COTAS EM MILIMETROS.",
        "SEGREGACAO INTERNA FORMA 4b: BARRAMENTO SEPARADO",
        "DAS UNIDADES FUNCIONAIS E CADA ACIONAMENTO EM",
        "COMPARTIMENTO PROPRIO, INCLUINDO SEUS BORNES (C1).",
        "GRAU DE PROTECAO IP55 (C10).",
        "ENTRADA DE CABOS SOMENTE PELA PARTE INFERIOR (C6).",
        "MANOPLA BLOQUEAVEL POR ACIONAMENTO NA PORTA (C5).",
        "ESPELHO INTERNO SOBRE PARTES VIVAS (M5).",
        "CHAPA MINIMA 1,95 mm; BASE 2,70 mm.",
        "PINTURA CINZA CLARO MUNSELL N 6,5; PLACA DE",
        "MONTAGEM LARANJA 2,5YR 6/14 (M13)."], h=2.0, lh=4.6)
    f.bloco(15, 12, 218, 60, "PENDENCIAS DO LAYOUT", [
        "AS DIMENSOES 1000 x 2200 x 500 SAO AS DA REVISAO 01 E SERAO",
        "REVISTAS APOS A DEFINICAO DO INVOLUCRO COM SEGREGACAO 4b E",
        "DO MEMORIAL TERMICO A 40 C (Q4 / Q5 - ITENS C1, C10 E M6).",
        "PREVER RESERVA PARA UM ACIONAMENTO FUTURO E DOIS CIRCUITOS",
        "AUXILIARES CONFORME NBR 5410 TABELA 59 (M7)."], h=2.05, lh=4.6)
    return f


PAGES = {"01": p01, "02": p02, "03": p03, "04": p04, "05": p05,
         "06": p06, "07": p07, "08": p08, "09": p09,
         "10": p10, "11": p11}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    alvo = sys.argv[1:] or sorted(PAGES)
    erros = 0
    for k in alvo:
        f = PAGES[k]()
        pr = f.validate()
        if pr:
            erros += 1
            print("FOLHA %s: %d ocorrencias" % (k, len(pr)))
            for p in pr[:14]:
                print("    -", p)
        else:
            f.save(os.path.join(OUT, "PEL-0301_%s.dxf" % k))
            print("FOLHA %s: OK (%d textos, %d segmentos)"
                  % (k, len(f.tboxes), len(f.segments)))
    sys.exit(1 if erros else 0)
