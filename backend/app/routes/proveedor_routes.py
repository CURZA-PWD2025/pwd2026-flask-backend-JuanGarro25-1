from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.proveedor_controller import ProveedorController

proveedores = Blueprint("proveedores", __name__, url_prefix="/proveedores")

@proveedores.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return ProveedorController.get_all()

@proveedores.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_by_id(id):
    return ProveedorController.get_by_id(id)

@proveedores.route("/", methods=["POST"])
@jwt_required()
def create():
    return ProveedorController.create(request.get_json())

@proveedores.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    return ProveedorController.update(id, request.get_json())

@proveedores.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return ProveedorController.delete(id)