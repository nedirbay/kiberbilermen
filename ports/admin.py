from django.contrib import admin

from .models import Port


@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ("number", "transport", "service_name", "category")
    list_filter = ("transport", "category")
    search_fields = ("service_name", "number")
