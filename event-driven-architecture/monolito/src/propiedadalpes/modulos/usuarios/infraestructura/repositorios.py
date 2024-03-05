from propiedadalpes.config.db import db
from propiedadalpes.modulos.usuarios.dominio.repositorios import RepositorioUsuarios, RepositorioEventosUsuarios
from propiedadalpes.modulos.usuarios.dominio.fabricas import FabricaUsuarios
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from .dto import Usuario as UsuarioDTO
from .mapeadores import MapeadorEventosUsuario, MapeadorUsuario
from uuid import UUID
from pulsar.schema import *

class RepositorioUsuariosSQLite(RepositorioUsuarios):

    def __init__(self):
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios
    
    def obtener_por_id(self, id: UUID) -> Usuario:
        reserva_dto = db.session.query(UsuarioDTO).filter_by(id=str(id)).one()
        return self._fabrica_usuarios.crear_objeto_entidad(reserva_dto, False, MapeadorUsuario())
    
    def obtener_todos(self) -> list[Usuario]:
        # TODO
        raise NotImplementedError
    
    def agregar(self, usuario: Usuario):
        usuario_dto = self._fabrica_usuarios.crear_objeto(usuario, MapeadorUsuario())
        db.session.add(usuario_dto)
        db.session.commit()

    def actualizar(self, usuario: Usuario):
        # TODO
        raise NotImplementedError
    
    def eliminar(self, id: UUID):
        # TODO
        raise NotImplementedError
    
    def existe_por_numero_id_y_pais(self, str_1: str, str_2: str):
        # TODO
        raise NotImplementedError