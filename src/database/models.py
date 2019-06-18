from peewee import *

db = SqliteDatabase("complex_extract.db")


def current_db():
    return db


def initialize_db():
    db.create_tables([Torrent])


class Torrent(Model):
    pk = AutoField()
    deluge_id = CharField()
    name = CharField()
    save_path = CharField()

    class Meta:
        database = db
