from propiedadalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from .dto import UsuarioDTO

class MapeadorUsuarioDTOJson(AppMap):
    pass

class MapeadorUsuario(RepMap):

    def obtener_tipo(self) -> type:
        return Usuario.__class__