from django.shortcuts import get_object_or_404, render

from .models import Port


def port_list(request):
    ports = Port.objects.all()
    category = request.GET.get("category")
    transport = request.GET.get("transport")
    query = request.GET.get("q")

    if category:
        ports = ports.filter(category=category)
    if transport:
        ports = ports.filter(transport=transport)
    if query:
        ports = ports.filter(service_name__icontains=query)

    return render(
        request,
        "ports/port_list.html",
        {
            "ports": ports,
            "categories": Port.Category,
            "transports": Port.Transport,
            "selected_category": category or "",
            "selected_transport": transport or "",
            "q": query or "",
        },
    )


def port_detail(request, pk: int):
    port = get_object_or_404(Port, pk=pk)
    return render(request, "ports/port_detail.html", {"port": port})
