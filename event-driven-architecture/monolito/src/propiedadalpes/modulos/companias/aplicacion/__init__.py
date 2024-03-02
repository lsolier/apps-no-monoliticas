from pydispatch import dispatcher

from .handlers import HandlerCompaniaIntegracion

from propiedadalpes.modulos.companias.dominio.eventos import CompaniaIngestada

dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_ingestada, signal=f'{CompaniaIngestada.__name__}Integracion')
