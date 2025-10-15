from flask import Flask, request, jsonify
from canva_bot import gerar_imagem
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/api/gerar-imagem', methods=['POST'])
def gerar():
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'Dados ausentes'}), 400

    try:
        url_imagem = gerar_imagem(
            dados.get('mes', ''),
            dados.get('semana', ''),
            dados.get('percentual', ''),
            dados.get('liquido', ''),
            dados.get('layout', '1')  # Adiciona o parâmetro layout com valor padrão "1"
        )
        return jsonify({'image_url': url_imagem})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
