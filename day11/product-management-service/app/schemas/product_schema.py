from marshmallow import Schema, fields
from marshmallow.validate import Length, Range,OneOf


class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=Length(max=30))
    description = fields.Str(validate =Length(min=20,max=300))
    price = fields.Int(required=True, validate=Range(min=1, max=9999))
    currency = fields.Str(validate=OneOf(['$', '€','₹']))
    stock = fields.Int(required=True, validate=Range(min=1, max=9999))
    active =fields.Str(validate=OneOf(['yes','no']))
    