from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import ImportanciaEnum
from app.models import Tarefa


class FormCriarTarefa(FlaskForm):
    titulo_tarefa = StringField('Título da Tarefa: ', validators=[DataRequired(), Length(1, 30)])
    descricao_tarefa = StringField('Descrição da Tarefa: ', validators=[DataRequired(), Length(1, 100)])
    importancia_tarefa = SelectField('Selecione a importância: ', choices=[(e.value, e.name.capitalize()) for e in ImportanciaEnum], validators=[DataRequired()])
    data_conclusao_tarefa = DateTimeLocalField('Data de conslusão: ', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit_tarefa = SubmitField('Enviar')

