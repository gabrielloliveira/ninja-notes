from typing import List

from ninja import Router
from ninja.responses import Response

from notes.api.schemas import MessageSchema
from .models import Note
from .schemas import NoteResponseSchema, NoteRequestSchema
from http import HTTPStatus

router = Router()


@router.get("/", response=List[NoteResponseSchema])
def list_notes(request):
    return Note.objects.order_by("-created_at")


@router.post("/", response=NoteResponseSchema)
def create_note(request, data: NoteRequestSchema):
    return Note.objects.create(**data.dict())


@router.get("/{uuid}", response={HTTPStatus.OK: NoteResponseSchema, HTTPStatus.NOT_FOUND: MessageSchema})
def get_note(request, uuid: str):
    try:
        return Note.objects.get(uuid=uuid)
    except Note.DoesNotExist:
        data = dict(type="error", message="Note not found")
        return Response(data, status=HTTPStatus.NOT_FOUND)
