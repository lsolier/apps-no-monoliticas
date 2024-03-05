from propiedadalpes.modulos.propiedades.dominio.eventos import PropiedadIngestada
from propiedadalpes.seedwork.aplicacion.handlers import Handler
from propiedadalpes.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedades_ingestada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedades')



    