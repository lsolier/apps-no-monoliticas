import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from propiedadalpes.modulos.usuarios.infraestructura.schema.v1.eventos import EventoUsuarioIngestado
from propiedadalpes.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-usuario', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadalpes-sub-eventos', schema=AvroSchema(EventoUsuarioIngestado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje) 

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()