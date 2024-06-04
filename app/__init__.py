from flask import Flask

app = Flask(__name__)

from app import database

database.iniciar_db()

from app import routes