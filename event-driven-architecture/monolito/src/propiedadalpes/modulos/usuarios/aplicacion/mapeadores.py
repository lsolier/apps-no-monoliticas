from propiedadalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from .dto import UsuarioDTO

class MapeadorUsuarioDTOJson(AppMap):
    pass

class MapeadorUsuario(RepMap):

    def obtener_tipo(self) -> type:
        return Usuario.__class__
    
    def dto_a_entidad(self, dto: UsuarioDTO) -> Usuario:
        usuario = Usuario()
        usuario.nombre = dto['nombre']
        return usuario
    
    def entidad_a_dto(self, entidad: Usuario) -> UsuarioDTO:
        _id = str(entidad.id)
        return UsuarioDTO( _id, entidad.nombre)