""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from propiedadalpes.config.db import db
from propiedadalpes.modulos.companias.dominio.repositorios import RepositorioCompanias, RepositorioContactos
from propiedadalpes.modulos.companias.dominio.fabricas import FabricaCompanias
from propiedadalpes.modulos.companias.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO
from .mapeadores import MapeadorCompania
from uuid import UUID

class RepositorioCompaniasSQLite(RepositorioCompanias):

    def __init__(self):
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_companias(self):
        return self._fabrica_companias

    def obtener_por_id(self, id: UUID) -> Compania:
        reserva_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self._fabrica_companias.crear_objeto_entidad(reserva_dto, False, MapeadorCompania())
    
    def obtener_todos(self) -> list[Compania]:
        # TODO
        raise NotImplementedError

    def agregar(self, compania: Compania):
        compania_dto = self._fabrica_companias.crear_objeto(compania, MapeadorCompania())
        db.session.add(compania_dto)
        db.session.commit()

    def actualizar(self, compania: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, compania_id: UUID):
        # TODO
        raise NotImplementedError
    
    def existe_por_numero_id_y_pais(self, numero_identificacion: str, codigo_iso_pais: str):
        return bool(db.session
                    .query(CompaniaDTO)
                    .filter_by(numero_identificacion=numero_identificacion, codigo_iso_pais=codigo_iso_pais)
                    .first())

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
