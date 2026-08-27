# Relatório de Conformidade — Painel de Pressurização das Escadas da Caldeira de Recuperação

**Projeto analisado:** Esquema Elétrico "Pressurização 4 INV" — 11-4400-PEL-0301 / Valmet MF00965787 / Arauco 11-4400-ELE-0137-DIG, **rev. 1** (com comentários do cliente — arquivo "COMENTADO")
**Obra:** Arauco Projeto Sucuriú — Inocência/MS — Área 4400 (Caldeira de Recuperação) — Cliente direto: Valmet
**Data do relatório:** 27/08/2026
**Elaborado por:** Storge Engenharia (análise de conformidade documental)

---

## 1. Como ler este relatório

Cada requisito foi confrontado com o projeto MF00965787 rev.1 e classificado como:

| Status | Significado |
|---|---|
| ❌ **NÃO ATENDE** | Requisito descumprido; evidência no próprio projeto |
| ⚠️ **PARCIAL** | Conceito existe, mas incompleto ou inconsistente |
| ✅ **ATENDE** | Requisito atendido pelo projeto atual |
| ❓ **INDETERMINADO** | Não é possível concluir só com o projeto — item separado na Seção 8, com a pergunta a responder |

Os itens têm identificador (**C** = crítico, **M** = médio, **D** = documentação, **OK** = conforme, **Q** = pendente de informação) para rastrear na revisão 2 do projeto.

---

## 2. Base documental analisada

| Documento | Rev. | Conteúdo |
|---|---|---|
| MF00965787 / 11-4400-ELE-0137-DIG (COMENTADO) | 1 | **Nosso projeto** (funcional + layout mecânico), com redlines do cliente na pág. 9 |
| EN-ITE-839-REV2019 (Valmet/Roka) | 0 | Padrão de segurança NR-10/NR-12 para painéis elétricos — 66 págs. |
| MF00857651 — ETC do Sistema de Ventilação Forçada | 0 | Especificação técnica de compra do pacote (escopo, motores 660 V, vendor list, NR-10/12) |
| Planilha de Equalização (ATN rev.1, 20/05/2025) | 1 | Compromissos contratuais da Stortech ("De acordo" em ~70 itens) |
| Proposta Comercial 803/2 Stortech | 28/04/2025 | Escopo vendido (sistema 2 estágios 15→50 Pa, 4 ventiladores, quadro, STG01) |
| 1000-1000-ELE-NRM-0001 — Electrical Design Criteria | 1 | Critérios elétricos Arauco (forma 4b, 690 V, IHM por inversor, coordenação tipo 2) |
| 1000-1000-ELE-NRM-0008 — Auxiliary Panels | 2 | Norma de painéis (sinalização NR-10, pintura, reservas, acessórios, ensaios) |
| 1000-1000-ELE-NRM-0005 — LV & MV Motors | 2 | Motores 660 V, IP55W, inverter-duty, aquecedores |
| 1000-1000-ELE-NRM-0010 — Instalações Elétricas | 1 | Identificação e cores de cabos de campo |
| 1000-1000-AUT-NRM-0001 — Automação e Instrumentação | 1 | Tropicalização (conformal coating G3), interface com DCS |
| 11-0055-PRC-0001-NRM — Design Criteria HVAC | 3 | **IP55 mínimo para painéis**, chave geral bloqueável, sinais p/ DCS |
| 11-0051-INC-0001-NRM — Fire Protection | 3 | Referencia NT 13 (pressurização de escadas) CBM-MS |
| 10-0000-PRC-0001-NRM — Mill Site Conditions | 4 | 417 m, T projeto equipamento 30 (40) °C |
| 10-0000-CIV-0002-NRM — Painting | 8 | Painel cinza claro Munsell N 6,5; placa de montagem laranja 2,5YR 6/14 |
| 1000-1000-GRL-NRM-0006 + CQ-ITE-003 rev.i | — | Requisitos de databook |
| AraucoSucuriú Documents Standard + Padrão DWG Valmet | 01 | Carimbo, numeração e finalidades de documentos |
| 11-4400-MEC-0004/0027-PLT | — | Layout da torre de escadas (≈94 m, 28 pavimentos, junto à caldeira) |

**Documentos citados nas especificações e que NÃO temos em mãos:** ITE MF00835531 (instrução NR-12 do projeto, citada na ATN item 29 — provavelmente a própria EN-ITE-839 renumerada), 1000-1000-ELE-TIP-0001 (detalhes típicos de montagem), vendor list Arauco, NT 13/2019 do CBM-MS na íntegra, NBR 14880 e NBR 16401 (normas compradas). Ver Seção 8.

---

## 3. O que o projeto rev.1 contém (resumo técnico)

