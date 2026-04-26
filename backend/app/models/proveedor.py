from app.database import db
from app.models.base_model import BaseModel

class Proveedor(BaseModel):
    __tablename__ = "proveedores"

    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono
        }