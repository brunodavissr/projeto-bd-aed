from app import app
import sqlite3

DATABASE = 'produtos.db'

def conectar_db():
    return sqlite3.connect(DATABASE)

def iniciar_db():
    conexao = conectar_db()
    with app.open_resource('schema.sql', mode='r') as f:
        conexao.cursor().executescript(f.read())
    conexao.commit()
    conexao.close()