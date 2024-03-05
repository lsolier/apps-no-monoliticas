""" Fábricas para la creación de objetos del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de propiedades

"""
from propiedadalpes.modulos.propiedades.dominio.eventos import EventoPropiedad
from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioCompaniaExcepcion
from propiedadalpes.seedwork.dominio.repositorios import Mapeador
from propiedadalpes.seedwork.dominio.fabricas import Fabrica
from propiedadalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaPropiedades(Fabrica):

    def _crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        propiedad: Propiedad = mapeador.dto_a_entidad(obj)
        return propiedad

    def crear_objeto_entidad(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            return self._crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioCompaniaExcepcion()

    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Compania.__class__:
            return mapeador.entidad_a_dto(obj)
        else:
            raise TipoObjetoNoExisteEnDominioCompaniaExcepcion()

