from flask import render_template
from app import app
from app.models.usuario import Usuario

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.obtener_todos()
    return render_template('usuarios/index.html', usuarios=usuarios)
