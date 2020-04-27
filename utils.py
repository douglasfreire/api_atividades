from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Douglas', idade=28)
    print(pessoa)
    pessoa.save()


def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa_filter = Pessoas.query.filter_by(nome='Ully').first()
    print("".join(['Nome: ', pessoa_filter.nome, '\nidade: ', str(pessoa_filter.idade)]))


def altera_pessoa():
    pessoa_altera = Pessoas.query.filter_by(nome='Ully').first()
    pessoa_altera.idade = 26
    pessoa_altera.save()


def exclui_pessoa():
    pessoa_exclui = Pessoas.query.filter_by(nome='Douglas').first()
    pessoa_exclui.delete()


if __name__ == '__main__':
    insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta()
