from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from app.models import ImportanciaEnum
from app.models import Tarefa


class FormTarefa(FlaskForm):
    titulo_tarefa = StringField('Título da Tarefa: ', validators=[DataRequired(), Length(1, 30)])
    descricao_tarefa = StringField('Descrição da Tarefa: ', validators=[DataRequired(), Length(1, 100)])
    importancia_tarefa = SelectField('Selecione a importância: ', choices=[(e.name, e.name.capitalize()) for e in ImportanciaEnum], validators=[DataRequired()])
    data_conclusao_tarefa = DateTimeLocalField('Data de conslusão: ', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit_tarefa = SubmitField('Enviar')

class FormCriarConta(FlaskForm):
    nome_usuario = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    confirmacao_senha = PasswordField('Confirme a senha', validators=[DataRequired(), EqualTo('senha')])
    btn_submit_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    btn_submit_login = SubmitField('Login')
