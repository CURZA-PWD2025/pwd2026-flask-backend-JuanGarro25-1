from app.database import db
from app.models.base_model import BaseModel

class Categoria(BaseModel):
    __tablename__ = "categorias"

    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text)

    productos = db.relationship("Producto", back_populates="categoria")  

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }