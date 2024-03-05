import json
from propiedadalpes.modulos.usuarios.aplicacion.queries.obtener_usuario import ObtenerUsuario
import propiedadalpes.seedwork.presentacion.api as api

from flask import request
from flask import Response
from propiedadalpes.modulos.usuarios.aplicacion.comandos.ingestar_usuario import IngestarUsuario
from propiedadalpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadalpes.seedwork.aplicacion.queries import ejecutar_query
from propiedadalpes.modulos.usuarios.aplicacion.servicios import ServicioUsuario
from propiedadalpes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('gestion_usuarios', '/gestion_usuarios')

@bp.route('/usuarios', methods=('POST',))
def ingestar():
    try:
        usuario_dict = request.json

        sr = ServicioUsuario()
        dto_final = sr.ingestar_usuario(usuario_dict)

        return dto_final
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')