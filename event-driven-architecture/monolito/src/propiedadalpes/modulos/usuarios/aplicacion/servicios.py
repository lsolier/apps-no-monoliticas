from propiedadalpes.seedwork.aplicacion.servicios import Servicio
from propiedadalpes.modulos.usuarios.infraestructura.fabricas import FabricaRepositorio
from propiedadalpes.modulos.usuarios.dominio.fabricas import FabricaUsuarios
from propiedadalpes.modulos.usuarios.dominio.repositorios import RepositorioUsuarios
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from .dto import UsuarioDTO
from .mapeadores import MapeadorUsuario

class ServicioUsuario(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

        @property
        def fabrica_repositorio(self):
            return self._fabrica_repositorio
        
        @property
        def fabrica_usuarios(self):
            return self._fabrica_usuarios
        
        def ingestar_usuario(self, usuario_dto: UsuarioDTO) -> UsuarioDTO:
            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)

            usuario: Usuario = self.fabrica_usuarios.crear_objeto_entidad(usuario_dto, MapeadorUsuario())

            repositorio.agregar(usuario)

            return self.fabrica_usuarios.crear_objeto(usuario, MapeadorUsuario())
        
        def obtener_usuario_por_id(self, id) -> UsuarioDTO:
            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)
            usuario: Usuario = repositorio.obtener_por_id(id)
            return self.fabrica_usuarios.crear_objeto(usuario, MapeadorUsuario())