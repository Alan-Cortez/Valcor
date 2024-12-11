class Usuario:
    # Asegúrate de tener un sistema de base de datos configurado aquí

    @staticmethod
    def obtener_todos():
        # Este método debería interactuar con la base de datos para obtener los usuarios.
        return [
            {"id": 1, "nombre": "Alan", "apellido": "Valdez"},
            {"id": 2, "nombre": "Luis", "apellido": "Valdez"}
        ]
