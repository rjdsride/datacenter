from django.contrib import admin
from datacenter import models

# Register your models here.


@admin.register(models.Cable)
class CableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pontaA",
        "pontaB",
    )
    ordering = ("-id",)
    # list_filter = 'created_date'
    search_fields = "id", "pontaA", "pontaB"
    # list_per_page = int(10),
    list_max_show_all_pages = (200,)
    #   list_editable = 'first_name', 'last_name',
    list_display_links = (
        "id",
        "pontaA",
        "pontaB",
    )


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = "id", "name", "type", "endereco"
    ordering = ("-id",)
    # list_filter = 'created_date'
    search_fields = "id", "name", "type", "endereco"
    # list_per_page = int(10),
    list_max_show_all_pages = (200,)
    #   list_editable = 'first_name', 'last_name',
    list_display_links = "id", "name", "type", "endereco"


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = "id", "type_name"
    ordering = ("-id",)
    # list_filter = 'created_date'
    search_fields = "id", "type_name"
    # list_per_page = int(10),
    list_max_show_all_pages = (200,)
    #   list_editable = 'first_name', 'last_name',
    list_display_links = "id", "type_name"


@admin.register(models.Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = "id", "endereco"
    ordering = ("-id",)
    # list_filter = 'created_date'
    search_fields = "id", "endereco"
    # list_per_page = int(10),
    list_max_show_all_pages = (200,)
    #   list_editable = 'first_name', 'last_name',
    list_display_links = "id", "endereco"


@admin.register(models.Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = "id", "fila", "bastidor", "device"
    ordering = ("-id",)
    # list_filter = 'created_date'
    search_fields = "id", "fila", "bastidor", "device"
    # list_per_page = int(10),
    list_max_show_all_pages = (200,)
    #   list_editable = 'first_name', 'last_name',
    list_display_links = "id", "fila", "bastidor", "device"
