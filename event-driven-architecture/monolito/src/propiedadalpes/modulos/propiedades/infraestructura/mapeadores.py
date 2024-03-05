""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
from dataclasses import asdict
from propiedadalpes.modulos.propiedades.dominio.eventos import PropiedadIngestada, EventoPropiedad
from propiedadalpes.modulos.companias.infraestructura.excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

from propiedadalpes.seedwork.dominio.repositorios import Mapeador
from propiedadalpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedades as PropiedadDTO

class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        return propiedad
    

class MapadeadorEventosPropiedad(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            PropiedadIngestada: self._entidad_a_propiedad_ingestada,
        }
    
    def obtener_tipo(self) -> type:
        return EventoPropiedad.__class__
    
    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_propiedad_ingestada(self, entidad: PropiedadIngestada, version=LATEST_VERSION):
        def v1(evento):
            print("debug evento --> ", evento)
            raise NotImplementedError
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad) 
        
    def entidad_a_dto(self, entidad: EventoPropiedad, version=LATEST_VERSION) -> PropiedadDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: PropiedadDTO, version=LATEST_VERSION) -> Propiedad:
        raise NotImplementedError