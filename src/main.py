import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from models.user import db, User  # Updated import path
from routes.user import user_bp
from routes.topic_analyzer import topic_analyzer_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

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
    app.run(host='0.0.0.0', port=5002, debug=True)
