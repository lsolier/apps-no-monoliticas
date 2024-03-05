from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from propiedadalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoPropiedad(EventoDominio):
    ...

@dataclass
class PropiedadIngestada(EventoDominio):
    id_propiedad: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None