Painel autoportante **2200×1000×500 mm**, alimentação **690 VCA 3F+PE (35 mm²) vinda do CCM 11-4400-QSA-0003**; disjuntor geral **Q1 MDW-C125-3 (minidisjuntor 125 A curva C)**; 4 alimentadores, cada um com seccionadora-fusível **FSW100-3 + 3 fusíveis NH000 aR 25 A (FNH000-25K-A)** + minidisjuntor **MDW-C10-3**, alimentando 4 inversores **WEG CFW11 7,5 cv 690 V (BRCFW110007T6OYZ)** para os ventiladores **STG-PF560AC (5,5 kW, 6,87 A, 1750 rpm** — tags 11-4412-VNT-2941-MT1 a 2944-MT1). Circuito auxiliar **220 VCA monofásico vindo de outro painel (11-4400-PLT-0011-1, disjuntor DJ-84)** protegido por Q6 (MDW 10 A) + reserva Q7; fonte 24 VCC 1,25 A; contator K1 habilita 220 V para os controladores de pressão **STG** (com IHM touch/WiFi, saída 0–10 V para a AI1 dos inversores). Porta com 13 sinaleiros + botões liga/desliga; interface seca com DCS (partida remota HX-7910A; em execução HS-7910B; alarme incêndio HS-7910C; falha controlador HS-7910D) e com o sistema de incêndio (fumaça da casa de máquinas trava/para; alarme geral apenas repete para o DCS). Ventilação do invólucro com 2 ventiladores 120×120 + grelhas com filtro + VT1.

---

## 4. Veredito executivo

**O projeto rev.1, como está, não passa no critério do cliente.** Sua suspeita procede. São **14 não conformidades críticas** (6 delas são exatamente os comentários formais do cliente no PDF, ainda não incorporados; as demais o cliente ainda nem apontou, mas vai apontar — a mais grave é o uso de **minidisjuntores MDW, limitados a 440 V, numa rede de 690 V**), mais ~20 itens médios de projeto/documentação, e **12 pontos que dependem de informação externa** (listados em separado na Seção 8, como você pediu).

Agravante de prazo: pela ATN, a **montagem e testes são Nov/2026** e a entrega em pleno funcionamento **Fev/2027** — e a fabricação ainda não começou (e-mail da Valmet). A revisão 2 do projeto precisa sair de uma vez só, incorporando tudo deste relatório, para não queimar mais um ciclo de comentários (a Valmet dá 15 dias úteis por ciclo de análise; nossa resposta contratual é 5 dias úteis).

---

## 5. GRUPO A — Comentários formais do cliente (redlines da pág. 9) — todos pendentes

### C1 — Compartimentar o painel para Forma 4b ❌
- **Exigência:** "COMPARTIMENTAR PAINEL PARA SE ADEQUAR A CATEGORIA 4B". Origem: 1000-1000-ELE-NRM-0001 §6.5.2 — *"Constructive form ... 4b"* (NBR IEC 61439-2) para conjuntos da rede 690 V.
- **Por quê não atende:** o layout (pág. 9) é monobloco, forma 1: barramento/distribuição, 4 inversores, comando e bornes compartilham o mesmo volume, sem qualquer segregação interna.
- **Como atender:** Forma 4b = barramento segregado das unidades funcionais **e** cada unidade funcional (alimentador + inversor) em compartimento próprio, **incluindo seus terminais de saída**. Na prática: invólucro modular compartimentado (ou kits de segregação metálica/chapa com IP≥2X interno), com: compartimento de entrada/barramento; 4 compartimentos de acionamento (FSW + proteção + CFW11 de cada ventilador); compartimento de comando/controladores; réguas de bornes separadas por unidade. Isso **muda dimensões, dissipação térmica e preço do invólucro** — redesenhar o layout mecânico antes de comprar chapa. Validar com a Valmet se aceitam 4b via segregação interna no invólucro único ou se esperam colunas tipo CCM.

### C2 — Chave de manobra do disjuntor de entrada na porta, com bloqueio ❌
- **Exigência:** redline + EN-ITE-839 §5.2 (seccionadora geral com *lock out*, sistema de haste, cadeado, entre 0,6–1,9 m do piso, não pode seccionar o PE, não pode ser usada como liga/desliga de processo) + 11-0055-PRC-0001 §6 (*"a lockable main switch for the cabinet"*).
- **Por quê não atende:** Q1 é minidisjuntor interno, sem acionamento externo nem provisão de bloqueio; abrir a porta hoje expõe partes vivas com o painel energizado.
- **Como atender:** disjuntor geral em caixa moldada com **mecanismo rotativo prolongado e manopla na porta, bloqueável por até 3 cadeados**, com intertravamento de porta (porta só abre com o disjuntor aberto; *defeat* por ferramenta para manutenção autorizada). Manopla preta/cinza (acesso restrito) conforme EN-ITE-839 §5.2. Sinalizar as canaletas/trecho entre a entrada de cabos e o disjuntor geral, que permanecem energizados (EN-ITE-839, nota do §5.2).

