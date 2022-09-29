from app import db
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'UMS_PRODUCT'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    price = db.Column(db.Integer)
    
    
    def __init__(self, id, name, description, price,currency,stock,active) :
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.currency = currency
        self.stock = stock
        self.active = active
             
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'role': self.role,
                    }

    @staticmethod
    def from_json(json_dct):
      return User(
        json_dct.get('id'), 
        json_dct['name'], 
        json_dct['description'], 
        json_dct['price'], 
      )