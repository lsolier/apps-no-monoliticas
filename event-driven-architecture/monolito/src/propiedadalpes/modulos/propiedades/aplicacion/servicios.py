from propiedadalpes.seedwork.aplicacion.servicios import Servicio
from propiedadalpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from propiedadalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from propiedadalpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadalpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import PropiedadDTO
from .mapeadores import MapeadorPropiedad

class ServicioCompania(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades
    
    def ingestar_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        propiedad: Propiedad = self._fabrica_propiedades.crear_objeto_entidad(propiedad_dto, MapeadorPropiedad())
        repositorio.agregar(propiedad)
        return self._fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
    
    def obtener_compania_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        propiedad: Propiedad = repositorio.obtener_por_id(id)
        return self._fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())