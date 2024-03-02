from propiedadalpes.modulos.companias.aplicacion.comandos.base import IngestarCompaniaBaseHandler
from propiedadalpes.modulos.companias.aplicacion.dto import CompaniaDTO, ContactoDTO, SucursalDTO
from propiedadalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompania
from propiedadalpes.modulos.companias.dominio.entidades import Compania
from propiedadalpes.modulos.companias.dominio.repositorios import RepositorioCompanias
from propiedadalpes.seedwork.aplicacion.comandos import Comando
from propiedadalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from dataclasses import dataclass, field

@dataclass
class IngestarCompania(Comando):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    numero_identificacion: str = field(default_factory=str)
    codigo_iso_pais: str = field(default_factory=str)
    contactos: list[ContactoDTO] = field(default_factory=list)
    sucursales: list[SucursalDTO] = field(default_factory=list)

# @dataclass
# class IngestarCompania(Comando):
#     fecha_creacion: str
#     fecha_actualizacion: str
#     id: str
#     nombre: str
#     numero_identificacion: str
#     codigo_iso_pais: str
#     contactos: list[ContactoDTO]
#     sucursales: list[SucursalDTO]

class IngestarCompaniaHandler(IngestarCompaniaBaseHandler):
    
    def handle(self, comando: IngestarCompania):
        compania_dto = CompaniaDTO(comando.fecha_creacion, comando.fecha_actualizacion, comando.id, 
                                   comando.nombre, comando.numero_identificacion, comando.codigo_iso_pais, 
                                   comando.contactos, comando.sucursales)
        
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        existe_compania_en_pais: bool = repositorio.existe_por_numero_id_y_pais(compania_dto.numero_identificacion, compania_dto.codigo_iso_pais)

        compania: Compania = self.fabrica_companias.crear_objeto_entidad(compania_dto, existe_compania_en_pais, MapeadorCompania())
        compania.ingestar_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(IngestarCompania)
def ejecutar_comando_ingestar_compania(comando: IngestarCompania):
    handler = IngestarCompaniaHandler()
    handler.handle(comando)