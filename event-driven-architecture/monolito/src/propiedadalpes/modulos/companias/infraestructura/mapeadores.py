""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
from dataclasses import asdict
from itertools import groupby

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