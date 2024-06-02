from app import app
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        #Adicionar na base de dados
        return redirect('/')
    return render_template("adicionar.html")

@app.route('/editar', methods=['GET', 'PUT'])
def editar():
    if request.method == 'PUT':
        #Atualizar na base de dados
        return redirect('/')
    return render_template("editar.html")