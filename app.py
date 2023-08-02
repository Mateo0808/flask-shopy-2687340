#dependencia de flask
from flask import Flask
#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
#Dependencias de migraciones
from flask_migrate import Migrate 
#Dependencia para fecha y hora del sistema
from datetime import datetime

#crear el objeto flask
app = Flask(__name__)

#Definir 'la cadena de conexion' (connectionsString)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

#crear el objeto para crear Modelos:

db = SQLAlchemy(app)

#CREAR EL OBJETO DE MIGRACION
migrate = Migrate(app, db)

#crear los modelos
class Cliente (db.Model):
    #definir los atributos
    __tablename__ = "clientes"
    id = db.Column(db.Integer , primary_key = True )
    username = db.Column(db.String(120), 
                         nullable = True)
    password = db.Column(db.String(128),
                         nullable = True)
    email = db.Column(db.String(100),
                      nullable = True)
    
class Producto(db.Model):
    __tablename__ ="productos"
    id = db.Column(db.Integer , primary_key = True )
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))
    
class Venta(db.Model):
    #Definir los atributos
    __tablename__ ="ventas"
    id = db.Column(db.Integer , primary_key = True )
    fecha = db.Column(db.DateTime,
                      default = datetime.utcnow)
    #Clave foranea
    cliente_id = db.Column(db.Integer, 
                           db.ForeignKey('clientes.id'))
    
    
class Detalle(db.Model):
    #Definir los atributos
    __tablename__ ="detalles"
    id = db.Column(db.Integer , primary_key = True )
    #Clave foranea
    producto_id = db.Column(db.Integer, 
                           db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, 
                           db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)
    

    