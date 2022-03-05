from django.urls import path
from .api import api

app_name = "core"

urlpatterns = [
    path("notes/", api.urls),
]
