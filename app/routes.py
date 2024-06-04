from app import app, database
from flask import render_template, request, redirect

@app.route('/')
def index():
    conexao_db = database.conectar_db()
    cursor_db = conexao_db.cursor()
    cursor_db.execute("SELECT * FROM produtos")
    produtos = cursor_db.fetchall()
    cursor_db.close()
    conexao_db.close()
    return render_template("index.html", produtos=produtos)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        imagem = request.form.get('imagem')
        conexao_db = database.conectar_db()
        cursor_db = conexao_db.cursor()
        cursor_db.execute(
            "INSERT INTO produtos VALUES(?, ?, ?, ?, ?)",
            (codigo, nome, descricao, preco, imagem)
        )
        conexao_db.commit()
        conexao_db.close()
        return redirect('/')
    return render_template("adicionar.html")

@app.route('/editar', methods=['GET', 'PUT'])
def editar():
    if request.method == 'PUT':
        #Atualizar na base de dados
        return redirect('/')
    return render_template("editar.html")