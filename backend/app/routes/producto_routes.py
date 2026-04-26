from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.producto_controller import ProductoController

productos = Blueprint("productos", __name__, url_prefix="/productos")

@productos.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return ProductoController.get_all()

@productos.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_by_id(id):
    return ProductoController.get_by_id(id)

@productos.route("/", methods=["POST"])
@jwt_required()
def create():
    return ProductoController.create(request.get_json())

@productos.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    return ProductoController.update(id, request.get_json())

@productos.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return ProductoController.delete(id)