### C3 — IHM dos inversores na porta ❌
- **Exigência:** redline + ELE-NRM-0001 §6.5.5: *"At least one HMI per frequency inverter must be provided"*, instalada na porta do compartimento.
- **Por quê não atende:** os 4 CFW11 ficam com a IHM no corpo do inversor, dentro do painel fechado.
- **Como atender:** 4 × kit IHM remota CFW11 (moldura de porta + cabo), uma por inversor, identificadas com o tag do motor correspondente. Com a compartimentação (C1), uma IHM na porta de cada compartimento de acionamento.

### C4 — Identificar todas as sinalizações pelo TAG das cargas ❌
- **Exigência:** redline + EN-ITE-839 §5.4.2 (identificação de componentes conforme projeto) + ELE-NRM-0008 §3.2.1 (plaquetas de acrílico rebitadas/parafusadas).
- **Por quê não atende:** o layout da porta usa "MOTOR 01…04"; o tag real (11-4412-VNT-2941-MT1 etc.) não aparece na porta.
- **Como atender:** plaquetas de acrílico gravadas, fixadas por rebite/parafuso (não adesivo), com o tag completo em cada sinaleiro, botão, IHM e manopla; idem para o tag do painel na porta. Atualizar o layout mecânico com a tabela de plaquetas.

### C5 — Bloqueio mecânico individual por carga, na porta ❌
- **Exigência:** redline ("TODAS AS CARGAS DEVEM TER CONDIÇÕES DE BLOQUEIO INDIVIDUAL POR MÉTODO DE BLOQUEIO MECÂNICO NA PORTA") + NR-12/EN-ITE-839 §5.2 (isolar todas as fontes com possibilidade de cadeado).
- **Por quê não atende:** as FSW100 e os disjuntores dos alimentadores são internos, sem acionamento externo nem bloqueio.
- **Como atender:** cada alimentador com dispositivo de seccionamento com **manopla externa na porta bloqueável por cadeado** (seccionadora-fusível com acionamento externo ou disjuntor com mecanismo rotativo na porta). Com a Forma 4b (C1), isso sai naturalmente: uma manopla bloqueável por compartimento. Assim cada ventilador pode ser bloqueado para manutenção sem parar os demais (essencial num sistema 3+1).

### C6 — Entrada de cabos somente por baixo ⚠️
- **Exigência:** redline. (Obs.: ELE-NRM-0008 permitiria fundo **ou** topo; o comentário do cliente restringe a fundo — prevalece.)
- **Por quê parcial:** o desenho não declara o arranjo de entrada; o teto precisa ficar cego.
- **Como atender:** nota de projeto + placas de fundo removíveis, parafusadas, com **prensa-cabos PG** (EN-ITE-839 §5.4.3) mantendo o IP do invólucro; topo sem furação e vedado.

---

## 6. GRUPO B — Não conformidades críticas ainda não redlinadas (o cliente vai apontar)

### C7 — Minidisjuntores MDW (≤440 V) aplicados em 690 V ❌ **(a mais grave do projeto)**
- **Evidência:** Q1 = MDW-C125-3 e Q2–Q5 = MDW-C10-3 nos circuitos 690 V (págs. 4 e 11).
- **Por quê não atende:** a linha MDW é minidisjuntor padrão NBR NM/IEC 60898, com tensão máxima de emprego 440 VCA e capacidade de interrupção típica 5–10 kA referida a 230/400 V. **Não existe característica declarada a 690 V** — sem poder de corte, sem curva válida, sem Ue. Viola NBR IEC 60947-2/NBR IEC 61439, ELE-NRM-0001 (coordenação tipo 2, IEC 60947-4-1) e ELE-NRM-0008 (suportabilidade mínima 15 kA).
- **Como atender:** entrada com **disjuntor em caixa moldada Ue ≥ 690 V** (ex.: linha WEG DWB/DWP com Icu declarada em 690 V) dimensionado ao Icc do ponto (ver Q1 da Seção 8); nos alimentadores, substituir os MDW por **disjuntor/disjuntor-motor com Ue ≥ 690 V** ou assumir a proteção do ramal pelos fusíveis (aR não protege cabo — ver C8), seguindo as **tabelas de coordenação WEG para CFW11 690 V** (coordenação tipo 2). Q6/Q7 (220 V) podem permanecer MDW, porém com bloqueio (ver C11).

### C8 — Fusíveis aR: tensão nominal e função de proteção ❓→❌ provável
- **Evidência:** FNH000-25K-A (pág. 11).
- **Por quê:** a linha WEG FNH…K-A padrão é **500 VCA** — insuficiente para 690 V. Além disso, fusível aR protege o semicondutor, **não** o cabo/sobrecarga do ramal: hoje quem faria isso são os MDW inválidos (C7).
- **Como atender:** especificar fusível ultrarrápido **aR com Un ≥ 690 VCA** (linha NH 690 V), corrente conforme tabela WEG do CFW11 0007 T6, e garantir a proteção de ramal por disjuntor 690 V (C7). Registrar a seletividade com o disjuntor geral no estudo de coordenação (C13).

