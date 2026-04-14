from django.shortcuts import get_object_or_404, render

from .models import DefenseTool


def defense_tool_list(request):
    tools = DefenseTool.objects.all()
    category = request.GET.get("category")
    query = request.GET.get("q")

    if category:
        tools = tools.filter(category=category)
    if query:
        tools = tools.filter(name__icontains=query)

    return render(
        request,
        "defense/defense_tool_list.html",
        {
            "tools": tools,
            "categories": DefenseTool.Category,
            "selected_category": category or "",
            "q": query or "",
        },
    )


def defense_tool_detail(request, pk: int):
    tool = get_object_or_404(DefenseTool, pk=pk)
    return render(request, "defense/defense_tool_detail.html", {"tool": tool})
