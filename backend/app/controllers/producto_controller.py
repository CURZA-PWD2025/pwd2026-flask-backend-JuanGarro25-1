from flask import jsonify
from app.database import db
from app.models.producto import Producto

class ProductoController:

    @staticmethod
    def get_all():
        productos = Producto.query.all()
        return jsonify([p.to_dict() for p in productos]), 200

    @staticmethod
    def get_by_id(id):
        producto = Producto.query.get(id)

        if not producto:
            return jsonify({"message": "Producto no encontrado"}), 404

        return jsonify(producto.to_dict()), 200

    @staticmethod
    def create(data):
        producto = Producto(
            nombre=data.get("nombre"),
            precio_costo=data.get("precio_costo"),
            precio_venta=data.get("precio_venta"),
            stock_actual=data.get("stock_actual", 0),
            stock_minimo=data.get("stock_minimo", 0),
            categoria_id=data.get("categoria_id")
        )

        db.session.add(producto)
        db.session.commit()

        return jsonify({"message": "Producto creado"}), 201

    @staticmethod
    def update(id, data):
        producto = Producto.query.get(id)

        if not producto:
            return jsonify({"message": "Producto no encontrado"}), 404

        producto.nombre = data.get("nombre", producto.nombre)
        producto.precio_costo = data.get("precio_costo", producto.precio_costo)
        producto.precio_venta = data.get("precio_venta", producto.precio_venta)
        producto.stock_actual = data.get("stock_actual", producto.stock_actual)
        producto.stock_minimo = data.get("stock_minimo", producto.stock_minimo)
        producto.categoria_id = data.get("categoria_id", producto.categoria_id)

        db.session.commit()

        return jsonify({"message": "Producto actualizado"}), 200

    @staticmethod
    def delete(id):
        producto = Producto.query.get(id)

        if not producto:
            return jsonify({"message": "Producto no encontrado"}), 404

        db.session.delete(producto)
        db.session.commit()

        return jsonify({"message": "Producto eliminado"}), 200