import requests

url_base = 'https://jsonplaceholder.typicode.com'

def get_exemplo():
    resultado_get = requests.get(url_base + '/posts')
    print(resultado_get.json())

def get_c_id_exemplo():
    resultado_get = requests.get(url_base + '/posts/5')
    print(resultado_get.json())

def post_exemplo():
    postagem = {'userId': 1, 'title': 'Uma nova postagem', 'body': 'Nova postagem teste'}
    resultado_post = requests.post(url_base + '/posts', postagem)
    print(resultado_post.json())

def put_exemplo():
    postagem = {'userId': 1, 'title': 'Uma nova postagem', 'body': 'Nova atualização teste'}
    resultado_put = requests.put(url_base + '/posts/1', postagem)
    print(resultado_put.json())


def delete_exemplo():
    resultado_delete = requests.delete(url_base + '/posts/1')
    print(resultado_delete.json())


if __name__ == '__main__':
    # get_exemplo()
    # get_c_id_exemplo()
    # post_exemplo()
    # put_exemplo()
    # delete_exemplo()
    pass