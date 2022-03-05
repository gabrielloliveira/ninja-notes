from django.urls import path
from ninja import NinjaAPI
from notes.core.api import router as core_router

api = NinjaAPI(
    title="Notes API",
    version="1.0",
    description="A simple notes API",
)

api.add_router("notes/", core_router)

urlpatterns = [
    path("", api.urls),
]
