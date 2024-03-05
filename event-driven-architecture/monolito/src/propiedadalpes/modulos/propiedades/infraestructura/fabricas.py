""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de companias

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from propiedadalpes.seedwork.dominio.fabricas import Fabrica
from propiedadalpes.seedwork.dominio.repositorios import Repositorio
from propiedadalpes.modulos.companias.dominio.repositorios import RepositorioCompanias, RepositorioEventosCompanias
from .repositorios import RepositorioCompaniasSQLite, RepositorioEventosCompaniaSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias:
            return RepositorioCompaniasSQLite()
        elif obj == RepositorioEventosCompanias:
            return RepositorioEventosCompaniaSQLAlchemy()
        else:
            raise ExcepcionFabrica()