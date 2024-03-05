from propiedadalpes.seedwork.aplicacion.comandos import ComandoHandler
from propiedadalpes.modulos.usuarios.infraestructura.fabricas import FabricaRepositorio
from propiedadalpes.modulos.usuarios.dominio.fabricas import FabricaUsuarios

class IngestarUsuarioBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def _fabrica_usuarios(self):
        return self._fabrica_usuarios