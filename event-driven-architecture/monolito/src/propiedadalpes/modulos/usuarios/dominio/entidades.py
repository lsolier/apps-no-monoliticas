from __future__ import annotations
from dataclasses import dataclass, field
from itertools import groupby


from propiedadalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass 
class Usuario(AgregacionRaiz):
    nombre: str = field(default_factory=str)
