# app.py

from flask import Flask, current_app

from config.bd import app 

# Importar blueprints desde routes
from routes import cartelera_bp, cines_bp, usuario_bp

# Inicializar la aplicación Flask
app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(cartelera_bp, url_prefix='/api')
app.register_blueprint(cines_bp, url_prefix='/api')
app.register_blueprint(usuario_bp, url_prefix='/api')



if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")