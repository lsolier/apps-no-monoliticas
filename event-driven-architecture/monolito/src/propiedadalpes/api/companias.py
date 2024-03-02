import json
import propiedadalpes.seedwork.presentacion.api as api

from flask import request
from flask import Response
from propiedadalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from propiedadalpes.modulos.companias.aplicacion.servicios import ServicioCompania
from propiedadalpes.seedwork.dominio.excepciones import ExcepcionDominio


bp = api.crear_blueprint('colecciones', '/colecciones')

@bp.route('/compania', methods=('POST',))
def ingestar():
    try:
        compania_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)

        sr = ServicioCompania()
        dto_final = sr.ingestar_compania(compania_dto)

        return map_compania.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/compania', methods=('GET',))
@bp.route('/compania/<id>', methods=('GET',))
def dar_compania(id=None):
    if id:
        sr = ServicioCompania()
        
        return sr.obtener_compania_por_id(id)
    else:
        return [{'message': 'GET!'}]