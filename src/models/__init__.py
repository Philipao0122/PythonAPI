from flask_sqlalchemy import SQLAlchemy

# Inicializar la base de datos
db = SQLAlchemy()

# Importar los modelos aquí para que estén disponibles cuando importes desde models
from .user import User
from .topic import Topic
