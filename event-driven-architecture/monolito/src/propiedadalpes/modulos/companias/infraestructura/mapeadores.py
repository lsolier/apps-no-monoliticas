""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
from dataclasses import asdict
import json

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
        contacto_dto.fecha_actualizacion = entidad.fecha_actualizacion
        contacto_dto.fecha_creacion = entidad.fecha_creacion
        contacto_dto.id = str(entidad.id)
        contacto_dto.nombre = entidad.nombre
        contacto_dto.numero_telefono = entidad.numero_telefono
        return contacto_dto

    def _procesar_direccion(self, value_object: Direccion) -> str:
        return '{} {}'.format(value_object.nombre, value_object.numero)
    
    def _procesar_sucursal(self, entidad: Sucursal) -> list:
        sucursales_dto = list()
        for direccion in entidad.direcciones:
            sucursal_dto = SucursalDTO()
            sucursal_dto.fecha_creacion = entidad.fecha_creacion
            sucursal_dto.fecha_actualizacion = entidad.fecha_actualizacion
            sucursal_dto.id = str(entidad.id)
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

        print('debug10-->', compania_dto)
        return compania_dto

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        return compania