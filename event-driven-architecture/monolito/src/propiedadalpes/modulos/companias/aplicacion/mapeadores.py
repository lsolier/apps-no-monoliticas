from propiedadalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadalpes.modulos.companias.dominio.entidades import Compania, Contacto, Sucursal
from propiedadalpes.modulos.companias.dominio.objetos_valor import Direccion
from .dto import CompaniaDTO, ContactoDTO, SucursalDTO, DireccionDTO

class MapeadorCompaniaDTOJson(AppMap):

    def _procesar_contacto(self, contacto: dict) -> ContactoDTO:
        return ContactoDTO(contacto.get('nombre'), contacto.get('numero_telefono'))
    
    def _procesar_sucursal(self, sucursal: dict) -> SucursalDTO:
        direcciones_dto: list[DireccionDTO] = list()
        for direccion in sucursal.get('direcciones', list()):
            direccion_dto = DireccionDTO(direccion.get('nombre'), direccion.get('numero'), direccion.get('codigo_postal'))
            direcciones_dto.append(direccion_dto)
        
        return SucursalDTO(sucursal.get('departamento'), sucursal.get('distrito'), direcciones_dto)
    
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        contactos = list()
        sucursales = list()

        for contacto in externo.get('contactos_clave', list()):
            contactos.append(self._procesar_contacto(contacto))

        for sucursal in externo.get('sucursales', list()):
            sucursales.append(self._procesar_sucursal(sucursal))

        return CompaniaDTO("", "", "", externo.get('nombre'), 
                           externo.get('numero_identificacion'), externo.get('codigo_iso_pais'), 
                           contactos, sucursales)

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__
    
class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def _procesar_contacto_dto(self, contacto_dto: ContactoDTO) -> Contacto:
        contacto = Contacto()
        contacto.nombre = contacto_dto.nombre
        contacto.numero_telefono = contacto_dto.numero_telefono
        return contacto
    
    def _procesar_sucursal_dto(self, sucursal_dto: SucursalDTO) -> Sucursal:
        direcciones: list[Direccion] = list()
        for direccion_dto in sucursal_dto.direcciones:
            direccion = Direccion(direccion_dto.nombre, direccion_dto.numero, direccion_dto.codigo_postal)
            direcciones.append(direccion)
        sucursal = Sucursal()
        sucursal.departamento = sucursal_dto.departamento
        sucursal.distrito = sucursal_dto.distrito
        sucursal.direcciones = direcciones
        return sucursal

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        compania.nombre = dto.nombre
        compania.numero_identificacion = dto.numero_identificacion
        compania.codigo_iso_pais = dto.codigo_iso_pais

        contactos_dto: list[ContactoDTO] = dto.contactos
        sucursales_dto: list[SucursalDTO] = dto.sucursales
        
        for contacto in contactos_dto:
            compania.contactos.append(self._procesar_contacto_dto(contacto))

        for sucursal in sucursales_dto:
            compania.sucursales.append(self._procesar_sucursal_dto(sucursal))
        
        return compania
    
    def _procesar_direccion(self, ov: Direccion) -> DireccionDTO:
        return DireccionDTO(ov.nombre, ov.numero, ov.codigo_postal)
    
    def _procesar_sucursal(self, entidad: Sucursal) -> SucursalDTO:
        direcciones_dto = list()
        for direccion in entidad.direcciones:
            direcciones_dto.append(self._procesar_direccion(direccion))

        return SucursalDTO(entidad.departamento, entidad.distrito, direcciones_dto)
    
    def _procesar_contacto(self, entidad: Contacto) -> ContactoDTO:
        return ContactoDTO(entidad.nombre, entidad.numero_telefono)
    
    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        contactos_dto = list()
        for contacto in entidad.contactos:
            contactos_dto.append(self._procesar_contacto(contacto))

        sucursales_dto = list()
        for sucursal in entidad.sucursales:
            sucursales_dto.append(self._procesar_sucursal(sucursal))

        return CompaniaDTO(fecha_creacion, fecha_actualizacion, _id, entidad.nombre, 
                           entidad.numero_identificacion, entidad.codigo_iso_pais, 
                           contactos_dto, sucursales_dto)