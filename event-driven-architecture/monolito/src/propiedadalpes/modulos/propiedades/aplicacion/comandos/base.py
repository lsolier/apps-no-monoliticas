from propiedadalpes.seedwork.aplicacion.comandos import ComandoHandler
from propiedadalpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from propiedadalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades

class IngestarPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades    
    