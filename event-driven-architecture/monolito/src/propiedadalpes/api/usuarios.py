import json
from propiedadalpes.modulos.usuarios.aplicacion.queries.obtener_usuario import ObtenerUsuario
import propiedadalpes.seedwork.presentacion.api as api

from flask import request
from flask import Response
from propiedadalpes.modulos.usuarios.aplicacion.comandos.ingestar_usuario import IngestarUsuario
from propiedadalpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadalpes.seedwork.aplicacion.queries import ejecutar_query
from propiedadalpes.modulos.usuarios.aplicacion.mapeadores import MapeadorUsuarioDTOJson
from propiedadalpes.modulos.usuarios.aplicacion.servicios import ServicioUsuario
from propiedadalpes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('gestion_usuarios', '/gestion_usuarios')

@bp.route('/usuarios', methods=('POST',))
def ingestar():
    try:
        usuario_dict = request.json

        map_usuario = MapeadorUsuarioDTOJson()
        usuario_dto = map_usuario.externo_a_dto(usuario_dict)

        sr = ServicioUsuario()
        dto_final = sr.ingestar_usuario(usuario_dto)

        return map_usuario.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/usuarios', methods=('GET',))
@bp.route('/usuarios/<id>', methods=('GET',))
def dar_usuario(id=None):
    if id:
        map_usuario = MapeadorUsuarioDTOJson()
        sr = ServicioUsuario()
        
        dto_final = sr.obtener_usuario_por_id(id)
        return map_usuario.dto_a_externo(dto_final)
    else:
        return [{'message': 'GET!'}]