from flask import Blueprint, render_template
from apps.models.usuario import Usuario

# Define el blueprint para las rutas relacionadas con los usuarios
usuarios_controller = Blueprint('usuarios_controller', __name__, template_folder='views/usuarios')

# Ruta para listar los usuarios
@usuarios_controller.route('/')
def index():
    # Aquí puedes obtener los usuarios desde la base de datos, pero por ahora usaremos datos estáticos
    usuarios = [
        Usuario(1, 'Alan Cortez', 'alan@example.com'),
        Usuario(2, 'Luis Valdez', 'luis@example.com'),
        Usuario(3, 'Paola Cortez', 'paola@example.com')
    ]
    return render_template('index.html', usuarios=usuarios)
