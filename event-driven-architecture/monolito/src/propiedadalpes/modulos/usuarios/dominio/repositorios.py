from abc import ABC
from propiedadalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioUsuarios(Repositorio, ABC):
    ...

class RepositorioEventosUsuarios(Repositorio, ABC):
    ...