from PIL import Image, ImageDraw, ImageFont
import uuid
import os
import math

def gerar_imagem(mes, semana, percentual, liquido):
    img = Image.open("template/MAIO.png").convert("RGB")
    draw = ImageDraw.Draw(img)
    
    largura_total = img.width
    
    # Carregar fontes com os tamanhos e pesos corretos
    font_mes = ImageFont.truetype("fonts/GOTHAM-BOLD.TTF", 32)
    font_semana = ImageFont.truetype("fonts/GOTHAM-LIGHT.TTF", 38)
    font_valor = ImageFont.truetype("fonts/GOTHAM-BOLD.TTF", 51)
    
    # Configuração da sombra
    # Distância: 50, Direção: -45°, Transparência: 40%
    angulo = math.radians(-45)
    distancia = 7
    offset_x = int(distancia * math.cos(angulo))  # ~35
    offset_y = int(distancia * math.sin(angulo))  # ~-35
    
    # Cor da sombra com 40% de opacidade (aproximado em RGB)
    # Misturando preto com a cor de fundo azul do template
    cor_sombra = (26, 40, 68)  # Tom escuro que simula sombra sobre azul
    
    # Função auxiliar para centralizar e desenhar texto com sombra
    def centralizar_com_sombra(texto, fonte, y, cor):
        largura_texto = draw.textlength(texto, font=fonte)
        x = (largura_total - largura_texto) / 2
        
        # Desenhar sombra primeiro (atrás do texto)
        draw.text((x + offset_x, y + offset_y), texto, font=fonte, fill=cor_sombra)
        
        # Desenhar texto principal por cima
        draw.text((x, y), texto, font=fonte, fill=cor)
    
    # Inserção dos textos com as cores especificadas
    centralizar_com_sombra(mes.upper(), font_mes, 335, "white")  # Mês: #white
    centralizar_com_sombra(f"{semana}", font_semana, 372, "white")  # Semana: #white
    centralizar_com_sombra(percentual, font_valor, 732, "#0291cf")  # Percentual: #0291cf
    centralizar_com_sombra(liquido, font_valor, 1064, "#7ed957")  # Líquido: #7ed957
    
    # Salvar imagem com nome único
    nome_arquivo = f"{uuid.uuid4()}.png"
    caminho = os.path.join("static", nome_arquivo)
    img.save(caminho)
    
    return f"https://canva-backend-rsbl.onrender.com/static/{nome_arquivo}"
