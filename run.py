from flask import Flask
from apps.controllers.usuarios_controller import UsuarioController

app = Flask(__name__)

# Instanciar el controlador de usuarios
usuario_controller = UsuarioController()

@app.route('/')
def index():
    return usuario_controller.index()

@app.route('/guardar', methods=['POST'])
def guardar():
    return usuario_controller.guardar()

@app.route('/eliminar/<int:id>')
def eliminar(id):
    return usuario_controller.eliminar(id)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    return usuario_controller.editar(id)

if __name__ == '__main__':
    app.run(debug=True)
