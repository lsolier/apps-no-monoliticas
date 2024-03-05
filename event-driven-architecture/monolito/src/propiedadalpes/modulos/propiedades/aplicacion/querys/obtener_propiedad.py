from propiedadalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadalpes.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadalpes.modulos.companias.infraestructura.repositorios import RepositorioCompanias
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from propiedadalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
import uuid

@dataclass
class ObtenerPropiedad(Query):
    id: str

class ObtenerPropiedadHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerPropiedad) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        reserva =  self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedad())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_compania(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    return handler.handle(query)