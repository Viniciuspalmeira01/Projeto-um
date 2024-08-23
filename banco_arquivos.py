import peewee

db = peewee.SqliteDatabase('Banco de textos')

class Texto(peewee.Model):
          titulo = peewee.CharField()
          texto = peewee.TextField()
          class Meta:
                  database = db
class Audio(peewee.Model):
        nome = peewee.CharField()
        audio = peewee.BlobField()
        class Meta:
                database = db                  