""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from propiedadalpes.config.db import db
from propiedadalpes.modulos.companias.dominio.repositorios import RepositorioCompanias, RepositorioContactos
from propiedadalpes.modulos.companias.dominio.fabricas import FabricaVuelos
from uuid import UUID

class RepositorioContactosSQLite(RepositorioContactos):

    def obtener_por_id(self, id: UUID) -> Compania:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Compania]:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioCompaniasSQLite(RepositorioCompanias):

    def __init__(self):
        self._fabrica_reservas: FabricaReservas = FabricaReservas()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_reservas

    def obtener_por_id(self, id: UUID) -> Reserva:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Reserva]:
        # TODO
        raise NotImplementedError

    def agregar(self, reserva: Reserva):
        # TODO
        raise NotImplementedError

    def actualizar(self, reserva: Reserva):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError