from flask import jsonify
from app.database import db
from app.models.movimiento_stock import MovimientoStock
from app.models.producto import Producto

class MovimientoStockController:

    @staticmethod
    def create(data):
        producto = Producto.query.get(data.get("producto_id"))

        if not producto:
            return {"message": "Producto no encontrado"}, 404

        tipo = data.get("tipo")
        cantidad = data.get("cantidad")

        if tipo == "entrada":
            producto.stock_actual += cantidad

        elif tipo == "salida":
            if producto.stock_actual < cantidad:
                return {"message": "Stock insuficiente"}, 400
            producto.stock_actual -= cantidad

        else:
            return {"message": "Tipo inválido"}, 400

        movimiento = MovimientoStock(
            tipo=tipo,
            cantidad=cantidad,
            producto_id=producto.id
        )

        db.session.add(movimiento)
        db.session.commit()

        return {"message": "Movimiento registrado"}, 201

    @staticmethod
    def get_all():
        movimientos = MovimientoStock.query.all()
        return jsonify([m.to_dict() for m in movimientos]), 200