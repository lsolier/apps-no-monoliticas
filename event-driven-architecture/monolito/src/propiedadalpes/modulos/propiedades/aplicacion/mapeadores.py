from propiedadalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadalpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import PropiedadDTO

class MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        return PropiedadDTO(externo.get('nombre'), externo.get('ubicacion'), externo.get('direccion'), "")

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__
    
class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        
        propiedad.nombre = dto.nombre
        propiedad.ubicacion = dto.ubicacion
        propiedad.direccion = dto.direccion
        propiedad.ciudad = dto.ciudad
    
        return propiedad
    
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        #_id = str(entidad.id)
        #return PropiedadDTO(_id, entidad.nombre, entidad.ubicacion, entidad.direccion, entidad.ciudad)
        return PropiedadDTO(entidad.nombre, entidad.ubicacion, entidad.direccion, entidad.ciudad)