class Usuario:
    def __init__(self, id, usuario, contrasena):
        self.id = id
        self.usuario = usuario
        self.contrasena = contrasena

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar su uso en la vista"""
        return {"id": self.id, "usuario": self.usuario, "contrasena": self.contrasena}
