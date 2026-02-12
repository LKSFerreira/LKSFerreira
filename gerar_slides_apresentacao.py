import os

import pandas as pd
from bs4 import BeautifulSoup
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Cm, Pt

# --- 🎨 DESIGN SYSTEM V8 (MODERN CARD UI REFINED) ---
# Paleta de Cores
COR_VERDE_PRIMARIA = RGBColor(0, 102, 51)
COR_VERDE_ESCURO = RGBColor(0, 84, 42)
COR_TEXTO_HEADER = RGBColor(255, 255, 255)

COR_FUNDO_SLIDE = RGBColor(240, 242, 245)
COR_CARD_BG = RGBColor(255, 255, 255)
COR_BORDA_SUTIL = RGBColor(217, 222, 228)
COR_SOMBRA = RGBColor(140, 148, 158)

COR_TEXTO_CONTEUDO = RGBColor(55, 61, 68)
COR_TEXTO_SECUNDARIO = RGBColor(98, 107, 117)
COR_TITULO_DARK = RGBColor(35, 41, 48)

# Fontes
FONTE_FAMILIA = "Segoe UI"
FONTE_TITULO_CARD = "Segoe UI Semibold"
FONTE_TITULO_PRINCIPAL = "Segoe UI Semibold"

# Configurações
ARQUIVO_ENTRADA = "data.csv"
ARQUIVO_SAIDA = "Apresentacao_Modern_V8.pptx"

# Nomes das Colunas (Ajuste conforme seu CSV)
COL_ACOES = "Actions"  # Ou 'Ações Realizadas'
COL_PROXIMAS = "Activities"  # Ou 'Próximas Atividades'
COL_PROBLEMAS = "Comments"  # Ou 'Problemas e Pendências'


def limpar_html(texto):
    if pd.isna(texto) or str(texto).strip() == "":
        return " - "

    soup = BeautifulSoup(str(texto), "html.parser")
    texto_limpo = " ".join(soup.get_text(separator=" ").split())
    return texto_limpo


def carregar_dados_blindado(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"ERRO: {caminho_arquivo} não encontrado.")
        return None

    encodings = ["utf-8", "cp1252", "latin1"]
    separadores = [",", ";"]

    for enc in encodings:
        for sep in separadores:
            try:
                pd.read_csv(caminho_arquivo, encoding=enc, sep=sep, nrows=2)
                print(f"Lido com sucesso: {enc} | separador '{sep}'")
                return pd.read_csv(caminho_arquivo, encoding=enc, sep=sep)
            except Exception:
                continue

    return None


def _aplicar_texto_header(text_frame, titulo):
    text_frame.clear()
    text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    text_frame.margin_left = Cm(0.15)
    text_frame.margin_right = Cm(0.15)

    p_h = text_frame.paragraphs[0]
    p_h.text = str(titulo).upper()
    p_h.alignment = PP_ALIGN.CENTER
    p_h.space_before = Pt(0)
    p_h.space_after = Pt(0)

    p_h.font.name = FONTE_TITULO_CARD
    p_h.font.size = Pt(10.8)
    p_h.font.bold = True
    p_h.font.color.rgb = COR_TEXTO_HEADER


def _aplicar_texto_body(text_frame, conteudo):
    text_frame.clear()
    text_frame.margin_left = Cm(0.38)
    text_frame.margin_right = Cm(0.38)
    text_frame.margin_top = Cm(0.24)
    text_frame.margin_bottom = Cm(0.22)
    text_frame.vertical_anchor = MSO_ANCHOR.TOP
    text_frame.word_wrap = True

    p_b = text_frame.paragraphs[0]
    p_b.text = conteudo
    p_b.alignment = PP_ALIGN.LEFT
    p_b.space_after = Pt(0)
    p_b.space_before = Pt(0)
    p_b.line_spacing = 1.18

    p_b.font.name = FONTE_FAMILIA
    p_b.font.size = Pt(10.2)
    p_b.font.color.rgb = COR_TEXTO_CONTEUDO


def criar_card_moderno(slide, left, top, width, height, titulo, conteudo, is_html=False):
    """Cria card com header refinado, borda suave e sombra discreta."""

    # Sombra principal (suave)
    sombra = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left + Cm(0.08), top + Cm(0.08), width, height
    )
    sombra.fill.solid()
    sombra.fill.fore_color.rgb = COR_SOMBRA
    sombra.fill.transparency = 88
    sombra.line.fill.background()
    sombra.shadow.inherit = False

    # Header
    h_header = Cm(0.9)
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, h_header)
    header.fill.solid()
    header.fill.fore_color.rgb = COR_VERDE_PRIMARIA
    header.line.color.rgb = COR_VERDE_ESCURO
    header.line.width = Pt(0.5)
    _aplicar_texto_header(header.text_frame, titulo)

    # Body
    h_body = height - h_header
    body = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top + h_header, width, h_body)
    body.fill.solid()
    body.fill.fore_color.rgb = COR_CARD_BG
    body.line.color.rgb = COR_BORDA_SUTIL
    body.line.width = Pt(0.9)

    if is_html:
        conteudo = limpar_html(conteudo)

    limite_chars = 1200
    conteudo_str = str(conteudo)
    if len(conteudo_str) > limite_chars:
        conteudo_str = conteudo_str[:limite_chars] + "... (texto truncado)"

    _aplicar_texto_body(body.text_frame, conteudo_str)


