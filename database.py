from peewee import * 

db = SqliteDatabase('Usuários.db')

class Usuario(Model):
          nome = CharField()
          email = CharField(unique = True)
          senha = CharField()
          idade = int()
          class Meta:
                  database = db
                  
class Anuncio(Model):
        usuario = ForeignKeyField(Usuario , backref='Usuários')
        titulo = CharField()
        descrição = TextField()
        valor = int()
        
        class Meta:
                database = db

