from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = 'b8605e5bfad413f5b48f79f5a057bb48b9da9c96'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///ControleDeTarefas.db'
database = SQLAlchemy(app)

from app.models import Tarefa

with app.app_context():
    database.create_all()

from app import routes