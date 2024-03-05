from pulsar.schema import *
from propiedadalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from propiedadalpes.seedwork.infraestructura.utils import time_millis
import uuid

class UsuarioIngestadoPayload(Record):
    id_usuario = String()
    fecha_creacion = Long()

class EventoUsuarioIngestado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = UsuarioIngestadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)