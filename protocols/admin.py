from django.contrib import admin

from .models import Protocol


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "highlight_dns")
    list_filter = ("category", "highlight_dns")
    search_fields = ("name",)
