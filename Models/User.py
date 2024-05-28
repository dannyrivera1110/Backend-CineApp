
from config.bd import bd, ma, app
from werkzeug.security import generate_password_hash

class Usuario(bd.Model):
    __tablename__ = 'usuario'
    id = bd.Column(bd.Integer, primary_key=True)
    apellido = bd.Column(bd.String(50))
    telefono = bd.Column(bd.String(50))
    nombre = bd.Column(bd.String(50))
    direccion = bd.Column(bd.String(50))
    correo = bd.Column(bd.String(50))
    contrasena = bd.Column(bd.String(100))  # Incrementar tamaño para almacenar hash

    def __init__(self, apellido, telefono, nombre, direccion, correo, contrasena):
        self.apellido = apellido
        self.telefono = telefono
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
        self.contrasena = generate_password_hash(contrasena)  # Hashear la contraseña
        
with app.app_context():
    bd.create_all()
    
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("id", "apellido", "telefono", "nombre", "direccion", "correo", "contrasena")

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)