from flask import render_template, request, redirect, url_for
from apps.models.usuario import get_db_connection

class UsuarioController:

    def index(self):
        # Conexión a la base de datos
        con = get_db_connection()
        if con:
            cursor = con.cursor()
            cursor.execute('SELECT id, nombre, apellido FROM usuarios')  # Consulta SQL
            usuarios = cursor.fetchall()
            cursor.close()
            con.close()
        else:
            usuarios = []

        return render_template('usuarios/index.html', usuarios=usuarios)

    def guardar(self):
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        
        # Conexión a la base de datos
        con = get_db_connection()
        if con:
            cursor = con.cursor()
            cursor.execute('INSERT INTO usuarios (nombre, apellido) VALUES (%s, %s)', (nombre, apellido))
            con.commit()
            cursor.close()
            con.close()
        
        return redirect(url_for('usuarios.index'))

    def eliminar(self, id):
        # Conexión a la base de datos
        con = get_db_connection()
        if con:
            cursor = con.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id = %s', (id,))
            con.commit()
            cursor.close()
            con.close()

        return redirect(url_for('usuarios.index'))

    def editar(self, id):
        # Si es un GET, mostramos el formulario con los datos del usuario
        if request.method == 'GET':
            con = get_db_connection()
            if con:
                cursor = con.cursor()
                cursor.execute('SELECT id, nombre, apellido FROM usuarios WHERE id = %s', (id,))
                usuario = cursor.fetchone()
                cursor.close()
                con.close()
            return render_template('usuarios/editar.html', usuario=usuario)

        # Si es un POST, actualizamos los datos del usuario
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            
            con = get_db_connection()
            if con:
                cursor = con.cursor()
                cursor.execute('UPDATE usuarios SET nombre = %s, apellido = %s WHERE id = %s', (nombre, apellido, id))
                con.commit()
                cursor.close()
                con.close()

            return redirect(url_for('usuarios.index'))
