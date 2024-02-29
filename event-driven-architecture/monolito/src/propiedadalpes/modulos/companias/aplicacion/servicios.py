from propiedadalpes.seedwork.aplicacion.servicios import Servicio
from propiedadalpes.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from propiedadalpes.modulos.companias.dominio.fabricas import FabricaCompanias
from propiedadalpes.modulos.companias.dominio.repositorios import RepositorioCompanias
from propiedadalpes.modulos.companias.dominio.entidades import Compania
from .dto import CompaniaDTO
from .mapeadores import MapeadorCompania

class ServicioCompania(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_companias(self):
        return self._fabrica_companias
    
    def ingestar_compania(self, compania_dto: CompaniaDTO) -> CompaniaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        existe_compania_en_pais: bool = repositorio.existe_por_numero_id_y_pais(compania_dto.numero_identificacion, compania_dto.codigo_iso_pais)

        compania: Compania = self.fabrica_companias.crear_objeto2(compania_dto, existe_compania_en_pais, MapeadorCompania())

        repositorio.agregar(compania)

        return self.fabrica_companias.crear_objeto(compania, MapeadorCompania())