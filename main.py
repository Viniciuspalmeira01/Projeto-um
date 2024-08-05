from database import Usuario , db , Anuncio
from peewee import *

db.connect()
db.create_tables([Usuario , Anuncio])   

def criar_usuários():
        joão = Usuario.create(nome='João' , email = 'joao@gmail' , senha ='202602', idade = 19).save()

def resultados():
          lista_usuarios = Usuario.select()
          for pessoa  in lista_usuarios:
                    print('Usuários: ',pessoa.id , pessoa.nome , pessoa.email , pessoa.senha)
resultados()