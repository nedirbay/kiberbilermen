from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import NewsItem, NewsCategory


def news_list(request):
    items_list = NewsItem.objects.all().order_by("-published_at")
    category_id = request.GET.get("category")
    query = request.GET.get("q")

    if category_id:
        items_list = items_list.filter(category_id=category_id)
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
            "categories": NewsCategory.objects.all(),
            "selected_category": category_id or "",
            "q": query or "",
        },
    )


def news_detail(request, pk: int):
    item = get_object_or_404(NewsItem, pk=pk)
    return render(request, "news/news_detail.html", {"item": item})
