from PIL import Image, ImageDraw, ImageFont, ImageFilter
import uuid
import os

def gerar_imagem(mes, semana, percentual, liquido):
    img = Image.open("template/Design sem nome (32).png").convert("RGBA")
    
    # Criar uma camada para as sombras
    shadow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_layer)
    
    # Criar camada principal para o texto
    text_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_layer)
    
    largura_total = img.width
    
    # Carregar fontes com os tamanhos e pesos corretos
    font_mes = ImageFont.truetype("fonts/GOTHAM-BOLD.TTF", 34)
    font_semana = ImageFont.truetype("fonts/GOTHAM-LIGHT.TTF", 27)
    font_valor = ImageFont.truetype("fonts/GOTHAM-BOLD.TTF", 51)
    
    # Configuração da sombra
    # Distância: 50, Direção: -45°, Desfoque: 0, Transparência: 40%
    # -45° significa: para cima e para a direita
    import math
    angulo = math.radians(-45)
    distancia = 50
    offset_x = int(distancia * math.cos(angulo))  # ~35
    offset_y = int(distancia * math.sin(angulo))  # ~-35
    cor_sombra = (0, 0, 0, int(255 * 0.9))  # Preto com 90% de opacidade
    
    # Função auxiliar para centralizar e desenhar texto com sombra
    def centralizar_com_sombra(texto, fonte, y, cor):
        largura_texto = draw.textlength(texto, font=fonte)
        x = (largura_total - largura_texto) / 2
        
        # Desenhar sombra
        shadow_draw.text((x + offset_x, y + offset_y), texto, font=fonte, fill=cor_sombra)
        
        # Desenhar texto principal
        draw.text((x, y), texto, font=fonte, fill=cor)
    
    # Inserção dos textos com as cores especificadas
    centralizar_com_sombra(mes.upper(), font_mes, 335, "white")  # Mês: #white
    centralizar_com_sombra(f"{semana}", font_semana, 372, "white")  # Semana: #white
    centralizar_com_sombra(percentual, font_valor, 732, "#0291cf")  # Percentual: #0291cf
    centralizar_com_sombra(liquido, font_valor, 1064, "#7ed957")  # Líquido: #7ed957
    
    # Combinar as camadas: imagem base + sombra + texto
    img = img.convert("RGBA")
    img = Image.alpha_composite(img, shadow_layer)
    img = Image.alpha_composite(img, text_layer)
    
    # Converter de volta para RGB para salvar como PNG
    img = img.convert("RGB")
    
    # Salvar imagem com nome único
    nome_arquivo = f"{uuid.uuid4()}.png"
    caminho = os.path.join("static", nome_arquivo)
    img.save(caminho)
    
    return f"https://canva-backend-rsbl.onrender.com/static/{nome_arquivo}"
