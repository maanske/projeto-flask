from app import app
from flask import render_template

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
    return 'nova'
