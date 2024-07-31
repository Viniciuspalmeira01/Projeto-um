from database import Usuario , db , Anuncio
from peewee import *

db.connect()

db.create_tables([Usuario , Anuncio])   

lista_usuarios = Usuario.select()
for pessoa  in lista_usuarios:
          print('Usuários: ',pessoa.id , pessoa.nome , pessoa.email , pessoa.senha)
          print()
          