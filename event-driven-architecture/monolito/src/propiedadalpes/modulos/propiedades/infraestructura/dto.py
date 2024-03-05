from propiedadalpes.config.db import db

Base = db.declarative_base()

class Propiedades(db.Model):
    __tablename__ = "propiedades"
    #id = db.Column(db.String(40), primary_key=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=True)
    ubicacion = db.Column(db.String(150), nullable=True)
    direccion = db.Column(db.String(100), nullable=True)
    ciudad = db.Column(db.String(100), nullable=True)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)

class EventosPropiedades(db.Model):
    __tablename__ = "eventos_propiedades"
    #id = db.Column(db.String(40), primary_key=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_entidad = db.Column(db.String(40), nullable=True)
    fecha_evento = db.Column(db.DateTime, nullable=True)
    version = db.Column(db.String(10), nullable=True)
    tipo_evento = db.Column(db.String(100), nullable=True)
    formato_contenido = db.Column(db.String(10), nullable=True)
    nombre_servicio = db.Column(db.String(40), nullable=True)
    contenido = db.Column(db.Text, nullable=True)