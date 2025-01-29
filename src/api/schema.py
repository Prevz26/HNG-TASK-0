from .extensions import ma
from marshmallow import fields

class Response(ma.Schema):
    email = fields.Email()
    current_datetime = fields.String()
    github_url = fields.String()

response = Response()