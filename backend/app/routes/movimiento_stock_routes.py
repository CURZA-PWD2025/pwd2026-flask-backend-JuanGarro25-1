from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.movimiento_stock_controller import MovimientoStockController

movimientos = Blueprint("movimientos", __name__, url_prefix="/movimientos")

@movimientos.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return MovimientoStockController.get_all()

@movimientos.route("/", methods=["POST"])
@jwt_required()
def create():
    return MovimientoStockController.create(request.get_json())