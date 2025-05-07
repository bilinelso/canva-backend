from PIL import Image, ImageDraw, ImageFont
import uuid
import os

def gerar_imagem(mes, semana, percentual, liquido):
    img = Image.open("template/Design sem nome (32).png").convert("RGB")
    draw = ImageDraw.Draw(img)

    font_mes = ImageFont.truetype("fonts/OpenSans-Light.ttf", 28)
    font_semana = ImageFont.truetype("fonts/OpenSans-Medium.ttf", 38)
    font_destaque = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 51)

    draw.text((494, 328), f"{mes}", font=font_mes, fill="black")
    draw.text((413, 372), f"DIA {semana}", font=font_semana, fill="black")
    draw.text((441, 732), f"{percentual}", font=font_destaque, fill="black")
    draw.text((413, 1064), f"{liquido}", font=font_destaque, fill="black")

    nome_arquivo = f"{uuid.uuid4()}.png"
    caminho = os.path.join("static", nome_arquivo)
    img.save(caminho)

    return f"https://canva-backend-rsbl.onrender.com/static/{nome_arquivo}"
