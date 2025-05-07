from PIL import Image, ImageDraw, ImageFont
import uuid
import os

def gerar_imagem(mes, semana, percentual, liquido):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminhos absolutos para template e fontes
    template_path = os.path.join(base_dir, "template", "Design sem nome (32).png")
    font_mes_path = os.path.join(base_dir, "fonts", "OpenSans-Light.ttf")
    font_semana_path = os.path.join(base_dir, "fonts", "OpenSans-SemiBold.ttf")
    font_valor_path = os.path.join(base_dir, "fonts", "OpenSans-Bold.ttf")

    img = Image.open(template_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    largura_total = img.width

    # Fontes
    font_mes = ImageFont.truetype(font_mes_path, 28)
    font_semana = ImageFont.truetype(font_semana_path, 38)
    font_valor = ImageFont.truetype(font_valor_path, 51)

    # Centralizador
    def centralizar(texto, fonte, y, cor):
        largura_texto = draw.textlength(texto, font=fonte)
        x = (largura_total - largura_texto) / 2
        draw.text((x, y), texto, font=fonte, fill=cor)

    # Texto
    centralizar(mes.upper(), font_mes, 328, "white")
    centralizar(f"DIA {semana}", font_semana, 372, "white")
    centralizar(percentual, font_valor, 732, "#9FD958")
    centralizar(liquido, font_valor, 1064, "#9FD958")

    # Salvar
    output_folder = os.path.join(base_dir, "static")
    os.makedirs(output_folder, exist_ok=True)
    nome_arquivo = f"{uuid.uuid4()}.png"
    caminho = os.path.join(output_folder, nome_arquivo)
    img.save(caminho)

    BASE_URL = "https://canva-backend.onrender.com"
return f"{BASE_URL}/static/{nome_arquivo}"

