from dataclasses import asdict
from itertools import groupby
from propiedadalpes.modulos.usuarios.dominio.eventos import UsuarioIngestado, EventoUsuario
from propiedadalpes.modulos.usuarios.infraestructura.despachadores import unix_time_millis

from propiedadalpes.seedwork.dominio.repositorios import Mapeador
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from .dto import Usuario as UsuarioDTO

class MapeadorUsuario(Mapeador):
    def obtener_tipo(self) -> type:
        return Usuario.__class__
    
    def dto_a_entidad(self, dto: UsuarioDTO) -> Usuario:
        usuario = Usuario(dto.id)
        usuario.nombre = dto.nombre

        return usuario
    
    def entidad_a_dto(self, entidad: Usuario) -> UsuarioDTO:
        
        usuario_dto = UsuarioDTO()
        usuario_dto.id = str(entidad.id)
        usuario_dto.nombre = entidad.nombre

        return usuario_dto
    
class MapeadorEventosUsuario(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            UsuarioIngestado: self._entidad_a_usuario_ingestado,
        }
    
    def obtener_tipo(self) -> type:
        return EventoUsuario.__class__
    
    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False
    
    def _entidad_a_usuario_ingestado(self, entidad: UsuarioIngestado, version=LATEST_VERSION):
        def v1(evento):
            print("debug evento --> ", evento)
            from .schema.v1.eventos import UsuarioIngestadoPayload, EventoUsuarioIngestado

            payload = UsuarioIngestadoPayload(
                id_usuario=str(evento.id_usuario), 
            )
            evento_integracion = EventoUsuarioIngestado(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'UsuarioIngestado'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'propiedadalpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad) 