### C9 — Cores de sinalização invertidas em relação ao padrão do cliente + inconsistência interna ❌
- **Exigência:** ELE-NRM-0008 §3.2.2/§4 (NR-10): **verde = desligado, vermelho = ligado, amarelo = painel/carga em falha**; EN-ITE-839 §5.1.2 (memorial NR-10: verde "D", vermelho "L").
- **Por quê não atende:** a legenda do projeto (pág. 3) declara verde=ligado, vermelho=desligado, amarelo=falha; a fiação real (págs. 6–8) liga FALHA nos sinaleiros vermelhos H3/H6/H9/H12 e DESLIGADO nos amarelos H4/H7/H10/H13; e o layout da porta (pág. 9) mostra uma terceira combinação. **Três documentos internos se contradizem, e nenhum segue o padrão Arauco.**
- **Como atender:** adotar por motor: **vermelho = ligado, verde = desligado, amarelo = falha**; branco = painel energizado (manter H1). Corrigir legenda, esquema de comando, lista de materiais e layout ao mesmo tempo. Botoeiras podem permanecer S2 verde=partida / S1 vermelho=parada (IEC 60204-1 tab. 2, aceito pela EN-ITE-839 §5.6). Item barato — mas confirme a convenção com a Valmet antes de gravar plaquetas (Seção 8, Q7).

### C10 — Grau de proteção do invólucro não declarado; IP55 exigido ❌
- **Exigência:** 11-0055-PRC-0001 §6: *"The electrical protection class of the control equipment and Electrical cabinets shall be at least IP55"*; EN-ITE-839 §5.4.3 (IP conforme ambiente); ELE-NRM-0008 (IP42 abrigado / IP55 intempérie).
- **Por quê não atende:** o desenho não declara IP; e o conjunto grelha+filtro 120×120 comum não sustenta IP55. A casa de máquinas fica na torre da caldeira de recuperação (ambiente industrial agressivo — AUT-NRM-0001 §3.1).
- **Como atender:** declarar IP do conjunto no desenho e usar **kit de ventilação filtrada com IP54/55 declarado** (ou trocar por trocador de calor/ar-condicionado de painel se o balanço térmico exigir — ver M6). Se a Valmet aceitar IP42 por ser sala fechada, registrar por escrito (Seção 8, Q5).

### C11 — Múltiplas fontes no painel sem seccionamento bloqueável e sem advertência ❌
- **Evidência:** além dos 690 V, entram 220 VCA de outro painel (PLT-0011-1/DJ-84), sinais 24 V do sistema de incêndio e do DCS — tudo permanece vivo com Q1 aberto.
- **Exigência:** NR-12 12.7.5/12.11.3 via EN-ITE-839 §5.2 (*isolar TODAS as fontes*, bloqueio); NR-10 10.3.1 (sinalização de advertência); EN-ITE-839 §5.8 (placas).
- **Como atender:** dispositivo de seccionamento bloqueável também para o circuito 220 V (Q6 com trava de cadeado ou seccionadora rotativa bloqueável); placa "**ATENÇÃO — PAINEL ALIMENTADO POR MAIS DE UMA FONTE**" listando as fontes e os disjuntores de origem (incluir a origem DJ-84 na plaqueta); fiação desses circuitos em **laranja** (circuitos excepcionais IEC 60204-1) com segregação/identificação própria (ver M3).

### C12 — Lógica de 2 estágios (15 → 50 Pa) não implementada ⚠️
- **Exigência contratual:** ATN itens 38 e 63 — a Valmet definiu: *"O sistema fornecido deve estar preparado para receber o sinal do sistema de prevenção e detecção de incêndio para identificar foco de incêndio e aumentar o nível de pressurização"* (15 Pa contínuo → 50 Pa em alarme), conforme a própria proposta 803/2.
- **Por quê parcial:** o alarme geral de incêndio hoje só energiza K2 e repete para o DCS; nada muda o setpoint dos controladores STG. A fumaça da casa de máquinas para o sistema (correto), mas o estágio de emergência não existe no funcional.
- **Como atender:** levar o contato do alarme geral também a uma **entrada dos STG01 para comutação de setpoint** (o STG01 tem esse recurso, "setpoint de comutação configurável" — proposta) ou implementar via entrada digital dos CFW11 (segunda referência). Documentar no esquema de comando e no memorial descritivo a filosofia: normal 15 Pa / alarme 50 Pa / fumaça da casa de máquinas = parada. Registrar também o descritivo de partida automática exigido pela NT 13/NBR 14880 (Seção 8, Q2).

