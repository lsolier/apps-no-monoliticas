from propiedadalpes.config.db import db

Base = db.declarative_base()

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.String(40), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero_identificacion = db.Column(db.String(40), nullable=True)

class EventosUsuario(db.Model):
    __tablename__ = "eventos_usuario"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)