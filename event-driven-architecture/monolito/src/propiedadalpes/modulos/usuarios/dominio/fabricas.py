from propiedadalpes.modulos.usuarios.dominio.eventos import EventoUsuario
from .entidades import Usuario
from .excepciones import TipoObjetoNoExisteEnDominioCompaniaExcepcion
from propiedadalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedadalpes.seedwork.dominio.fabricas import Fabrica
from propiedadalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaUsuarios(Fabrica):

    def _crear_objeto(self, obj: any, existe_usuario:bool, mapeador: Mapeador) -> any:
        usuario: Usuario = mapeador.dto_a_entidad(obj)
        return usuario