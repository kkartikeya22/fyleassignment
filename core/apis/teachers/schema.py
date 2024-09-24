from marshmallow import Schema, fields

class TeacherSchema(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    user_id = fields.Int()
