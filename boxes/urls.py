from django.urls import path

from .views import (
    AddWordView,
    BoxWordView,
    AddBoxView,
    BoxesView,
    WordEditView,
    WordDeleteView,
    ShiftBoxes,
)

app_name = "boxes"
urlpatterns = [
    path("add_word/<int:box_id>/", AddWordView.as_view(), name="add_word"),
    path("box_detail/<int:id>/", BoxWordView.as_view(), name="box_detail"),
    path("add_box/", AddBoxView.as_view(), name="add_box"),
    path("<int:id>/", BoxesView.as_view(), name="boxes_view"),
    path("word/edit/<int:id>/<int:red>/", WordEditView.as_view(), name="edit_word"),
    path("word/delete/<int:id>/", WordDeleteView.as_view(), name="delete_word"),
    path("shift", ShiftBoxes.as_view(), name="shift"),
]