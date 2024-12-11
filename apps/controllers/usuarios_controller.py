from flask import render_template, request, redirect, url_for
from apps.models.usuario import Usuario

class UsuarioController:
    # Lista simulada de usuarios
    usuarios = [
        Usuario(1, 'juanperez', '12345'),
        Usuario(2, 'mariaflores', 'password'),
        Usuario(3, 'luisgomez', 'mypassword')
    ]

    def index(self):
        """Renderiza la vista con todos los usuarios"""
        return render_template('usuarios/index.html', usuarios=self.usuarios)

    def guardar(self):
        """Guarda un nuevo usuario"""
        usuario = request.form['txtUsuarioFA']
        contrasena = request.form['txtContrasenaFA']
        nuevo_usuario = Usuario(len(self.usuarios) + 1, usuario, contrasena)
        self.usuarios.append(nuevo_usuario)
        return redirect(url_for('index'))

    def eliminar(self, id):
        """Elimina un usuario por su id"""
        self.usuarios = [usuario for usuario in self.usuarios if usuario.id != int(id)]
        return redirect(url_for('index'))

    def editar(self, id):
        """Edita los datos de un usuario"""
        usuario = next((usuario for usuario in self.usuarios if usuario.id == int(id)), None)
        if usuario and request.method == 'POST':
            usuario.usuario = request.form['txtUsuarioFA']
            usuario.contrasena = request.form['txtContrasenaFA']
            return redirect(url_for('index'))
        
        return render_template('usuarios/editar.html', usuario=usuario)
