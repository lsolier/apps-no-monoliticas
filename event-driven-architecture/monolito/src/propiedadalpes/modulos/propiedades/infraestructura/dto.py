from propiedadalpes.config.db import db

Base = db.declarative_base()

class Propiedades(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String(40), primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    ubicacion = db.Column(db.String(150), nullable=False)
    direccion = db.Column(db.String(100), nullabe=False)
    ciudad = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)ç

class EventosPropiedades(db.Model):
    __tablename__ = "eventos_propiedades"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)