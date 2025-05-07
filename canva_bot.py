def gerar_imagem(mes, semana, percentual, liquido):
    import os
    import uuid
    from PIL import Image, ImageDraw, ImageFont

    img = Image.open("template/Design sem nome (32).png").convert("RGB")
    draw = ImageDraw.Draw(img)
    largura_total = img.width

    # Fontes
    font_mes = ImageFont.truetype("fonts/OpenSans-Light.ttf", 28)
    font_semana = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 38)
    font_valor = ImageFont.truetype("fonts/OpenSans-Bold.ttf", 51)

    def centralizar(texto, fonte, y, cor):
        largura_texto = draw.textlength(texto, font=fonte)
        x = (largura_total - largura_texto) / 2
        draw.text((x, y), texto, font=fonte, fill=cor)

    # Inserção dos textos
    centralizar(mes.upper(), font_mes, 328, "white")
    centralizar(f"DIA {semana}", font_semana, 372, "white")
    centralizar(percentual, font_valor, 732, "#9FD958")
    centralizar(liquido, font_valor, 1064, "#9FD958")

    # Salvamento
    nome_arquivo = f"{uuid.uuid4()}.png"
    caminho = os.path.join("static", nome_arquivo)
    os.makedirs("static", exist_ok=True)
    img.save(caminho)

    BASE_URL = "https://canva-backend.onrender.com"
    return f"{BASE_URL}/static/{nome_arquivo}"
