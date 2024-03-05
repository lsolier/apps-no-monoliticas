from propiedadalpes.config.db import db
from propiedadalpes.modulos.usuarios.dominio.repositorios import RepositorioUsuarios, RepositorioEventosUsuarios
from propiedadalpes.modulos.usuarios.dominio.fabricas import FabricaUsuarios
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from .dto import Usuario as UsuarioDTO, EventoUsuario
from .mapeadores import MapeadoreEventosUsuario, MapeadorUsuario
from uuid import UUID
from pulsar.schema import *

class RepositorioUsuariosSQLite(RepositorioUsuarios):

    def __init__(self):
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    def fabrica_usuarios(self):
        return self._fabrica_usuarios

class RepositorioEventosUsuarioSQLAlchemy(RepositorioEventosUsuarios):

    def __init__(self):
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()