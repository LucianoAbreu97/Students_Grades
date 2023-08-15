from argparse import ArgumentError
import json
from flask import jsonify
from flask_restful import Resource,reqparse

from app.models.alunos import Alunos

class Index(Resource):
    def get(self):
        return jsonify("Bem Vindo ao Banco de Dados de Alunos da Estacio!")
    
#Criação   
argumentos = reqparse.RequestParser()
argumentos.add_argument('cpf', type=int)
argumentos.add_argument('nome', type=str)
argumentos.add_argument('nasc', type=str)
argumentos.add_argument('sexo', type=str)
argumentos.add_argument('idade', type=int)
argumentos.add_argument('av1', type=float)
argumentos.add_argument('av2', type=float)

#Atualizar
argumentos_atualizar = reqparse.RequestParser()
argumentos_atualizar.add_argument('id', type=int)
argumentos_atualizar.add_argument('cpf', type=int)
argumentos_atualizar.add_argument('nome', type=str)
argumentos_atualizar.add_argument('nasc', type=str)
argumentos_atualizar.add_argument('sexo', type=str)
argumentos_atualizar.add_argument('idade', type=int)
argumentos_atualizar.add_argument('av1', type=float)
argumentos_atualizar.add_argument('av2', type=float)

#Deletar
argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument('id', type=int)

############################################################################

class Criar_Aluno(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            user = Alunos(**datas)
            user.salvar_aluno()
            return {"message": "Aluno criado com sucesso!"}, 201
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class Atualizar_Aluno(Resource):
    def put(self):
        try:
            datas = argumentos_atualizar.parse_args()
            atualizar = Alunos.atualizar_aluno(self, datas['id'], datas['cpf'], datas['nome'], datas['nasc'], datas['sexo'], datas['idade'], datas['av1'], datas['av2'])
            return {"message": "Dados do aluno atualizados com sucesso!"}, 200
        except Exception as e:
            return jsonify({'stats': 500, 'msg': f'{e}'}), 500
        
class Deletar_Aluno(Resource):
    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            atualizar = Alunos.deletar_aluno(self, datas['id'])
            return {'message': "Aluno deletado com sucesso!"}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class Visualizar_Aluno(Resource):
    def get(self, cpf):
        try:
            aluno = Visualizar_Aluno.query.filter_by(cpf=cpf).first()
            if aluno:
                return jsonify({
                    'id': aluno.id,
                    'cpf': aluno.cpf,
                    'nome': aluno.nome,
                    'nasc': aluno.nasc,
                    'sexo': aluno.sexo,
                    'idade': aluno.idade,
                    'av1': aluno.av1,
                    'av2': aluno.av2,
                    'media': aluno.media
                })
            else:
                return jsonify({'message': 'Aluno não encontrado.'}), 404
        except Exception as e:
            return jsonify({'stats': 500, 'msg': f'{e}'}), 500