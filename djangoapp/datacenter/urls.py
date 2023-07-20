from django.urls import path
from datacenter import views

app_name = "datacenter"

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    # contact (CRUD)
    path("cable/<int:cable_id>/", views.cable, name="cable"),
    path("cable/create/", views.create, name="create"),
]
