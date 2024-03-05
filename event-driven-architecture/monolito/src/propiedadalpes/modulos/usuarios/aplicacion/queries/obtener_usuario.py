from propiedadalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadalpes.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadalpes.modulos.usuarios.infraestructura.repositorios import RepositorioUsuarios
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from propiedadalpes.modulos.usuarios.aplicacion.mapeadores import MapeadorUsuario
import uuid

@dataclass
class ObtenerUsuario(Query):
    id: str

class ObtenerUsuarioHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerUsuario) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)
        reserva =  self._fabrica_usuarios.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorUsuario())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerUsuario)
def ejecutar_query_obtener_usuario(query: ObtenerUsuario):
    handler = ObtenerUsuarioHandler()
    return handler.handle(query)