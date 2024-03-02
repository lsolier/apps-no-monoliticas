from propiedadalpes.modulos.companias.dominio.eventos import CompaniaIngestada
from propiedadalpes.seedwork.aplicacion.handlers import Handler
from propiedadalpes.modulos.companias.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_compania_ingestada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')



    