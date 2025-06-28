# This makes the src directory a Python package
# Export the Flask app for WSGI servers
from .main import app

__all__ = ['app']