from propiedadalpes.config.db import db

Base = db.declarative_base()

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.String(40), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero_identificacion = db.Column(db.String(40), nullable=False)
