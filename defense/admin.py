from django.contrib import admin

from .models import DefenseTool


@admin.register(DefenseTool)
class DefenseToolAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)
