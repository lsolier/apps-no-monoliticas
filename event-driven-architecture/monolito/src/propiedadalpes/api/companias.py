import json
from propiedadalpes.modulos.companias.aplicacion.queries.obtener_compania import ObtenerCompania
import propiedadalpes.seedwork.presentacion.api as api

from flask import request
from flask import Response
from propiedadalpes.modulos.companias.aplicacion.comandos.ingestar_compania import IngestarCompania
from propiedadalpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadalpes.seedwork.aplicacion.queries import ejecutar_query
from propiedadalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from propiedadalpes.modulos.companias.aplicacion.servicios import ServicioCompania
from propiedadalpes.seedwork.dominio.excepciones import ExcepcionDominio


bp = api.crear_blueprint('colecciones', '/colecciones')

@bp.route('/companias', methods=('POST',))
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
    
@bp.route('/companias-comando', methods=('POST',))
def ingestar_asincrono():
    try:
        compania_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)

        comando = IngestarCompania(compania_dto.fecha_creacion, compania_dto.fecha_actualizacion, compania_dto.id, 
                                   compania_dto.nombre, compania_dto.numero_identificacion, compania_dto.codigo_iso_pais, 
                                   compania_dto.contactos, compania_dto.sucursales)

        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/companias', methods=('GET',))
@bp.route('/companias/<id>', methods=('GET',))
def dar_compania(id=None):
    if id:
        map_compania = MapeadorCompaniaDTOJson()
        sr = ServicioCompania()
        
        dto_final = sr.obtener_compania_por_id(id)
        return map_compania.dto_a_externo(dto_final)
    else:
        return [{'message': 'GET!'}]
    
@bp.route('/companias-query', methods=('GET',))
@bp.route('/companias-query/<id>', methods=('GET',))
def dar_compania_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCompania(id))
        map_compania = MapeadorCompaniaDTOJson()
        
        return map_compania.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]