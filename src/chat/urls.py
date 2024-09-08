from django.urls import path
from chat.views import lobby

urlpatterns = [
    path("", lobby, name="lobby"),
]
