from propiedadalpes.seedwork.aplicacion.queries import QueryHandler
from propiedadalpes.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from propiedadalpes.modulos.companias.dominio.fabricas import FabricaCompanias

class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_companias(self):
        return self._fabrica_companias    