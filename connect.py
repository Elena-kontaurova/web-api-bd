''' kjkjk'''
from peewee import Model, MySQLDatabase, CharField, DateTimeField, DateField


db = MySQLDatabase('mod', user='root', password='lenok',
                   host='localhost', port=3306)


class BaseModel(Model):
    ''' kjkj'''
    class Meta:
        ''' llkl'''
        database = db


class News(BaseModel):
    ''' kkj'''
    name = CharField()
    date = DateTimeField()
    text = CharField()
    img = CharField()


class Sobis(BaseModel):
    ''' kkjkj'''
    name = CharField()
    date = DateField()
    avtor = CharField()
    text = CharField()


class Sotrud(BaseModel):
    ''' jkkjkj'''
    name = CharField()
    dol = CharField()
    email = CharField()
    phone = CharField()
    date = CharField()


db.connect()
db.create_tables([News, Sobis, Sotrud], safe=True)
db.close()