### C13 — Sem estudo de curto-circuito, coordenação e seletividade ❌
- **Exigência:** ELE-NRM-0001 §6.5.2 (coordenação tipo 2 IEC 60947-4-1); ELE-NRM-0008 (15 kA mín.); NR-10 10.3.x (memorial com compatibilidade das proteções); NBR IEC 61439 (Icw do conjunto).
- **Como atender:** obter o Icc no ponto de alimentação (QSA-0003 — Seção 8, Q1), emitir memorial de curto/coordenação/seletividade (Q1 × fusíveis aR × disjuntores de ramal × CFW11), declarar Icw/Ipk do conjunto no desenho e na placa.

### C14 — Fiação de força interna sem classe de isolação declarada para rede 690 V IT/HRG ⚠️
- **Evidência:** "CABO DE FORÇA 35MM²/4MM²" sem classe; rede 690 V da planta é **aterrada por alta resistência (2–5 A)** — ELE-NRM-0001 §4.4 — logo, na primeira falta à terra as fases sãs vão a 690 V contra a terra em regime.
- **Como atender:** fiação de força interna e cabos de saída em **0,6/1 kV** (não usar fio 450/750 V nos circuitos 690 V); declarar a classe no desenho e na lista de materiais. Verificar Ui ≥ 690 V de todos os componentes de força (FSW 690 V ✅; bornes PT4 800 V ✅; substituições de C7/C8 já resolvem o resto).

---

## 7. GRUPO C — Não conformidades médias (projeto, fabricação e documentação)

