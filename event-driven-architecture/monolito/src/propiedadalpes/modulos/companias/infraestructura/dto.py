from propiedadalpes.config.db import db

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla companias e contactos
companias_contactos = db.Table(
    "companias_contactos",
    db.Model.metadata,
    db.Column("compania_id", db.String, db.ForeignKey("companias.id")),
    db.Column("contacto_id", db.Integer, db.ForeignKey("contactos.id"))
)

class Contacto(db.Model):
    __tablename__ = "contactos"
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    numero_telefono = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    __table_args__ = (
        db.UniqueConstraint('nombre', 'numero_telefono', name='_contaco_nombre_numero_telefono_uc'),
    )

class Sucursal(db.Model):
    __tablename__ = "sucursales"
    id = db.Column(db.String, primary_key=True)
    departamento = db.Column(db.String, nullable=False)
    distrito = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=False)
    codigo_postal = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("companias.id"))
    __table_args__ = (
        db.UniqueConstraint('departamento', 'distrito', 'direccion', 'codigo_postal', name='_sucursal_uc'),
    )

class Compania(db.Model):
    __tablename__ = "companias"
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    numero_identificacion = db.Column(db.String, nullable=False)
    codigo_iso_pais = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    sucursales = db.relationship('Sucursal')
    contactos_clave = db.relationship('Contacto', secondary=companias_contactos, backref='companias')
    __table_args__ = (
        db.UniqueConstraint('nombre', 'numero_identificacion', 'codigo_iso_pais', name='_compania_uc'),
    )
