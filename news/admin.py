from django.contrib import admin

from .models import NewsItem


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "category")
    list_filter = ("category", "published_at")
    search_fields = ("title",)
