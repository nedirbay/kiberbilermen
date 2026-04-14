from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import NewsItem


def news_list(request):
    items_list = NewsItem.objects.all().order_by("-published_at")
    category = request.GET.get("category")
    query = request.GET.get("q")

    if category:
        items_list = items_list.filter(category=category)
    if query:
        items_list = items_list.filter(title__icontains=query)

    # Pagination: 9 items per page (3x3 grid)
    paginator = Paginator(items_list, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "news/news_list.html",
        {
            "page_obj": page_obj,
            "categories": NewsItem.Category,
            "selected_category": category or "",
            "q": query or "",
        },
    )


def news_detail(request, pk: int):
    item = get_object_or_404(NewsItem, pk=pk)
    return render(request, "news/news_detail.html", {"item": item})
