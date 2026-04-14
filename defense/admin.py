from django.contrib import admin

from .models import DefenseTool, DefenseCategory


@admin.register(DefenseCategory)
class DefenseCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(DefenseTool)
class DefenseToolAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)
