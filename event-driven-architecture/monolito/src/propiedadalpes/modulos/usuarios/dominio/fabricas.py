from propiedadalpes.modulos.usuarios.dominio.eventos import EventoUsuario
from .entidades import Usuario
from propiedadalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedadalpes.seedwork.dominio.fabricas import Fabrica
from propiedadalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaUsuarios(Fabrica):

    def _crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        usuario: Usuario = mapeador.dto_a_entidad(obj)
        return usuario
    
    def crear_objeto_entidad(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Usuario.__class__:
            return self._crear_objeto(obj, mapeador)
        else:
            raise Exception("Error")

    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Usuario.__class__:
            return mapeador.entidad_a_dto(obj)
        else:
            raise Exception("Error")

