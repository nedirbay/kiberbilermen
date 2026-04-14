from django.contrib import admin

from .models import Protocol, ProtocolCategory


@admin.register(ProtocolCategory)
class ProtocolCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "highlight_dns")
    list_filter = ("category", "highlight_dns")
    search_fields = ("name",)
