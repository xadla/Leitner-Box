from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("boxes/", include("boxes.urls", namespace="boxes")),
    path("", include("pages.urls", namespace="pages")),
]
