from dataclasses import dataclass, field
from propiedadalpes.seedwork.dominio.fabricas import Fabrica
from propiedadalpes.seedwork.dominio.repositorios import Repositorio
from propiedadalpes.modulos.usuarios.dominio.repositorios import RepositorioUsuarios, RepositorioEventosUsuarios
from .repositorios import RepositorioUsuariosSQLite, RepositorioEventosUsuarioSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioUsuarios:
            return RepositorioUsuariosSQLite()
        elif obj == RepositorioEventosUsuarios:
            return RepositorioEventosUsuarioSQLAlchemy()
        else:
            raise ExcepcionFabrica()