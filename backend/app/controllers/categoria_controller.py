from flask import jsonify
from app.database import db
from app.models.categoria import Categoria

class CategoriaController:

    @staticmethod
    def get_all():
        categorias = Categoria.query.all()
        return jsonify([c.to_dict() for c in categorias]), 200

    @staticmethod
    def create(data):
        categoria = Categoria(
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion")
        )

        db.session.add(categoria)
        db.session.commit()

        return jsonify({"message": "Categoría creada"}), 201
    
    @staticmethod
    def update(id, data):
        categoria = Categoria.query.get(id)
        if not categoria:
            return jsonify({"message": "Categoría no encontrada"}), 404

        categoria.nombre = data.get("nombre", categoria.nombre)
        categoria.descripcion = data.get("descripcion", categoria.descripcion)

        db.session.commit()
        return jsonify({"message": "Categoría actualizada"}), 200
    
    @staticmethod
    def delete(id):
        categoria = Categoria.query.get(id)

        if not categoria:
            return jsonify({"message": "Categoría no encontrada"}), 404

        db.session.delete(categoria)
        db.session.commit()

        return jsonify({"message": "Categoría eliminada"}), 200