| ID | Item | Exigência (fonte) | Situação / Ação |
|---|---|---|---|
| M1 | **PE reforçado dos inversores** ⚠️ | Corrente de fuga > 10 mA → PE ≥ 10 mm² Cu ou PE duplo (EN-ITE-839 §5.5.8; IEC 60204-1; IEC 61800-5-1) | PE dos CFW11/motores está em 4 mm². Elevar o PE de cada inversor ao mínimo normativo, PE geral do painel ≥ 16 mm² (barra já prevista), documentar seções no unifilar |
| M2 | **Placa de descarga capacitiva** ❌ | Tensão residual > 60 V após 5 s exige advertência com tempo de espera (EN-ITE-839 §5.5.9) | CFW11 exige ~10 min de espera. Incluir placa "Aguarde 10 minutos após desenergizar" em cada compartimento de inversor |
| M3 | **Código de cores da fiação** ⚠️ | IEC 60204-1 §13.2.4 via EN-ITE-839 §5.4.2: preto=força CA/CC, vermelho=comando CA, **azul=comando CC**, **laranja=circuitos que permanecem energizados por fonte externa**, verde/amarelo=PE, azul-claro=neutro; padrão Valmet: fases A/B/C = azul-escuro/branco/violeta | Hoje: 24 VCC em vermelho/preto (deveria ser azul/azul); laranja usada para sinais internos dos inversores (reservar para incêndio/DCS/220 V pós-seccionamento); N em azul (ok se azul-claro); PE verde (aceito pela ELE-NRM-0010 §8; verde/amarelo é o preferido). Redefinir a tabela de cores na legenda e refazer a lista de bornes. **Confirmar padrão final com a Valmet antes de cabear** (EN-ITE-839 manda consultar o cliente) |
| M4 | **Segregação e grupos de bornes** ⚠️ | Terminais separados em grupos: força, comando, comando de fontes externas; ≥ 200 mm acima da base (EN-ITE-839 §5.5.5) | Criar régua exclusiva (ex.: "Z") para os circuitos externos (incêndio, DCS, 220 V), com tampa/advertência de circuito energizado; conferir cota dos bornes no layout |
| M5 | **Proteção contra toque acidental interno** ⚠️ | ETC 3.2 ("proteções contra ponto de toque acidental"); EN-ITE-839 §5.4.4; ELE-NRM-0008 (espelho interno em policarbonato 5 mm com recorte para manoplas) | Prever espelho interno/coberturas acrílicas sobre chegada do geral, barramentos e bornes de força; item hoje ausente do desenho e da lista de materiais |
| M6 | **Balanço térmico do invólucro** ❌ | Análise de dissipação exigida (EN-ITE-839 §5.4.7); T ambiente de projeto 30 (40) °C (Site Conditions) | 4×CFW11 + fonte ≈ 700–900 W de perdas. Emitir memorial térmico para 40 °C e dimensionar a ventilação/climatização compatível com o IP (C10). As distâncias mínimas dos inversores (3/11/13 cm) já estão indicadas ✅ — recalcular após a compartimentação |
| M7 | **Espaço reserva** ❌ | NBR 5410 tab. 59 via EN-ITE-839 §5.4.1 (até 6 circuitos → 2 reservas; 7–12 → 3); ELE-NRM-0008: ≥ 20 % de circuitos reserva equipados | Hoje só Q7 (1 reserva em 220 V). Prever espaço + infraestrutura para ao menos 1 alimentador 690 V futuro e 2 circuitos auxiliares, refletindo no barramento e no layout |
| M8 | **Tropicalização dos eletrônicos** ❓ | Conformal coating / ISA S71.04 G3 (ELE-NRM-0001 §6.5.5; AUT-NRM-0001 §3.1) | Especificar CFW11 com placas envernizadas (padrão WEG atende — declarar na LM) e confirmar proteção equivalente no STG01 (produto Storge — ver Seção 8, Q3) |
| M9 | **Rede IT/HRG: configuração dos inversores** ❌ | Rede 690 V com aterramento de alta resistência (ELE-NRM-0001 §4.4) | Instrução de fabricação/comissionamento: configurar os CFW11 para rede IT (remoção do jumper/parafuso do filtro RFI-MOV conforme manual WEG), senão a primeira falta à terra da planta danifica os filtros. Registrar em nota de desenho |
| M10 | **Acessórios de painel** ❌ | ELE-NRM-0008 §4 (aplicável via ELE-NRM-0001 §3.1 "sem restrição"): tomada de serviço 2P+T padrão brasileiro, iluminação interna LED automática, porta-documentos, plaqueta de tag | Nenhum previsto. Incluir os quatro; a tomada de serviço em circuito com **DR 30 mA** (EN-ITE-839 §5.5.2, IEC 60204) |
| M11 | **Placas de segurança normalizadas** ❌ | EN-ITE-839 §5.8 (modelos EN-ITE-774: MSA A09-T1, MSA P18-T1, MT V-T, MSA A75-T1, MI E-T) + §6.4 placa de arco (NFPA 70E/NR-10 Anexo II: zona de risco 0,2 m / controlada 0,7 m; arco 457 mm; aprox. limitada 1,0 m / restrita 0,3 m) + placa NR-12 (ETC 3.5) | Montar a lista de sinalização do painel (porta, fontes, partes vivas, início/fim de circuito) e incluir no desenho + lista de compras de plaquetas |
| M12 | **Fonte 24 VCC no limite** ⚠️ | Boa prática/reserva 20 % | G1 = 1,25 A para 13 LEDs + K1 + 3 relés + 2 STG01 (touch + WiFi): margem praticamente nula. Recalcular consumo e subir para ≥ 2,5 A |
| M13 | **Pintura** ❓ | ELE-NRM-0008 §3.2.3 + Painting: painel **cinza claro Munsell N 6,5**, placa de montagem **laranja Munsell 2,5YR 6/14**, esquema conforme 10-0000-CIV-0002; chapa mínima #14 (1,95 mm), base #12 | Desenho não declara cor, esquema nem espessuras. Declarar e enviar plano de pintura para aprovação (compromisso da ATN item 23) |
| M14 | **Erros de lista de materiais** ❌ | Consistência documental (NR-10 10.3.9) | (a) G1 sem part number e "787-1702 WAGO" (que É a fonte) atribuído aos ventiladores; (b) K3 aparece no comando sem constar da LM (se for contato do DCS, renomear para borne/identificação de sinal); (c) STG01/STG02 e VT1 fora da LM; (d) contagens de bornes X (19×21 posições) e Y (27×28) divergem; (e) "CANALTERA" (typo); (f) bloco NA/NF de S1/S2 conferir versus função |
| M15 | **Bitola/nota de comando divergente** ⚠️ | IEC 60204-1 (mín. 0,2 mm² interno) — atendido; porém nota da pág. 9 diz 0,75 mm² e a lista de bornes usa 1,0/1,5 mm² | Uniformizar (recomendo 1,0 mm² mínimo geral de comando) e corrigir a nota |
| M16 | **"Barramento neutro 7 posições"** ⚠️ | Rede 690 V é 3F+PE (sem neutro distribuído) | O "neutro" existente é só do 220 V auxiliar: renomear/segregar (N-220 V) para não induzir erro de montagem; barra PE identificada "PE" (EN-ITE-839 §5.3.1) |
| M17 | **Parada de emergência** ❓ | EN-ITE-839 §5.2 nota ("comandos de emergência para corte em quadros de alta demanda"); NR-12 (apreciação de riscos define) | Não previsto. Como as cargas são remotas (ventiladores no shaft), a necessidade depende da apreciação de riscos NR-12 do conjunto — levantar com a Valmet (Seção 8, Q10). Se exigida: botão soco na porta cortando a habilitação (não pode desligar involuntariamente o sistema de emergência — discutir filosofia: pressurização é sistema de segurança contra incêndio) |
| M18 | **Q1 125 A superdimensionado** ⚠️ | Dimensionamento (NBR 5410 / 61439) | Carga total ≈ 4 × 10 A. Ao trocar o geral (C7), redimensionar (ex.: 63 A) coerente com cabo 35 mm² e coordenação — reduz custo do MCCB 690 V |
| M19 | **Proteção térmica/aquecedor dos motores** ❓ | ELE-NRM-0005 §4.10 (aquecedores em todos os motores), motores inverter-duty | O painel não prevê circuito de aquecedores nem leitura de termistor. Depende do datasheet real do motor do STG-PF560AC (Seção 8, Q3). Se houver PTC: ligar na entrada do CFW11; se houver heater 220 V: prever alimentação comandada por "motor parado" |

