
from config.bd import bd, ma, app



class Cartelera(bd.Model):
    __tablename__ = 'Cartelera'
    id = bd.Column(bd.Integer, primary_key=True)
    title = bd.Column(bd.String(50))
    director = bd.Column(bd.String(50))
    imageUrl = bd.Column(bd.String(50))
    description = bd.Column(bd.String(50))
    horario = bd.Column(bd.String(50))
    categories = bd.Column(bd.String(50))
    isFavorite = bd.Column(bd.Boolean)
    review = bd.Column(bd.String(50))
   
    def __init__(self, title, director, imageUrl, description, horario, categories, isFavorite, review):
        self.title = title
        self.director = director
        self.imageUrl = imageUrl
        self.description = description
        self.horario = horario
        self.categories = categories
        self.isFavorite = isFavorite
        self.review = review
        
with app.app_context():
    bd.create_all()

class CarteleraSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "director", "imageUrl", "description", "horario", "categories", "isFavorite", "review")

cartelera_schema = CarteleraSchema()
carteleras_schema = CarteleraSchema(many=True)  