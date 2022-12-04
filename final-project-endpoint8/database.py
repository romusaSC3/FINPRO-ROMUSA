from unicodedata import category
from creds import pg_creds
from sqlalchemy import (
        create_engine, 
        insert, 
        text,
        Table, 
        Column, 
        Integer, 
        String, 
        MetaData, 
        Float, 
        ForeignKey)

engine = create_engine(
    "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        pg_creds["user"],
        pg_creds["pass"],
        pg_creds["host"],
        pg_creds["port"],
        pg_creds["db"]))

local_engine = create_engine("sqlite:///assignment3.db", #echo=True
                             future=True,)

def run_query(query: str):
    with engine.connect() as conn:
        return [dict(row) for row in conn.execute(query)]
    
# # IMPLEMENT THIS -----------------------------------------------------
def create_sqlite_db():
    local_engine.connect()

def create_table_categories():
    metadata_obj = MetaData()
    category_table = Table(
        'categories',
        metadata_obj,
        Column('ID', Integer, nullable=False, unique=True),
        Column('Category name', String, nullable=False, unique=True, primary_key=True),
    )
    metadata_obj.create_all(local_engine)
    return category_table

# IMPLEMENT THIS
def copy_categories():
    """Copy all rows in table "categories" from PostgreSQL to SQLite."""
    with local_engine.connect() as conn:
        conn.execute(insert(create_table_categories()), run_query('SELECT * FROM categories'))
        return conn.commit()