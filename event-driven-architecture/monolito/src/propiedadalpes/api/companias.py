import propiedadalpes.seedwork.presentacion.api as api

from flask import request

bp = api.crear_blueprint('companias', '/companias')

@bp.route('/coleccion', methods=('POST',))
def reservar():
    try:
        reserva_dict = request.json

        map_coleccion = MapeadorReservaDTOJson()
        reserva_dto = map_coleccion.externo_a_dto(reserva_dict)

        sr = ServicioReserva()
        dto_final = sr.crear_reserva(reserva_dto)

        return map_reserva.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/coleccion', methods=('GET',))
@bp.route('/coleccion/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioReserva()
        
        return sr.obtener_reserva_por_id(id)
    else:
        return [{'message': 'GET!'}]