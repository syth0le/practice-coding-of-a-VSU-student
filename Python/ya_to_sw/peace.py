import flask
from flask import jsonify, request, make_response
from . import db_session
from .couriers import Couriers
from .orders import Orders
from .tools import time_check
import json


blueprint = flask.Blueprint(
    'couriers_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/couriers', methods=['POST'])
def post_couriers():
    id_error_list = []
    id_list = []
    couriers_list = []
    db_sess = db_session.create_session()
    for curier in request.json['data']:
        try:
            if curier['regions'] == [] or curier['working_hours'] == []:
                raise Exception
            if db_sess.query(Couriers).get(curier['courier_id']) is not None:
                raise Exception
            couriers = Couriers(
                courier_id=curier['courier_id'],
                courier_type=curier['courier_type'],
                regions=json.dumps(curier['regions']),
                working_hours=json.dumps(curier['working_hours']),
                orders_ids=json.dumps([])
            )
            id_list.append({'id': curier['courier_id']})
            couriers_list.append(couriers)
        except:
            id_error_list.append({'id': curier['courier_id']})
    try:
        if id_error_list:
            raise Exception
        db_sess.add_all(couriers_list)
        db_sess.commit()
        return make_response(jsonify({'success': 'HTTP 201 Created',
                                      "couriers": id_list
                                      }), 200)
    except:
        return make_response(jsonify({'error': 'HTTP 400 Bad Request',
                                      "validation_error": {
                                        "couriers": id_error_list
                                      }}), 400)


@blueprint.route('/couriers/<int:courier_id>', methods=['PATCH'])
def patch_courier(courier_id):
    db_sess = db_session.create_session()
    try:
        couriers = db_sess.query(Couriers).get(courier_id)
        for key in request.json.keys():
            couriers[key] = request.json[key]
        for order in couriers.orders:
            if couriers.weight() < order.weight:
                order.is_available = True
                order.courier_id = None
                orders_id_list = json.loads(couriers.orders_ids)
                orders_id_list.remove(order.order_id)
                couriers.orders_ids = json.dumps(orders_id_list)
        db_sess.commit()
        return make_response(jsonify({'success': 'HTTP 200 OK',
                                      "courier_id": couriers.courier_id,
                                      "courier_type": couriers.courier_type,
                                      "regions": couriers.regions,
                                      "working_hours": couriers.working_hours
                                      }), 200)
    except:
        return make_response(jsonify({'error': 'HTTP 400 Bad Request'}), 400)


@blueprint.route('/orders', methods=['POST'])
def post_orders():
    id_error_list = []
    id_list = []
    orders_list = []
    db_sess = db_session.create_session()
    for order in request.json['data']:
        try:
            if order['delivery_hours'] == []:
                raise Exception
            if db_sess.query(Orders).get(order['order_id']) is not None:
                raise Exception
            orders = Orders(
                order_id=order['order_id'],
                weight=order['weight'],
                region=order['region'],
                delivery_hours=json.dumps(order['delivery_hours']),
                is_available=True,
            )
            id_list.append({'id': order['order_id']})
            orders_list.append(orders)
        except:
            id_error_list.append({'id': order['order_id']})
    try:
        if id_error_list:
            raise Exception
        db_sess.add_all(orders_list)
        db_sess.commit()
        return make_response(jsonify({'success': 'HTTP 201 Created',
                                      "couriers": id_list
                                      }), 200)
    except:
        return make_response(jsonify({'error': 'HTTP 400 Bad Request',
                                      "validation_error": {
                                        "couriers": id_error_list
                                      }}), 400)


@blueprint.route('/orders/assign', methods=['POST'])
def assign_orders():
    try:
        order_list = []
        success_order_list = []
        id = request.json['courier_id']
        db_sess = db_session.create_session()
        courier = db_sess.query(Couriers).get(id)
        for order in db_sess.query(Orders).filter(Orders.region.in_ (courier.regions),
                                                  Orders.weight <= courier.weight(), Orders.is_available):
            if time_check():
                order.is_available = False
                order.courier_id = courier.courier_id
                order_list.append(order.order_id)
                success_order_list.append({'id': order.order_id})
        if not order_list:
            raise Exception
        courier.orders_ids = json.dumps(json.loads(courier.orders_ids) + order_list)
        db_sess.commit()
        return make_response(jsonify({'success': 'HTTP 200 OK',
                                      "orders": success_order_list
                                     }), 200)
    except:
        return make_response(jsonify({'error':'HTTP 400 Bad Request'}), 400)
