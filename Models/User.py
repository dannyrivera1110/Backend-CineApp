
from config.bd import bd, ma, app


class Usuario(bd.Model):
    __tablename__ = 'usuario'
    id = bd.Column(bd.Integer, primary_key=True)
    apellido = bd.Column(bd.String(50))
    telefono = bd.Column(bd.String(50))
    nombre = bd.Column(bd.String(50))
    direccion = bd.Column(bd.String(50))
    correo = bd.Column(bd.String(50))
    contrasena = bd.Column(bd.String(100))  

    def __init__(self, apellido, telefono, nombre, direccion, correo, contrasena):
        self.apellido = apellido
        self.telefono = telefono
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
        self.contrasena = contrasena
        
with app.app_context():
    bd.create_all()
    
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("id", "apellido", "telefono", "nombre", "direccion", "correo", "contrasena")

