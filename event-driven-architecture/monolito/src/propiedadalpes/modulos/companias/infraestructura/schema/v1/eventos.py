from pulsar.schema import *
from propiedadalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaIngestadaPayload(Record):
    id_compania = String()
    estado = String()
    fecha_creacion = Long()

class EventoCompaniaIngestada(EventoIntegracion):
    data = CompaniaIngestadaPayload()