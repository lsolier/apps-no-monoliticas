from propiedadalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from .dto import CompaniaDTO, ContactoDTO, SucursalDTO, DireccionDTO

class MapeadorCompaniaDTOJson(AppMap):

    def _procesar_contacto(self, contacto: dict) -> ContactoDTO:
        return ContactoDTO(contacto.get('nombre'), contacto.get('numero_telefono'))
    
    def _procesar_sucursal(self, sucursal: dict) -> SucursalDTO:

        direcciones_dto: list[DireccionDTO] = list()
        for direccion in sucursal.get('direcciones', list()):
            direccion_dto = DireccionDTO()
            direccion_dto.nombre = direccion.get('nombre')
            direccion_dto.numero = direccion.get('numero')
            direccion_dto.codigo_postal = direccion.get('codigo_postal')
            direcciones_dto.append(direccion_dto)
        
        return SucursalDTO(sucursal.get('departamento'), sucursal.get('distrito'), direcciones_dto)
    
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        coleccion_dto = CompaniaDTO()

        for contacto in externo.get('contactos_clave', list()):
            coleccion_dto.contactos.append(self._procesar_contacto(contacto))

        for sucursal in externo.get('sucursales', list()):
            coleccion_dto.sucursales.append(self._procesar_contacto(sucursal))

        return coleccion_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__
    
class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return CompaniaDTO(fecha_creacion, fecha_actualizacion, _id, list())

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        reserva = Compania()
        reserva.itinerarios = list()

        itinerarios_dto: list[ItinerarioDTO] = dto.itinerarios

        for itin in itinerarios_dto:
            reserva.itinerarios.append(self._procesar_itinerario(itin))
        
        return reserva