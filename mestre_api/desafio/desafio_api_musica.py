from flask import Flask, jsonify, request

app = Flask(__name__)

cancoes = [
    {
        'cancao':'Hate by Design',
        'estilo':'Rock'
    },
    {
        'cancao':'Um outro lugar',
        'estilo':'Folk'
    },
    {
        'cancao':'Dance Monkey',
        'estilo':'Eletronic'
    }
]

@app.route('/cancoes', methods=['GET'])
def retornar_todas_cancoes():
    return jsonify(cancoes)


@app.route('/cancoes/<int:cancao_id>', methods=['GET'])
def retornar_todas_cancoes_com_id(cancao_id):
    cancao = cancoes[cancao_id]
    return jsonify(cancao)


@app.route('/cancoes', methods=['POST'])
def adicionar_nova_cancao():
    nova_cancao = request.get_json()
    cancoes.append(nova_cancao)
    return jsonify({'mensagem':'Cancao adicionada com sucesso'}),200


@app.route('/cancoes/<int:cancao_id>', methods=['PUT'])
def alterar_cancao(cancao_id):
    cancao = request.get_json()
    cancoes[cancao_id].update(cancao)
    return jsonify(cancoes[cancao_id])


@app.route('/cancoes/<int:cancao_id>', methods=['DELETE'])
def deletar_cancao(cancao_id):
    del cancoes[cancao_id]
    return jsonify({'mensagem':'Canção excluída com sucesso'})
    

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)