from flask import Flask
from flask_restful import Resource, Api, request
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                "status": 400,
                "mensagem": "Dados não encontrado"
            }
        return response

    def put(self, nome):
        pessoa_put = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa_put.nome = dados['nome']
        if 'idade' in dados:
            pessoa_put.idade = dados['idade']

        pessoa_put.save()
        response_put = {
            'id': pessoa_put.id,
            'nome': pessoa_put.nome,
            'idade': pessoa_put.idade
        }
        return response_put

    def delete(self, nome):
        pessoa_delete = Pessoas.query.filter_by(nome=nome).first()
        pessoa_delete.delete()
        return {"status": 200, "mensagem": f"{pessoa_delete.nome} excluida com sucesso"}


class lista_pessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id": i.id, "nome": i.nome, "idade": i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome } for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'id': atividade.id,
            'pessoa':atividade.pessoa.nome,
            'nome': atividade.nome
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(lista_pessoas, '/pessoa')
api.add_resource(ListaAtividade, '/atividade')

if __name__ == '__main__':
    app.run(debug=True)
