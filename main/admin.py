from django.contrib import admin

from .models import HistoryEvent, HomeHighlight


@admin.register(HistoryEvent)
class HistoryEventAdmin(admin.ModelAdmin):
    list_display = ("title", "year_start", "year_end", "order")
    list_editable = ("order",)


@admin.register(HomeHighlight)
class HomeHighlightAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
