from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


# http://localhost:5000/

app = Flask(__name__)

data_path = os.getcwd() + os.sep + 'data' + os.sep + 'blog.db'

# Configurações iniciais

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{data_path}'

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

db.drop_all()
db.create_all()
autor = Autor(nome='Marcos', 
              email='marcolim977@gmail.com', 
              senha='123', 
              admin=True)

db.session.add(autor)
db.session.commit()


@app.route('/postagens', methods=['GET'])
def obter_todas_postagens():
    postagens = Postagem.query.all()
    lista_postagens = []
    for postagem in postagens:
        dados_postagens = {}
        dados_postagens['id_postagem'] = postagem.id_postagem
        dados_postagens['titulo'] = postagem.titulo
        dados_postagens['id_autor'] = postagem.id_autor
        lista_postagens.append(dados_postagens)

    return jsonify({'postagens': lista_postagens})


@app.route('/postagens/<int:postagem_id>', methods=['GET'])
def obter_postagem_por_id(postagem_id):
    postagem = Postagem.query_filter_by(postagem_id).first()

    if not postagem():
        return jsonify({'mensagem': 'Postagem não encontrada'})

    dados_postagem = {}
    dados_postagem.id_postagem = postagem.id_postagem
    dados_postagem.titulo = postagem.titulo
    dados_postagem.id_autor = postagem.id_autor

    return jsonify({'autor': dados_postagem})


@app.route('/postagens', methods=['POST'])
def nova_postagem():
    pass

@app.route('/postagens/<int:postagem_id>', methods=['PUT'])
def atualizar_postagem(postagem_id):
    pass 


@app.route('/postagens/<int:postagem_id>', methods=['DELETE']   )
def excluir_postagem(postagem_id):
    pass


@app.route('/autores', methods=['GET'])
def obter_todos_autores():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        dados_autores = {}
        dados_autores['id_autor'] = autor.id_autor
        dados_autores['id_autor'] = autor.nome
        dados_autores['id_autor'] = autor.email
        lista_de_autores.append(dados_autores)

    return jsonify({'autores': lista_de_autores})



@app.route('/autores/<int:id_autor>', methods=['GET'])
def obter_autor_por_id(id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()

    if not autor:
        return jsonify({'mensagem': 'Autor não encontrado'})
    
    dados_autor = {}
    dados_autor.id_autor = autor.id_autor
    dados_autor.nome = autor.nome
    dados_autor.email = autor.email

    return jsonify({'autor': dados_autor})

@app.route('/autores', methods=['POST'])
def novo_autor():
    dados = request.get_json()  # Extraindo todos os dados de uma requisição
    novo_usuario = Autor(
                         nome=dados['nome'],
                         senha=dados['senha'],
                         email=dados['email'])
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({'mensagem': 'Novo usuario criado com suscesso'},200)
    

@app.route('/autores/<int:id_autor>', methods=['PUT'])
def atualizar_autor(id_autor):
    dados = request.get_json()

    autor = Autor.query.filter_by(id_autor=id_autor).first()

    if not autor:
        return jsonify({'mensagem': 'Autor não encontrado'})

    autor.nome = dados['nome']
    autor.email = dados['email']

    db.session.commit()

    return jsonify({'mensagem': f'Autor {autor.nome} alterado com sucesso'})

@app.route('/autores/<int:id_autor>', methods=['DELETE'])
def excluir_autor(id_autor):
    dados = request.get_json()

    autor_a_deletar = Autor.query.filter_by(id_autor=id_autor).first()

    if not autor_a_deletar:
        return jsonify({'mensagem':'Autor não encontrado'})

    db.session.delete(autor_a_deletar)
    db.session.commit()

    return jsonify({'mensagem': 'Autor excluído com sucesso'})


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)    
