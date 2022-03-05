from django.contrib import admin

from notes.core.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("title", "content")
