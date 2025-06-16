from app import app, database
from flask import Flask, render_template, redirect, url_for, flash
from app.models import Tarefa, ImportanciaEnum
from app.forms import FormCriarTarefa

@app.route('/')
def home():
    todas_tarefas = Tarefa.query.all()
    return render_template('home.html', todas_tarefas=todas_tarefas)


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
        print('Erro no formulário: ')
        print(form_nova_tarefa.errors)

    return render_template('adicionar_tarefas.html', form_nova_tarefa=form_nova_tarefa)



@app.route('/remover_tarefa/<int:id_tarefa>', methods=["POST"])
def remover_tarefa(id_tarefa):
    tarefa_removida = Tarefa.query.get_or_404(id_tarefa)
    if tarefa_removida:
        database.session.delete(tarefa_removida)
        database.session.commit()
        return redirect(url_for('home'))
    else:
        return flash('Erro ao buscar tarefa!')