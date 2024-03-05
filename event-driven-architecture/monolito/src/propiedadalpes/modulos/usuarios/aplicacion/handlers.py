from propiedadalpes.modulos.usuarios.dominio.eventos import UsuarioIngestado
from propiedadalpes.seedwork.aplicacion.handlers import Handler
from propiedadalpes.modulos.usuarios.infraestructura.despachadores import Despachador

class HandlerUsuarioIntegracion(Handler):

    @staticmethod
    def handle_usuario_ingestado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-usuario')
