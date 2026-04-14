from django.contrib import admin

from .models import Attack


@admin.register(Attack)
class AttackAdmin(admin.ModelAdmin):
    list_display = ("name", "attack_type")
    list_filter = ("attack_type",)
    search_fields = ("name",)
