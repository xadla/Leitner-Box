from django.urls import path

from .views import (
    AddWord,
    AddBox,
    BoxesView,
)

app_name = "boxes"
urlpatterns = [
    path("add_word/", AddWord.as_view(), name="add_word"),
    path("add_box/", AddBox.as_view(), name="add_box"),
    path("", BoxesView.as_view(), name="boxes_view"),
]