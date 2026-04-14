from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import DefenseTool, DefenseCategory


def defense_tool_list(request):
    tools_list = DefenseTool.objects.all()
    category_id = request.GET.get("category")
    query = request.GET.get("q")

    if category_id:
        tools_list = tools_list.filter(category_id=category_id)
    if query:
        tools_list = tools_list.filter(name__icontains=query)

    # Pagination: 9 items per page (3x3 grid)
    paginator = Paginator(tools_list, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "defense/defense_tool_list.html",
        {
            "page_obj": page_obj,
            "categories": DefenseCategory.objects.all(),
            "selected_category": category_id or "",
            "q": query or "",
        },
    )


def defense_tool_detail(request, pk: int):
    tool = get_object_or_404(DefenseTool, pk=pk)
    return render(request, "defense/defense_tool_detail.html", {"tool": tool})
