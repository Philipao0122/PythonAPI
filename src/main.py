import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

# Cargar variables de entorno
load_dotenv()

# Configuración de rutas
BASE_DIR = Path(__file__).parent.parent
SRC_DIR = Path(__file__).parent

# Asegurar que el directorio de la base de datos exista
DB_DIR = SRC_DIR / 'database'
DB_DIR.mkdir(exist_ok=True)

# Configuración de la aplicación
app = Flask(__name__, 
            static_folder=os.path.join(SRC_DIR, 'static'))

# Configuración de seguridad
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'clave-temporal-cambiar-en-produccion')

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_DIR}/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
from models.user import db
db.init_app(app)

# Importar y registrar blueprints
try:
    from routes.user import user_bp
    from routes.topic_analyzer import topic_analyzer_bp
    
    # Registrar blueprints una sola vez
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(topic_analyzer_bp, url_prefix='/api/topics')
    
    # Crear tablas de la base de datos
    with app.app_context():
        db.create_all()
        print(f"Base de datos creada en: {DB_DIR}/app.db")
        
except ImportError as e:
    print(f"Error al importar módulos: {e}")
    raise

# Habilitar CORS para todas las rutas
CORS(app)

# Ruta para servir archivos estáticos
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Ruta de prueba
@app.route('/')
def index():
    return jsonify({
        'message': 'Bienvenido a la API',
        'status': 'success',
        'endpoints': {
            'users': '/api/users',
            'topics': '/api/topics'
        }
    })


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5002))
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    print(f"Iniciando servidor en modo {'debug' if debug else 'producción'}")
    print(f"URL: http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
