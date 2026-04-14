from django.shortcuts import get_object_or_404, render

from .models import Protocol


def protocol_list(request):
    protocols = Protocol.objects.all()
    category = request.GET.get("category")
    query = request.GET.get("q")

    if category:
        protocols = protocols.filter(category=category)
    if query:
        protocols = protocols.filter(name__icontains=query)

    return render(
        request,
        "protocols/protocol_list.html",
        {
            "protocols": protocols,
            "categories": Protocol.Category,
            "selected_category": category or "",
            "q": query or "",
        },
    )


def protocol_detail(request, pk: int):
    protocol = get_object_or_404(Protocol, pk=pk)
    return render(request, "protocols/protocol_detail.html", {"protocol": protocol})
