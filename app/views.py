from app import app
from flask import render_template, url_for, request

@app.route('/')
def homepage():
    usuario = 'Manske'
    idade = 17
    context ={
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html')

@app.route('/contato/')
def novapagina():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.ger('pesquisa')
        context.update({'pesquisa':pesquisa})
    return render_template('contato.html', context=context)
