# apps/models/usuario.py
import mysql.connector

def get_db_connection():
    # Configuración de conexión MySQL
    try:
        con = mysql.connector.connect(
            host="185.232.14.52",  # Cambia a tu host
            database="u760464709_tst_sep",  # Cambia a tu base de datos
            user="u760464709_tst_sep_usr",  # Cambia a tu usuario
            password="dJ0CIAFF="  # Cambia a tu contraseña
        )
        return con
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
