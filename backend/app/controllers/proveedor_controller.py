from flask import jsonify
from app.database import db
from app.models.proveedor import Proveedor

class ProveedorController:

    @staticmethod
    def get_all():
        proveedores = Proveedor.query.all()
        return jsonify([p.to_dict() for p in proveedores]), 200

    @staticmethod
    def get_by_id(id):
        proveedor = Proveedor.query.get(id)

        if not proveedor:
            return jsonify({"message": "Proveedor no encontrado"}), 404

        return jsonify(proveedor.to_dict()), 200

    @staticmethod
    def create(data):
        proveedor = Proveedor(
            nombre=data.get("nombre"),
            email=data.get("email"),
            telefono=data.get("telefono")
        )

        db.session.add(proveedor)
        db.session.commit()

        return jsonify({"message": "Proveedor creado"}), 201

    @staticmethod
    def update(id, data):
        proveedor = Proveedor.query.get(id)

        if not proveedor:
            return jsonify({"message": "Proveedor no encontrado"}), 404

        proveedor.nombre = data.get("nombre", proveedor.nombre)
        proveedor.email = data.get("email", proveedor.email)
        proveedor.telefono = data.get("telefono", proveedor.telefono)

        db.session.commit()

        return jsonify({"message": "Proveedor actualizado"}), 200

    @staticmethod
    def delete(id):
        proveedor = Proveedor.query.get(id)

        if not proveedor:
            return jsonify({"message": "Proveedor no encontrado"}), 404

        db.session.delete(proveedor)
        db.session.commit()

        return jsonify({"message": "Proveedor eliminado"}), 200