from django.shortcuts import get_object_or_404, render

from .models import Protocol, ProtocolCategory


def protocol_list(request):
    protocols = Protocol.objects.all()
    category_id = request.GET.get("category")
    query = request.GET.get("q")

    if category_id:
        protocols = protocols.filter(category_id=category_id)
    if query:
        protocols = protocols.filter(name__icontains=query)

    return render(
        request,
        "protocols/protocol_list.html",
        {
            "protocols": protocols,
            "categories": ProtocolCategory.objects.all(),
            "selected_category": category_id or "",
            "q": query or "",
        },
    )


def protocol_detail(request, pk: int):
    protocol = get_object_or_404(Protocol, pk=pk)
    return render(request, "protocols/protocol_detail.html", {"protocol": protocol})
