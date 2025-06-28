from app import app, database, bcrypt
from flask import render_template, redirect, url_for, flash, request
from app.models import Tarefa, Usuario
from app.forms import FormTarefa, FormCriarConta, FormLogin, FormBuscarTarefas
from flask_login import login_user, current_user, login_required, logout_user


@app.route('/')
def home():
    return render_template('home.html', current_user=current_user)


@app.route('/tarefas')
@login_required
def tarefas():
    form_buscar = FormBuscarTarefas()
    parametro_busca = request.args.get('parametro_busca')
    if not parametro_busca:
        tarefas = Tarefa.query.filter_by(usuario_id=current_user.id).all()
    else:
        tarefas = Tarefa.query.filter(
            Tarefa.usuario_id == current_user.id,
            Tarefa.titulo_tarefa.ilike(f'%{parametro_busca}%')).all()
    return render_template('suas_tarefas.html', tarefas=tarefas, current_user=current_user, form_buscar=form_buscar)




@app.route('/adicionar_tarefas', methods=["POST", "GET"])
@login_required
def adicionar_tarefas():
    form_tarefa = FormTarefa()
    if form_tarefa.validate_on_submit():
        tarefa = Tarefa(
            titulo_tarefa=form_tarefa.titulo_tarefa.data,
            descricao_tarefa=form_tarefa.descricao_tarefa.data,
            importancia_tarefa=form_tarefa.importancia_tarefa.data,
            data_conclusao_tarefa=form_tarefa.data_conclusao_tarefa.data,
            usuario_id=current_user.id
        )
        database.session.add(tarefa)
        database.session.flush()
        database.session.commit()
        flash("Tarefa com checklist criada com sucesso!")
        return redirect(url_for('home'))
    else:
        print('Erro no formulário de criar tarefa: ')
        print(form_tarefa.errors)

    return render_template('adicionar_tarefas.html', form_tarefa=form_tarefa, titulo_pagina="Criar nova tarefa")


@app.route('/remover_tarefa/<int:id_tarefa>', methods=["POST"])
@login_required
def remover_tarefa(id_tarefa):
    tarefa_removida = Tarefa.query.get_or_404(id_tarefa)
    if tarefa_removida:
        database.session.delete(tarefa_removida)
        database.session.commit()
        return redirect(url_for('home'))
    else:
        return flash('Erro ao buscar tarefa!')


@app.route('/editar_tarefa/<int:id_tarefa>', methods=["POST", "GET"])
@login_required
def editar_tarefa(id_tarefa):
    antigos_dados = Tarefa.query.get_or_404(id_tarefa)
    form_tarefa = FormTarefa(obj=antigos_dados)

    if form_tarefa.validate_on_submit():
        form_tarefa.populate_obj(antigos_dados)
        database.session.commit()

        return redirect(url_for('home'))
    else:
        print('Erro no formulário: ', form_tarefa.errors)
    return render_template('adicionar_tarefas.html', form_tarefa=form_tarefa, titulo_pagina="Editar Tarefa")


@app.route('/criarconta', methods=["POST", "GET"])
def criarconta():
    form_criar_conta = FormCriarConta()

    if form_criar_conta.validate_on_submit():
        senha_bcrypt = bcrypt.generate_password_hash(form_criar_conta.senha.data).decode('utf-8')
        usuario = Usuario(
            nome_usuario=form_criar_conta.nome_usuario.data,
            email=form_criar_conta.email.data,
            senha=senha_bcrypt
        )
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario)
        return redirect(url_for('home'))
    else:
        print('Erro no formulário de criar conta: ')
        print(form_criar_conta.errors)
    return render_template('criar_conta.html', form_criar_conta=form_criar_conta)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()

        if usuario:
            if bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
                login_user(usuario)
                par_next = request.args.get('next')
                return redirect(par_next) if par_next else redirect(url_for('home'))
            else:
                flash('Senha incorreta!')
        else:
            flash(f'Nenhuma conta associada ao e-mail: {form_login.email.data}', 'alert-danger')
    else:
        print('Erro no formulário de login: ', form_login.errors)

    return render_template('login.html', form_login=form_login)


@app.route('/sair')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
