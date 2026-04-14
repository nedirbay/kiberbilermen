from django.contrib import admin

from .models import NewsItem, NewsCategory


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "category")
    list_filter = ("category", "published_at")
    search_fields = ("title",)