def _adicionar_titulo_principal(slide, margin_x, width_total, txt_id, txt_titulo):
    shape_title = slide.shapes.add_textbox(margin_x, Cm(0.5), width_total, Cm(1.5))
    tf_title = shape_title.text_frame
    tf_title.clear()
    tf_title.margin_left = Cm(0.2)
    tf_title.margin_right = Cm(0.2)
    tf_title.vertical_anchor = MSO_ANCHOR.MIDDLE

    p_t = tf_title.paragraphs[0]
    p_t.space_before = Pt(0)
    p_t.space_after = Pt(0)

    run_id = p_t.add_run()
    run_id.text = f"ITEM {txt_id}"
    run_id.font.name = FONTE_TITULO_PRINCIPAL
    run_id.font.bold = True
    run_id.font.size = Pt(21)
    run_id.font.color.rgb = COR_VERDE_PRIMARIA

    run_sep = p_t.add_run()
    run_sep.text = "  |  "
    run_sep.font.size = Pt(20)
    run_sep.font.color.rgb = RGBColor(168, 176, 185)

    run_tit = p_t.add_run()
    run_tit.text = txt_titulo
    run_tit.font.name = "Segoe UI Light"
    run_tit.font.size = Pt(20)
    run_tit.font.color.rgb = COR_TITULO_DARK


def main():
    print("--- 🎨 GERADOR DE SLIDES V8 (MODERN UI REFINED) ---")

    df = carregar_dados_blindado(ARQUIVO_ENTRADA)
    if df is None:
        return

    for col in [COL_ACOES, COL_PROXIMAS, COL_PROBLEMAS]:
        if col not in df.columns:
            df[col] = ""
    df = df.fillna("")

    prs = Presentation()
    prs.slide_width = Cm(33.867)
    prs.slide_height = Cm(19.05)

    print(f"Processando {len(df)} itens...")

    for _, row in df.iterrows():
        slide = prs.slides.add_slide(prs.slide_layouts[6])

        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COR_FUNDO_SLIDE

        # --- GRID SYSTEM (mantido) ---
        margin_x = Cm(1.0)
        width_total = Cm(31.867)
        gap = Cm(0.5)

        txt_id = str(row.get("ID", ""))
        txt_titulo = str(row.get("Title", ""))
        _adicionar_titulo_principal(slide, margin_x, width_total, txt_id, txt_titulo)

        current_y = Cm(2.2)

        # 2. Metadados
        h_meta = Cm(2.0)
        w_meta = (width_total - (3 * gap)) / 4
        meta_dados = [
            ("TIPO", row.get("Work Item Type", "")),
            ("RESPONSÁVEL", row.get("Assigned To", "").split("<")[0].strip()),
            ("STATUS", row.get("State", "")),
            ("PRIORIDADE", str(row.get("Priority", ""))),
        ]

        pos_x = margin_x
        for titulo, valor in meta_dados:
            criar_card_moderno(slide, pos_x, current_y, w_meta, h_meta, titulo, valor)
            pos_x += w_meta + gap

        current_y += h_meta + gap

        # 3. Descrição
        h_desc = Cm(4.5)
        criar_card_moderno(
            slide,
            margin_x,
            current_y,
            width_total,
            h_desc,
            "DESCRIÇÃO DETALHADA",
            row.get("Description", ""),
            is_html=True,
        )

        current_y += h_desc + gap

        # 4. Ações e Próximas
        h_middle = Cm(5.0)
        w_half = (width_total - gap) / 2

        criar_card_moderno(
            slide,
            margin_x,
            current_y,
            w_half,
            h_middle,
            "✅ AÇÕES REALIZADAS",
            row[COL_ACOES],
        )
        criar_card_moderno(
            slide,
            margin_x + w_half + gap,
            current_y,
            w_half,
            h_middle,
            "📅 PRÓXIMAS ATIVIDADES",
            row[COL_PROXIMAS],
        )

        current_y += h_middle + gap

        # 5. Problemas
        h_total_slide = Cm(19.05)
        margin_bottom = Cm(1.0)
        h_restante = h_total_slide - current_y - margin_bottom
        if h_restante < Cm(2.0):
            h_restante = Cm(2.5)

        criar_card_moderno(
            slide,
            margin_x,
            current_y,
            width_total,
            h_restante,
            "⚠️ PONTOS DE ATENÇÃO",
            row[COL_PROBLEMAS],
        )

    try:
        prs.save(ARQUIVO_SAIDA)
        print(f"\n✨ Apresentação salva com sucesso: {ARQUIVO_SAIDA}")
    except PermissionError:
        print(
            f"\n🚫 ERRO: O arquivo '{ARQUIVO_SAIDA}' está aberto. Feche-o e tente novamente."
        )


if __name__ == "__main__":
    main()
