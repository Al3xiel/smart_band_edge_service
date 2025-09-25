from peewee import SqliteDatabase

db = SqliteDatabase ('smart_band.db')

def init_db()->None:
    """Initialize the database and create tables if they do not exist."""
    db.connect()
    """TODO: Import models and create tables"""
    db.close()

