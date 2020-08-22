from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


# http://localhost:5000/

app = Flask(__name__)

data_path = os.getcwd() + os.sep + 'data'

# Configurações iniciais

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db: SQLAlchemy


class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))


class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

# db.drop_all()
# db.create_all()
# autor = Autor(nome='Marcos', 
#               email='marcolim977@gmail.com', 
#               senha='123', 
#               admin=True)

# db.session.add(autor)
# db.session.commit()


# @app.route('/postagens', methods=['GET'])
# def obter_todas_postagens():
#     return jsonify(postagens)


# @app.route('/postagens/<int:postagem_id>', methods=['GET'])
# def obter_postagem_por_id(postagem_id):
#     return jsonify(postagens[postagem_id])


# @app.route('/postagens', methods=['POST'])
# def nova_postagem():
#     postagem = request.get_json()
#     postagens.append(postagem)
#     return jsonify({'mensagem': 'recurso criado com sucesso'}),200


# @app.route('/postagens/<int:postagem_id>', methods=['PUT'])
# def atualizar_postagem(postagem_id):
#     resultado = request.get_json()
#     postagens[postagem_id].update(resultado)
#     return jsonify(postagens[postagem_id]),200


# @app.route('/postagens/<int:postagem_id>', methods=['DELETE'])
# def excluir_postagem(postagem_id):
#     postagem = postagens[postagem_id]
#     del postagem
#     return jsonify({'mensagem':'A postagem foi excluida com sucesso'})


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)    
