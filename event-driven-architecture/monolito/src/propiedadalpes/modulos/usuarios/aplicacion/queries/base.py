from propiedadalpes.seedwork.aplicacion.queries import QueryHandler
from propiedadalpes.modulos.usuarios.infraestructura.fabricas import FabricaRepositorio
from propiedadalpes.modulos.usuarios.dominio.fabricas import FabricaUsuarios

class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios  