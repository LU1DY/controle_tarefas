import enum
from flask_login import UserMixin
from app import database


class ImportanciaEnum(enum.Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"


class Tarefa(database.Model):
    id_tarefa = database.Column(database.Integer, primary_key=True)
    titulo_tarefa = database.Column(database.String(30), nullable=False)
    descricao_tarefa = database.Column(database.String(100), nullable=False)
    importancia_tarefa = database.Column(database.Enum(ImportanciaEnum), nullable=False, default=ImportanciaEnum.MEDIA)
    data_conclusao_tarefa = database.Column(database.DateTime, nullable=False)


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome_usuario = database.Column(database.String(30), nullable=False)
    email = database.Column(database.String(120), nullable=False, unique=True)
    senha = database.Column(database.String(200), nullable=False)