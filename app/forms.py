from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from app.models import ImportanciaEnum
from app.models import Tarefa, Usuario
import re

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

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado!')

    def validate_senha(self, senha):
        valor_senha = senha.data
        if not re.search(r'\d', valor_senha):
            raise ValidationError('A senha deve conter pelo menos um número!')
        elif not re.search(r'[a-z]', valor_senha):
            raise ValidationError('A senha deve conter pelo menos uma letra minúscula!')
        elif not re.search(r'[A-Z]', valor_senha):
            raise ValidationError('A senha deve conter pelo menos uma letra maiúscula!')
        elif not re.search(r'[!@#$%^&*(),.?":{}	<>]', valor_senha):
            raise ValidationError('A senha deve conter pelo menos um caracter especial!')



class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    btn_submit_login = SubmitField('Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError(f'Nenhuma conta associada ao e-mail: {email.data}')




