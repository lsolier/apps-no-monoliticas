import json
from propiedadalpes.modulos.propiedades.aplicacion.querys.obtener_propiedad import ObtenerPropiedad
import propiedadalpes.seedwork.presentacion.api as api

from flask import request
from flask import Response
from propiedadalpes.modulos.propiedades.aplicacion.comandos.ingestar_propiedad import IngestarPropiedad
from propiedadalpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadalpes.seedwork.aplicacion.queries import ejecutar_query
from propiedadalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedadalpes.modulos.propiedades.aplicacion.servicios import ServicioCompania
from propiedadalpes.seedwork.dominio.excepciones import ExcepcionDominio


bp = api.crear_blueprint('gestion_propiedades', '/gestion_propiedades')

@bp.route('/propiedades', methods=('POST',))
def ingestar():
    try:
        compania_dict = request.json

        map_compania = MapeadorPropiedadDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)

        sr = ServicioCompania()
        dto_final = sr.ingestar_propiedad(compania_dto)

        return map_compania.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/propiedad-comando', methods=('POST',))
def ingestar_asincrono():
    try:
        compania_dict = request.json

        map_compania = MapeadorPropiedadDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)

        comando = IngestarPropiedad(compania_dto.fecha_creacion, compania_dto.fecha_actualizacion, compania_dto.id, 
                                   compania_dto.nombre, compania_dto.numero_identificacion, compania_dto.codigo_iso_pais, 
                                   compania_dto.contactos, compania_dto.sucursales)

        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/obtener_propiedades', methods=('GET',))
@bp.route('/obtener_propiedades/<id>', methods=('GET',))
def dar_compania(id=None):
    if id:
        map_compania = MapeadorPropiedadDTOJson()
        sr = ServicioCompania()
        
        dto_final = sr.obtener_compania_por_id(id)
        return map_compania.dto_a_externo(dto_final)
    else:
        return [{'message': 'GET!'}]
    
@bp.route('/propiedades-query', methods=('GET',))
@bp.route('/propiedades-query/<id>', methods=('GET',))
def dar_compania_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedad(id))
        map_compania = MapeadorPropiedadDTOJson()
        
        return map_compania.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]