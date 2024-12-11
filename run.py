from flask import Flask, render_template

# Crear una instancia de Flask
app = Flask(__name__)

# Definir las rutas
@app.route('/')
def index():
    # Renderiza la vista index.html
    return render_template('usuarios/index.html')

# Arrancar el servidor cuando se ejecuta este archivo directamente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
