import os
import sys
from pathlib import Path
from waitress import serve

# Add the project root and src to Python path
project_root = Path(__file__).parent
src_path = project_root / 'src'
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_path))

# Import the app after setting up the path
from src.main import app

if __name__ == "__main__":
    port = int(os.getenv('PORT', 10000))
    print(f"Starting server on port {port}...")
    print(f"Python path: {sys.path}")
    print(f"Current working directory: {os.getcwd()}")
    
    # Verify required modules
    try:
        from src.models import user
        from src.routes import user as user_routes
        from src.routes import topic_analyzer
        print("All required modules found!")
    except ImportError as e:
        print(f"Error importing modules: {e}")
        raise
    
    # Start the server
    print(f"Server running at: http://localhost:{port}")
    serve(app, host='0.0.0.0', port=port)
