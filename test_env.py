from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener la clave secreta
secret_key = os.getenv('SECRET_KEY')

# Mostrar resultados
print("SECRET_KEY cargada:", secret_key)
print("Tipo:", type(secret_key))
print("Longitud:", len(secret_key) if secret_key else 0)

# Verificar si es la clave por defecto
if secret_key == 'clave_por_defecto_segura_cambiar_en_produccion':
    print("\n¡ADVERTENCIA! Se está utilizando la clave por defecto.")
    print("Por favor, configura una clave secreta en el archivo .env")
else:
    print("\n¡La clave secreta se ha cargado correctamente desde .env!")
