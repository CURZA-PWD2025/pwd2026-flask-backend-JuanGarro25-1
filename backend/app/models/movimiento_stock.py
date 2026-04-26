from app.database import db
from app.models.base_model import BaseModel

class MovimientoStock(BaseModel):
    __tablename__ = "movimientos_stock"

    tipo = db.Column(db.String(10), nullable=False)  # entrada / salida
    cantidad = db.Column(db.Integer, nullable=False)

    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "cantidad": self.cantidad,
            "producto_id": self.producto_id
        }