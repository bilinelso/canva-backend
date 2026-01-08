from PIL import Image, ImageDraw, ImageFont
import uuid
import os
import math

def gerar_imagem(mes, semana, percentual, liquido, layout="1", tipo_relatorio="diario"):
    """
    Gera imagem do relatório
    
    Args:
        mes: Nome do mês (para diário) ou período (para acumulado)
        semana: Número da semana (apenas para relatório diário)
        percentual: Valor percentual
        liquido: Valor líquido
        layout: Template a ser usado ("1" ou "2")
        tipo_relatorio: Tipo do relatório ("diario" ou "acumulado")
    """
    # Seleciona o template baseado no layout escolhido
    templates = {
        "1": "template/MAIO.png",
        "2": "template/Design sem nome (32).png"
    }
    
    template_path = templates.get(layout, templates["1"])
    
    img = Image.open(template_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    largura_total = img.width
    
    # Carregar fontes com os tamanhos e pesos corretos
    font_mes = ImageFont.truetype("fonts/GOTHAM-BOLD.TTF", 38)
    font_semana = ImageFont.truetype("fonts/GOTHAM-LIGHT.TTF", 27)
    font_valor = ImageFont.truetype("fonts/GOTHAM-BOLD.TTF", 51)
    
    # Configuração da sombra
    # Distância: 50, Direção: -45°, Transparência: 40%
    angulo = math.radians(45)
    distancia = 5

    offset_x = int(distancia * math.cos(angulo))
    offset_y = int(distancia * math.sin(angulo))
    
    # Cor da sombra com 40% de opacidade (aproximado em RGB)
    # Misturando preto com a cor de fundo azul do template
    cor_sombra = (26, 40, 68)
    
    # Função auxiliar para centralizar e desenhar texto com sombra
    def centralizar_com_sombra(texto, fonte, y, cor):
        largura_texto = draw.textlength(texto, font=fonte)
        x = (largura_total - largura_texto) / 2
        
        # Desenhar sombra primeiro (atrás do texto)
        draw.text((x + offset_x, y + offset_y), texto, font=fonte, fill=cor_sombra)
        
        # Desenhar texto principal por cima
        draw.text((x, y), texto, font=fonte, fill=cor)
    
    # Lógica diferente para relatório diário vs acumulado
    if tipo_relatorio == "acumulado":
        # Relatório Acumulado
        centralizar_com_sombra(mes.upper(), font_mes, 335, "white")  # Período
        # Não mostra semana no relatório acumulado
    else:
        # Relatório Diário (padrão)
        centralizar_com_sombra(mes.upper(), font_mes, 335, "white")  # Mês
        centralizar_com_sombra(f"{semana}", font_semana, 372, "white")  # Semana
    
    # Valores sempre são mostrados
    centralizar_com_sombra(percentual, font_valor, 732, "#0291cf")  # Percentual
    centralizar_com_sombra(liquido, font_valor, 1064, "#7ed957")  # Líquido
    
    # Salvar imagem com nome único
    nome_arquivo = f"{uuid.uuid4()}.png"
    caminho = os.path.join("static", nome_arquivo)
    img.save(caminho)
    
    return f"https://canva-backend-rsbl.onrender.com/static/{nome_arquivo}"
