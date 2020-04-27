from models import Pessoas, Usuario

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


def insere_usuario(login, senha):
    usuario = Usuario(login=login, senha=senha)
    usuario.save()

def consulta_usuario():
    usuario = Usuario.query.all()
    print(usuario)


if __name__ == '__main__':
    insere_usuario(login='douglas', senha='123456')
    insere_usuario(login='ully', senha='123456')
    consulta_usuario()
    # consulta_usuario()
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta()
