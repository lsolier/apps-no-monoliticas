""" Interfaces para los repositorios del dominio de propiedades

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de propiedades

"""

from abc import ABC
from propiedadalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioPropiedades(Repositorio, ABC):
    ...

class RepositorioEventosPropiedades(Repositorio, ABC):
    ...