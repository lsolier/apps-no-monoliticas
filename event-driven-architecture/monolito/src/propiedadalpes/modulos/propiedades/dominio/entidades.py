"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propeidades

"""

from __future__ import annotations
from dataclasses import dataclass, field
from propiedadalpes.seedwork.dominio.entidades import Entidad
import propiedadalpes.modulos.propiedades.dominio.objetos_valor as ov

@dataclass
class Propiedad(Entidad):
    id: str = field(default_factory=str)
    estado: ov.EstadoPropiedad = field(default=ov.EstadoPropiedad.INGESTADA)
    nombre: str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)