from apps import create_app

# Crea una instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Inicia la aplicación en modo de desarrollo
    app.run(debug=True)
