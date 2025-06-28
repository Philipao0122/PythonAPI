import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
src_path = project_root / 'src'
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_path))

# Import the app after setting up the path
from src.main import app as application

# This is needed for WSGI servers
if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    application.run(host='0.0.0.0', port=port, debug=debug)
