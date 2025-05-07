from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from canva_bot import gerar_imagem_local
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/gerar-imagem", methods=["POST"])
def gerar():
    dados = request.json
    caminho = gerar_imagem_local(
        dados.get("mes", ""),
        dados.get("semana", ""),
        dados.get("percentual", ""),
        dados.get("liquido", "")
    )
    url_completa = f"https://{request.host}{caminho}"
    return jsonify({ "url": url_completa })

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(host="0.0.0.0", port=10000)
