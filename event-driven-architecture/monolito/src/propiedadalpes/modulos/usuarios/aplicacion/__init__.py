from pydispatch import dispatcher

from .handlers import HandlerUsuarioIntegracion

from propiedadalpes.modulos.usuarios.dominio.eventos import UsuarioIngestado

dispatcher.connect(HandlerUsuarioIntegracion.handle_usuario_ingestado, signal=f'{UsuarioIngestado.__name__}Integracion')