
from config.bd import bd,ma, app

class Cines(bd.Model):
    __tablename__ = 'cines'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(100))
    latitud = bd.Column(bd.Float)
    longitud = bd.Column(bd.Float)
    resenas = bd.Column(bd.JSON)
    pelicula_proyectandose = bd.Column(bd.String(100))
    horainicio = bd.Column(bd.String(50))
    imagen = bd.Column(bd.String(100))
    horarios = bd.Column(bd.String(100))
    IdCartelera = bd.Column(bd.Integer, bd.ForeignKey("Cartelera.id"))
    cartelera = bd.relationship('Cartelera', backref=bd.backref('cines', lazy=True))
    def __init__(self, nombre, latitud, longitud, resenas, pelicula_proyectandose, horainicio, imagen, horarios,IdCartelera):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.resenas = resenas
        self.pelicula_proyectandose = pelicula_proyectandose
        self.horainicio = horainicio
        self.imagen = imagen
        self.horarios = horarios
        self.IdCartelera=IdCartelera

with app.app_context():
    bd.create_all()

class CinesSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "latitud", "longitud", "resenas", "pelicula_proyectandose", "horainicio", "imagen", "horarios","IdCartelera")

cines_schema = CinesSchema()
cineses_schema = CinesSchema(many=True)
