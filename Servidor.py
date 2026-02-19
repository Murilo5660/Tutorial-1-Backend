from flask import Flask, jsonify

app = Flask(__name__)

# 2.1 Exemplo 1: O Ponto de Partida
@app.route('/')
def home():
    return "<h1>Servidor Online! Do Murilo</h1><p>Bem-vindo ao Backend.</p>"

# 2.2 Exemplo 2: Rotas com Parâmetros
@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"Ola, {nome}! Você acessou uma rota dinamica."

# 2.3 Exemplo 3: Retornando HTML Estruturado
@app.route('/produtos')
def listar_produtos():
    itens = ['Teclado', 'Mouse', 'Monitor', 'Cadeira Gamer']
    html = "<h2>Lista de Produtos</h2><ul>"
    for i in itens:
        html += f"<li>{i}</li>"
    html += "</ul>"
    return html

# 2.4 Exemplo 4: Lógica de Processamento
@app.route('/somar/<int:v1>/<int:v2>')
def somar(v1, v2):
    res = v1 + v2
    return f"O resultado da soma e: {res}"

# 2.5 Exemplo 5: O Padrão de API (JSON)
@app.route('/api/status')
def status_api():
    dados = {
        "servidor": "HSC Core",
        "status": "Operacional",
        "temperatura_cpu": 45.8,
        "usuarios_online": 12
    }
    return jsonify(dados)

# 3 Inicialização do Servidor
if __name__ == '__main__':
    app.run(debug=True)
