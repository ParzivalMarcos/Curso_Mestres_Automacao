from flask import Flask, jsonify, request


# http://localhost:5000/

app = Flask(__name__)


postagens = [
    {
        'titulo': 'Minha Historia',
        'autor': 'Marcos Marinho'
    },
    {
        'titulo': 'Python Descomplicado',
        'autor': 'Marcos Marinho'
    },
    {
        'titulo': 'Ano Sabatico',
        'autor': 'Marcos Marinho'
    }
]


@app.route('/postagens', methods=['GET'])
def obter_todas_postagens():
    return jsonify(postagens)


@app.route('/postagens/<int:postagem_id>', methods=['GET'])
def obter_postagem_por_id(postagem_id):
    return jsonify(postagens[postagem_id])


@app.route('/postagens', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify({'mensagem': 'recurso criado com sucesso'}),200


@app.route('/postagens/<int:postagem_id>', methods=['PUT'])
def atualizar_postagem(postagem_id):
    resultado = request.get_json()
    postagens[postagem_id].update(resultado)
    return jsonify(postagens[postagem_id]),200


@app.route('/postagens/<int:postagem_id>', methods=['DELETE'])
def excluir_postagem(postagem_id):
    postagem = postagens[postagem_id]
    del postagem
    return jsonify({'mensagem':'A postagem foi excluida com sucesso'})


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)