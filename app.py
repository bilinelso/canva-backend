from flask import Flask, request, jsonify
from canva_bot import gerar_imagem
from flask_cors import CORS

app = Flask(__name__)

# Configuração CORS mais permissiva
CORS(app, 
     origins=["https://relatorio.stratefinance.com.br", "http://localhost:*"],
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type"],
     supports_credentials=True)

# Rota adicional para preflight requests
@app.route('/api/gerar-imagem', methods=['OPTIONS'])
def options():
    response = jsonify({'status': 'ok'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response

@app.route('/api/gerar-imagem', methods=['POST'])
def gerar():
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'Dados ausentes'}), 400

    try:
        # Determina o tipo de relatório (padrão: diario)
        tipo_relatorio = dados.get('tipo_relatorio', 'diario')
        
        url_imagem = gerar_imagem(
            dados.get('mes', ''),  # Para acumulado, será "período"
            dados.get('semana', ''),  # Ignorado no relatório acumulado
            dados.get('percentual', ''),
            dados.get('liquido', ''),
            dados.get('layout', '1'),
            tipo_relatorio=tipo_relatorio
        )
        response = jsonify({'image_url': url_imagem})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        import traceback
        traceback.print_exc()
        error_response = jsonify({'erro': str(e)})
        error_response.headers.add('Access-Control-Allow-Origin', '*')
        return error_response, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
