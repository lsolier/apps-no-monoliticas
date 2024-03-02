""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Compania
from .reglas import IdentificadorCompaniaUnicoPorPais
from .excepciones import TipoObjetoNoExisteEnDominioCompaniaExcepcion
from propiedadalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedadalpes.seedwork.dominio.fabricas import Fabrica
from propiedadalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaCompanias(Fabrica):

    def _crear_objeto(self, obj: any, existe_compania_en_pais:bool, mapeador: Mapeador) -> any:
        compania: Compania = mapeador.dto_a_entidad(obj)
        self.validar_regla(IdentificadorCompaniaUnicoPorPais(not existe_compania_en_pais))
        return compania


    def crear_objeto_entidad(self, obj: any, existe_compania_en_pais:bool, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Compania.__class__:
            return self._crear_objeto(obj, existe_compania_en_pais, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioCompaniaExcepcion()

    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Compania.__class__:
            return mapeador.entidad_a_dto(obj)
        else:
            raise TipoObjetoNoExisteEnDominioCompaniaExcepcion()

