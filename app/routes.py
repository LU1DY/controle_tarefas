from app import app, database
from flask import Flask, render_template, redirect, url_for
from app.models import Tarefa, ImportanciaEnum
from app.forms import FormCriarTarefa

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/adicionar_tarefas', methods=["POST", "GET"])
def adicionar_tarefas():
    form_nova_tarefa = FormCriarTarefa()

    if form_nova_tarefa.validate_on_submit():
        tarefa = Tarefa(
            titulo_tarefa=form_nova_tarefa.titulo_tarefa.data,
            descricao_tarefa=form_nova_tarefa.descricao_tarefa.data,
            importancia_tarefa=form_nova_tarefa.importancia_tarefa.data,
            data_conclusao_tarefa=form_nova_tarefa.data_conclusao_tarefa.data
        )
        database.session.add(tarefa)
        database.session.commit()
        print('deu certo!!!!!!!! eu acho :) :>')
        return redirect(url_for('home'))
    else:
        print('deu errado!!!!!! :( :<')

    return render_template('adicionar_tarefas.html', form_nova_tarefa=form_nova_tarefa)