### D — Documentação exigida e ainda não produzida ❌

Pela EN-ITE-839 §5.1, ETC §3.1/3.3, ATN e ELE-NRM-0008 §9/Anexo I, o pacote de documentos do painel deve conter (além do esquema): **diagrama unifilar** (NR-10 10.2.3 — hoje só existe o funcional), **memorial descritivo** NR-10 10.3.9 (proteções, posição dos dispositivos verde-D/vermelho-L, identificação, advertências, princípio dos dispositivos de segurança), **memoriais de cálculo** (pressurização com margem 20 % — ATN 47; elétrico/térmico/Icc), **relatório de validação IEC 60204-1 §18** + ensaios de rotina NBR IEC 61439 (inspeção, continuidade PE, resistência de isolação, ensaio dielétrico, funcional), **ART** do projeto (CREA), **PIT** (15 dias após OC — ATN 12), **plano de pintura**, **lista de sobressalentes 2 anos** (ATN 5), **manuais O&M em português** (NR-12 12.13), **placa de identificação NR-12 + placa diagramática**, **modelo 3D STEP** (ATN 26), **databook** conforme CQ-ITE-003/GRL-NRM-0006, tramitação via **M-Files** com numeração do cliente (ATN 27). No carimbo: corrigir datas conflitantes entre a tabela interna (26/09/2025) e a do cliente (rev.0 04/12/2025, rev.1 02/03/2026) e emitir a próxima revisão com finalidade **PA (Para Aprovação)**.

---

## 8. ITENS SEPARADOS — não dá para concluir só com o nosso projeto ❓

Como combinado, estes dependem de informação sua, da Valmet ou de definição de fabricação. Respondendo, eu fecho a classificação:

| Q | O que falta saber | Por que importa | A quem pedir |
|---|---|---|---|
| Q1 | **Icc trifásico disponível no ponto de alimentação** (saída do QSA-0003) e características do alimentador | Dimensiona Icu do disjuntor geral, Icw do conjunto, placa de arco (M11) e estudo C13 | Valmet (elétrica) |
| Q2 | **O alimentador 690 V vem da barra de emergência do QSA?** E o 220 V (PLT-0011-1/DJ-84) é de circuito essencial/UPS? | Pressurização é sistema de segurança: NT 13/NBR 14880 exigem suprimento garantido; ELE-NRM-0001 §4.4 pede comando de MCC em 220 V de UPS. Se o 220 V cair, os STG param e o sistema não pressuriza | Valmet (elétrica) |
| Q3 | **Datasheet real do motor do STG-PF560AC**: 660 V? inverter-duty? IP66 (carcaça ≥ 90)? PTC? aquecedor? | Compromissos contratuais ATN 35/36 e ELE-NRM-0005; define M19 e valida o CFW11 de 7 A (motor 6,87 A = 98 % do drive — margem zero; conferir corrente real em 660 V) | Interno Storge (engenharia do ventilador) |
| Q4 | **Vendor list Arauco** | ETC exige proteções/inversores/motores da vendor list; WEG deve estar, mas Phoenix/WAGO/invólucro precisam de confirmação | Valmet |
| Q5 | **IP exigido para o painel dentro da casa de máquinas** (IP55 do critério HVAC vale para a nossa sala?) | Define C10 e a solução térmica M6 | Valmet |
| Q6 | **Lista de sinais definitiva com o DCS**: seco 24 V é aceito? precisam de pressão analógica (4–20 mA) na sala de controle? | HVAC §5 lista sinais analógicos PLC→DCS; hoje o painel só entrega binários; STG01 sai em 0–10 V (precisaria conversor) | Valmet (automação) |
| Q7 | **Confirmação do padrão de cores** (sinalização C9 e fiação M3) | Evita gravar plaqueta/cabear duas vezes; EN-ITE-839 manda consultar o cliente | Valmet |
| Q8 | **ITE MF00835531** (citada na ATN 29) — obter o arquivo e confirmar se é a EN-ITE-839 | É o documento NR-12 contratual por referência | Valmet |
| Q9 | **1000-1000-ELE-TIP-0001** (detalhes típicos de montagem elétrica) — não recebemos | Compromisso ATN 61; afeta detalhes de campo (nosso escopo inclui montagem) | Valmet |
| Q10 | **Apreciação de riscos NR-12 do sistema** existe? Categoria de segurança (ISO 13849) definida? Exigem botão de emergência? | Define M17 e a eventual necessidade de funções de segurança avaliadas | Valmet / interno |
| Q11 | **WiFi do STG01 é aceito na planta?** (política de redes/segurança industrial da Arauco) | AUT-NRM trata infraestrutura wireless como sistema da planta; recurso WiFi de fornecedor pode ser vetado — se for, prever configuração local pela IHM touch | Valmet (automação/TI) |
| Q12 | **Divergência de modelo do ventilador**: proposta/ATN = STG-PF630AC (3+1 reserva); projeto = STG-PF560AC | Precisa fechar com o memorial de cálculo (20 % de margem — ATN 47) e formalizar a mudança com a Valmet | Interno + Valmet |

