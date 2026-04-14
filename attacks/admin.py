from django.contrib import admin

from .models import Attack, AttackCategory


@admin.register(AttackCategory)
class AttackCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Attack)
class AttackAdmin(admin.ModelAdmin):
    list_display = ("name", "attack_type")
    list_filter = ("attack_type",)
    search_fields = ("name",)
