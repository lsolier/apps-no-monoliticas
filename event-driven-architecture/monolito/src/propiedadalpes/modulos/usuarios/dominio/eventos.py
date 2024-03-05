from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from propiedadalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoUsuario(EventoDominio):
    ...

@dataclass
class UsuarioIngestado(EventoDominio):
    id_usuario: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None