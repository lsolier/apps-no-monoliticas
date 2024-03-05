from propiedadalpes.modulos.usuarios.aplicacion.comandos.base import IngestarUsuarioBaseHandler
from propiedadalpes.modulos.usuarios.aplicacion.dto import UsuarioDTO
from propiedadalpes.modulos.usuarios.aplicacion.mapeadores import MapeadorUsuario
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from propiedadalpes.modulos.usuarios.dominio.repositorios import RepositorioUsuarios, RepositorioEventosUsuarios
from propiedadalpes.seedwork.aplicacion.comandos import Comando
from propiedadalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from dataclasses import dataclass, field

@dataclass
class IngestarUsuario(Comando):
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)

class IngestarUsuarioHandler(IngestarUsuarioBaseHandler):

    def handle(self, comando: IngestarUsuario):
        usuario_dto = UsuarioDTO(comando.id, comando.nombre)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios)
        usuario: Usuario = self._fabrica_usuarios.crear_objeto(RepositorioEventosUsuarios)
        usuario.ingestar_usuario(usuario)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosUsuarios)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, usuario ,repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.commit()

@comando.register(IngestarUsuario)
def ejecutar_comando_ingestar_usuario(comando: IngestarUsuario):
    handler = IngestarUsuarioHandler()
    handler.handle(comando)