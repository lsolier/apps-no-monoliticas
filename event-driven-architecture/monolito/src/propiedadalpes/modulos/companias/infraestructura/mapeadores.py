""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
from dataclasses import asdict
from itertools import groupby
from propiedadalpes.modulos.companias.dominio.eventos import CompaniaIngestada, EventoCompania
from propiedadalpes.modulos.companias.infraestructura.despachadores import unix_time_millis
from propiedadalpes.modulos.companias.infraestructura.excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

from propiedadalpes.seedwork.dominio.repositorios import Mapeador
from propiedadalpes.modulos.companias.dominio.objetos_valor import Direccion
from propiedadalpes.modulos.companias.dominio.entidades import Compania, Contacto, Sucursal
from .dto import Compania as CompaniaDTO
from .dto import Sucursal as SucursalDTO
from .dto import Contacto as ContactoDTO

class MapeadorCompania(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def _procesar_contacto(self, entidad: Contacto) -> ContactoDTO:
        contacto_dto = ContactoDTO()
        contacto_dto.id = str(entidad.id)
        contacto_dto.fecha_actualizacion = entidad.fecha_actualizacion
        contacto_dto.fecha_creacion = entidad.fecha_creacion
        contacto_dto.nombre = entidad.nombre
        contacto_dto.numero_telefono = entidad.numero_telefono
        return contacto_dto

    def _procesar_direccion(self, value_object: Direccion) -> str:
        return '{}, {}'.format(value_object.nombre, value_object.numero)
    
    def _procesar_sucursal(self, entidad: Sucursal) -> list:
        sucursales_dto = list()
        for direccion in entidad.direcciones:
            sucursal_dto = SucursalDTO()
            sucursal_dto.fecha_creacion = entidad.fecha_creacion
            sucursal_dto.fecha_actualizacion = entidad.fecha_actualizacion
            sucursal_dto.departamento = entidad.departamento
            sucursal_dto.distrito = entidad.distrito
            sucursal_dto.direccion = self._procesar_direccion(direccion)
            sucursal_dto.codigo_postal = direccion.codigo_postal
            sucursales_dto.append(sucursal_dto)
        return sucursales_dto

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        
        compania_dto = CompaniaDTO()
        compania_dto.fecha_creacion = entidad.fecha_creacion
        compania_dto.fecha_actualizacion = entidad.fecha_actualizacion
        compania_dto.id = str(entidad.id)
        compania_dto.nombre = entidad.nombre
        compania_dto.numero_identificacion = entidad.numero_identificacion
        compania_dto.codigo_iso_pais = entidad.codigo_iso_pais

        contactos_dto = list()
        sucursales_dto = list()
        
        for contacto in entidad.contactos:
            contactos_dto.append(self._procesar_contacto(contacto))

        for sucursal in entidad.sucursales:
            sucursales_dto.extend(self._procesar_sucursal(sucursal))

        compania_dto.contactos_clave = contactos_dto
        compania_dto.sucursales = sucursales_dto

        return compania_dto
    
    def _procesar_contacto_dto(self, dto: ContactoDTO) -> Contacto:
        contacto = Contacto(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        contacto.nombre = dto.nombre
        contacto.numero_telefono = dto.numero_telefono
        contacto.fecha_actualizacion = dto.fecha_actualizacion
        return contacto

    def _procesar_direccion_dto(self, direccion_dto: str, codigo_postal: str) -> Direccion:
        direccion_dto_array = direccion_dto.split(",")
        numero = int(direccion_dto_array.pop().strip())
        nombre = ','.join(direccion_dto_array)
        return Direccion(nombre, numero, codigo_postal)
    
    def _procesar_sucursales_dto(self, sucursales_dto: list[SucursalDTO]) -> list[Sucursal]:        
        sucursales_agrupadas = {}
        for clave, grupo in groupby(sucursales_dto, lambda sucursal: (sucursal.departamento, sucursal.distrito)):
            sucursales_agrupadas[clave] = list(grupo)

        sucursales = list()
        for departamento_distrito in sucursales_agrupadas:
            sucursales_dep_dis: list[SucursalDTO] = sucursales_agrupadas[departamento_distrito]
            dto: SucursalDTO = sucursales_dep_dis[0]
            sucursal = Sucursal('', dto.fecha_creacion, dto.fecha_actualizacion)
            sucursal.departamento = dto.departamento
            sucursal.distrito = dto.distrito
            for sucursal_dep_dis in sucursales_dep_dis:
                sucursal.direcciones.append(self._procesar_direccion_dto(sucursal_dep_dis.direccion, sucursal_dep_dis.codigo_postal))
            sucursales.append(sucursal)
        
        return sucursales

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        compania.nombre = dto.nombre
        compania.numero_identificacion = dto.numero_identificacion
        compania.codigo_iso_pais = dto.codigo_iso_pais

        contactos = list()

        for contacto_dto in dto.contactos_clave:
            contactos.append(self._procesar_contacto_dto(contacto_dto))

        compania.contactos = contactos
        compania.sucursales = self._procesar_sucursales_dto(dto.sucursales)

        return compania
    

class MapadeadorEventosCompania(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            CompaniaIngestada: self._entidad_a_compania_ingestada,
        }
    
    def obtener_tipo(self) -> type:
        return EventoCompania.__class__
    
    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_compania_ingestada(self, entidad: CompaniaIngestada, version=LATEST_VERSION):
        def v1(evento):
            print("debug evento --> ", evento)
            from .schema.v1.eventos import CompaniaIngestadaPayload, EventoCompaniaIngestada

            payload = CompaniaIngestadaPayload(
                id_compania=str(evento.id_compania), 
                estado=str(evento.estado), 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoCompaniaIngestada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'CompaniaIngestada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'propiedadalpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad) 
        
    def entidad_a_dto(self, entidad: EventoCompania, version=LATEST_VERSION) -> CompaniaDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: CompaniaDTO, version=LATEST_VERSION) -> Compania:
        raise NotImplementedError