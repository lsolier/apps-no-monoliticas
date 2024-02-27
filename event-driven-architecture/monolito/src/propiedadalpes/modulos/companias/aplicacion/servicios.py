from propiedadalpes.seedwork.aplicacion.servicios import Servicio
from propiedadalpes.modulos.companias.infraestructura.fabricas import FabricaRepositorio
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
        compania: Compania = self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        repositorio.agregar(reserva)

        return self.fabrica_vuelos.crear_objeto(reserva, MapeadorReserva())