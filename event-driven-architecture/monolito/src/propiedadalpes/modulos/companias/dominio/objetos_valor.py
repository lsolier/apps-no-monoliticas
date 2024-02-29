"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from propiedadalpes.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Direccion(ObjetoValor):
    nombre: str = field(default_factory=str)
    numero: int = field(default_factory=int)
    codigo_postal: str = field(default_factory=str)
