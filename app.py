# app.py
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from config.Token import generar_token, verificar_token
from config.bd import app,bd
# Importar blueprints desde routes
from APis import cartelera_bp, cines_bp, usuario_bp

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'abcde'
jwt = JWTManager(app)



# Inicializar la aplicación Flask
app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(cartelera_bp, url_prefix='/api')
app.register_blueprint(cines_bp, url_prefix='/api')
app.register_blueprint(usuario_bp, url_prefix='/api')

@app.route('/obtenertoken', methods=["GET"])
def obtenertoken():
    datatoken = generar_token('Daniel', '123')
    var_token = datatoken['token']
    response = {
        "statusCode": 200,
        "body": var_token
    }
    return jsonify(response)

# Ruta para verificar el token
@app.route('/verificaciontoken', methods=["GET"])
def verificaciontoken():
    token = request.headers['Authorization']
    token = token.replace('Bearer ', "").replace("", "")
    vf = verificar_token(token)
    print(f"vf=>{vf}")
    return jsonify(vf)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")