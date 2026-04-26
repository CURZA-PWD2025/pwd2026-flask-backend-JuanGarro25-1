from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.categoria_controller import CategoriaController

categorias = Blueprint("categorias", __name__, url_prefix="/categorias")

@categorias.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return CategoriaController.get_all()

@categorias.route("/", methods=["POST"])
@jwt_required()
def create():
    return CategoriaController.create(request.get_json())

@categorias.route('/<int:id>', methods=['PUT'])
def update(id):
    return CategoriaController.update(id, request.get_json())

@categorias.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return CategoriaController.delete(id)