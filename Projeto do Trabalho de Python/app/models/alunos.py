from asyncore import read
from app import db

class Alunos(db.Model):
    __tablename__ = 'Alunos'
    __table_artgs__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    nome = db.Column(db.String(255))
    nasc = db.Column(db.String(30))
    sexo = db.Column(db.String(25))
    idade = db.Column(db.Integer)
    av1 = db.Column(db.Float)
    av2 = db.Column(db.Float)
    media = db.Column(db.Float)

    def __init__(self, cpf, nome, nasc, sexo, idade, av1, av2):
        self.cpf = cpf
        self.nome = nome
        self.nasc = nasc
        self.sexo = sexo
        self.idade = idade
        self.av1 = av1
        self.av2 = av2
        self.media = (av1 + av2) / 2

    def salvar_aluno(self):
        try:
            db.session.add(self)
            db.session.commit()
            print("Aluno salvo com sucesso!")
        except Exception as e:
            print("Erro ao salvar o aluno: ", e)
        finally:
            db.session.close()
            print("Conexão encerrada.")

    def atualizar_aluno(self, id, cpf, nome, nasc, sexo, idade, av1, av2):
        try:
            db.session.query(Alunos).filter(Alunos.id==id).update({"cpf":cpf,
                                                                   "nome": nome,
                                                                   "nasc": nasc,
                                                                   "sexo": sexo,
                                                                   "idade": idade,
                                                                   "av1": av1,
                                                                   "av2":av2})
            db.session.commit()
        except Exception as e:
            print("Erro ao atualizar o aluno, ", e)
        finally:
            db.session.close()
            print("Conexão encerrada.")

    def deletar_aluno(self,id):
        try:
            db.session.query(Alunos).filter(Alunos.id==id).delete()
            db.session.commit()
            print("O aluno foi deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar o aluno,", e)
        finally:
            db.session.close()
            print("Conexão encerrada.")

    def buscar_aluno(self, cpf):
        try:
            aluno = db.session.query(Alunos).filter(Alunos.cpf==cpf)
            return aluno
        except Exception as e:
            print("Erro ao buscar aluno por CPF:", e)
        finally:
            db.session.close()
            print("Conexão encerrada.")