---

## 9. O que já ATENDE (manter na rev. 2)

| OK | Item |
|---|---|
| OK1 | Conceito de acionamento: 4 ventiladores ≤ 185 kW com VFD no painel (ELE-NRM-0001, tabela de partidas) e fusíveis ultrarrápidos aR por inversor (proposta 803/2) — só corrigir tensão/coordenação (C7/C8) |
| OK2 | Interligação com o sistema de detecção de incêndio por bornes (ATN 38): entradas de alarme geral e fumaça previstas |
| OK3 | Parada por fumaça na casa de máquinas (laço exclusivo) — filosofia correta para não insuflar fumaça na escada |
| OK4 | Partida remota pelo DCS + sinais de estado (em execução / falha controlador / alarme incêndio / ligado-falha por motor) via relés de interface |
| OK5 | Comandos de porta em extrabaixa tensão 24 VCC (NR-12 12.4.13 / EN-ITE-839 §5.6.1) |
| OK6 | Botoeiras: verde partida / vermelho parada (IEC 60204-1 tab. 2) |
| OK7 | Distâncias de montagem dos inversores indicadas (3 cm laterais / 11 cm acima / 13 cm abaixo, conforme manual WEG) |
| OK8 | Canaletas com tampa 30×80 / 50×80 e fiação em canaleta; bornes numerados com destino (lista de bornes completa) |
| OK9 | Carimbo/formato de documento no padrão Arauco/Valmet (logos, tabelas de revisão, finalidades) — corrigir apenas as datas e a finalidade da próxima emissão |
| OK10 | Cabo de entrada 35 mm² compatível com o alimentador previsto (validar na coordenação final C13/M18) |
| OK11 | Garantia 24 meses pós-PA e demais condições comerciais já aceitas na ATN (nada a fazer no projeto, só cumprir) |

---

## 10. Plano de ação sugerido (ordem de ataque)

1. **Hoje:** não iniciar fabricação; aceitar a reunião oferecida no e-mail da Valmet e levar este relatório como pauta (resolve Q1–Q11 em uma sentada).
2. **Compras de longo prazo (disparar já, condicionais à reunião):** invólucro compartimentado Forma 4b (C1), MCCB 690 V com manopla de porta (C2/C7), 4 kits IHM remota CFW11 (C3), manoplas bloqueáveis dos alimentadores (C5), fusíveis aR 690 V (C8), kit ventilação IP54/55 (C10).
3. **Rev. 2 do projeto (uma emissão única, finalidade PA):** incorporar C1–C14 + M1–M19 + D; incluir unifilar, memorial descritivo e térmico; tabela de plaquetas e sinalização; lista de materiais corrigida.
4. **Estudos:** Icc/coordenação/seletividade (após Q1), balanço térmico, consumo 24 V.
5. **Fabricação:** com PIT aprovado; ensaios de rotina NBR IEC 61439 + relatório IEC 60204-1 §18 documentados para o databook.
6. **Documentação final:** databook CQ-ITE-003, STEP 3D, M-Files, ART.

**Prazo:** a ATN prevê montagem/testes **Nov/2026** e entrega final **Fev/2027**. Estamos em ago/2026 com fabricação parada — o caminho crítico é o invólucro Forma 4b + MCCB 690 V. Tratar a rev. 2 como urgência de 1–2 semanas.

---

## 11. Nota sobre responsabilidade contratual

Pela ATN (itens 9 e 21) e pela ETC §3.3, a aceitação ou comentário da Valmet **não exime** o fornecedor: desvios não levantados valem como "cumprimento confirmado na íntegra", e correções são exigíveis **a qualquer tempo, mesmo após instalação**. Ou seja: cada item deste relatório que não formos atender precisa ser formalizado como desvio e aceito por escrito — silêncio conta contra nós.

---

*Fontes: MF00965787 rev.1 (comentado); EN-ITE-839-REV2019 rev.0; MF00857651 rev.0; ATN rev.1 (20/05/2025); Proposta 803/2 (28/04/2025); 1000-1000-ELE-NRM-0001 r1, -0005 r2, -0008 r2, -0010 r1; 1000-1000-AUT-NRM-0001 r1; 11-0055-PRC-0001-NRM r3; 11-0051-INC-0001-NRM r3; 10-0000-PRC-0001-NRM r4; 10-0000-CIV-0002-NRM r8; 1000-1000-GRL-NRM-0006 r1; CQ-ITE-003 rev.i; AraucoSucuriú Documents Standard rev.01; 11-4400-MEC-0004/0027-PLT.*
