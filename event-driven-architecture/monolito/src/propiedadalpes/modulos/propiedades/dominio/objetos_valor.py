"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from propiedadalpes.seedwork.dominio.objetos_valor import ObjetoValor

class EstadoPropiedad(str, Enum):
    INGESTADA = "Ingestada"
    AUDITADA = "Auditada"
    VALIDADA = "Validada"