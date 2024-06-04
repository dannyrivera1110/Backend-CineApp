
from flask_cors import CORS
from config.bd import app

from APis.usuario import usuario_bp
from APis.cines import cines_bp
from APis.cartelera import cartelera_bp

app.register_blueprint(cartelera_bp, url_prefix='/api')
app.register_blueprint(cines_bp, url_prefix='/api')
app.register_blueprint(usuario_bp, url_prefix='/api')

#Enable CORS for the entire application
CORS(app)


@app.route("/")
def index():
    return "Welcome to the backend  "


#if __name__ == "__main__":
 #   app.run(debug=True, port=5000, host="0.0.0.0")