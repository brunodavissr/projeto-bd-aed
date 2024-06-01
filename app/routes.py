from app import app
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        print(request.form)
        return redirect("/")
    return render_template("adicionar.html")