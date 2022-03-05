from ninja import ModelSchema, Schema

from notes.core.models import Note


class NoteRequestSchema(ModelSchema):
    class Config:
        model = Note
        model_fields = ("title", "content")


class NoteResponseSchema(ModelSchema):
    class Config:
        model = Note
        model_fields = (
            "uuid",
            "created_at",
            "updated_at",
            "title",
            "content",
        )
