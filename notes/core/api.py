from typing import List

from ninja import Router
from .models import Note
from .schemas import NoteResponseSchema, NoteRequestSchema

router = Router()


@router.get("/", response=List[NoteResponseSchema])
def list_notes(request):
    return Note.objects.order_by("-created_at")


@router.post("/", response=NoteResponseSchema)
def create_note(request, data: NoteRequestSchema):
    return Note.objects.create(**data.dict())
