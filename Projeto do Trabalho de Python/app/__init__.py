from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estacio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

from app.models.alunos import Alunos
with app.app_context():
    db.create_all()

from app.resource.estacio import Index, Criar_Aluno, Atualizar_Aluno, Deletar_Aluno, Visualizar_Aluno
api.add_resource(Index, '/')
api.add_resource(Criar_Aluno, '/create')
api.add_resource(Atualizar_Aluno, '/update')
api.add_resource(Deletar_Aluno, '/delete')
api.add_resource(Visualizar_Aluno, '/show')