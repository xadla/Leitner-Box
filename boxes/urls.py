from django.urls import path

from .views import AddWord

app_name = "boxes"
urlpatterns = [
    path("add/", AddWord.as_view(), name="add"),
]