""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from propiedadalpes.config.db import db
from propiedadalpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioEventosPropiedades
from propiedadalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from propiedadalpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedades as PropiedadDTO, EventosPropiedades
from .mapeadores import MapadeadorEventosPropiedad, MapeadorPropiedad
from uuid import UUID
from pulsar.schema import *

class RepositorioCompaniasSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_companias(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        reserva_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self._fabrica_propiedades.crear_objeto_entidad(reserva_dto, False, MapeadorPropiedad())
    
    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self._fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)
        db.session.commit()

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioEventosCompaniaSQLAlchemy(RepositorioEventosPropiedades):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    def obtener_por_id(self, id: UUID) -> Propiedad:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, evento):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError