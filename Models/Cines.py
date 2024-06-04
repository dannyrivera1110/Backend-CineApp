
from config.bd import bd,ma, app

class Cines(bd.Model):
    __tablename__ = 'cines'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(100))
    latitud = bd.Column(bd.Float)
    longitud = bd.Column(bd.Float)
    resenas = bd.Column(bd.String(100))
    pelicula_proyectandose = bd.Column(bd.String(100))
    horainicio = bd.Column(bd.String(50))
    imagen = bd.Column(bd.String(100))
    horarios = bd.Column(bd.String(100))
   
    def __init__(self, nombre, latitud, longitud, resenas, pelicula_proyectandose, horainicio, imagen, horarios):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.resenas = resenas
        self.pelicula_proyectandose = pelicula_proyectandose
        self.horainicio = horainicio
        self.imagen = imagen
        self.horarios = horarios
        

with app.app_context():
    bd.create_all()

class CinesSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "latitud", "longitud", "resenas", "pelicula_proyectandose", "horainicio", "imagen", "horarios","IdCartelera")


