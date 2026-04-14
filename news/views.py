from django.shortcuts import get_object_or_404, render

from .models import NewsItem


def news_list(request):
    items = NewsItem.objects.all()
    category = request.GET.get("category")
    query = request.GET.get("q")

    if category:
        items = items.filter(category=category)
    if query:
        items = items.filter(title__icontains=query)

    return render(
        request,
        "news/news_list.html",
        {
            "items": items,
            "categories": NewsItem.Category,
            "selected_category": category or "",
            "q": query or "",
        },
    )


def news_detail(request, pk: int):
    item = get_object_or_404(NewsItem, pk=pk)
    return render(request, "news/news_detail.html", {"item": item})
