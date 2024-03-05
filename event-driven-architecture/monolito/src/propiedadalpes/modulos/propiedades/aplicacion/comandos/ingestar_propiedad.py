from propiedadalpes.modulos.propiedades.aplicacion.comandos.base import IngestarPropiedadBaseHandler
from propiedadalpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadalpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadalpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioEventosPropiedades

from propiedadalpes.seedwork.aplicacion.comandos import Comando
from propiedadalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from dataclasses import dataclass, field

@dataclass
class IngestarPropiedad(Comando):
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)

class IngestarPropiedadHandler(IngestarPropiedadBaseHandler):
    
    def handle(self, comando: IngestarPropiedad):
        propiedad_dto = PropiedadDTO(comando.id, comando.nombre, comando.ubicacion, comando.direccion, comando.ciudad)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades)

        propiedad: Propiedad = self.fabrica_companias.crear_objeto_entidad(propiedad_dto, MapeadorPropiedad())
        propiedad.ingestar_propiedad(propiedad)

        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosPropiedades)        

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad, repositorio_eventos_func=repositorio_eventos.agregar)
        #UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(IngestarPropiedad)
def ejecutar_comando_ingestar_compania(comando: IngestarPropiedad):
    handler = IngestarPropiedadHandler()
    handler.handle(comando)