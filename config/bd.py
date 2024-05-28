from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/bdmovil2'
user = "Leanalf"
password = "admin123"
direc = "localhost"
namebd = "Leanalf9$tasksul"
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{direc}/{namebd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Movil2"


bd = SQLAlchemy(app)
ma = Marshmallow(app)

# Función para listar las tablas
def listar_tablas():
    inspector = bd.inspect(bd.engine)
    tablas = inspector.get_table_names()
    print("Tablas en la base de datos:")
    for tabla in tablas:
        print(tabla)

# Llamada a la función para listar las tablas
if __name__ == "__main__":
    listar_tablas()