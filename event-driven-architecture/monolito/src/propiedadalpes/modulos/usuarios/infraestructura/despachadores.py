import pulsar
from pulsar.schema import *

from propiedadalpes.modulos.usuarios.infraestructura.schema.v1.eventos import UsuarioIngestadoPayload, EventoUsuarioIngestado
from propiedadalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoUsuarioIngestado))
        publicador.send(mensaje)
        cliente.close()

def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = UsuarioIngestadoPayload(
            id_usuario=str(evento.id_usuario),
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoUsuarioIngestado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoUsuarioIngestado))