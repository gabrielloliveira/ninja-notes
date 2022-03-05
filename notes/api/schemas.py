from ninja import Schema


class MessageSchema(Schema):
    type = str
    message = str
