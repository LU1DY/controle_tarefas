from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = 'b8605e5bfad413f5b48f79f5a057bb48b9da9c96'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///ControleDeTarefas.db'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app.models import Tarefa, Usuario


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


# Rota para login, em tentativa de acesso a página com login_required sem estar logado
login_manager.login_view = 'login'

with app.app_context():
    database.create_all()

from app import routes
