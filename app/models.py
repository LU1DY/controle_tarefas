import enum

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

