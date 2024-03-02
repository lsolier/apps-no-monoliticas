from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from propiedadalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaIngestada(EventoDominio):
    id_compania: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    