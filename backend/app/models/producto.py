from app.database import db

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    precio_costo = db.Column(db.Float, nullable=False)
    precio_venta = db.Column(db.Float, nullable=False)
    stock_actual = db.Column(db.Integer, default=0)
    stock_minimo = db.Column(db.Integer, default=0)

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    categoria = db.relationship("Categoria", back_populates="productos")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio_costo": self.precio_costo,
            "precio_venta": self.precio_venta,
            "stock_actual": self.stock_actual,
            "stock_minimo": self.stock_minimo,
            "categoria_id": self.categoria_id
        }