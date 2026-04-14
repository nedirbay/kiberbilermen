from django.shortcuts import get_object_or_404, render

from .models import Port, PortCategory


def port_list(request):
    ports = Port.objects.all()
    category_id = request.GET.get("category")
    transport = request.GET.get("transport")
    query = request.GET.get("q")

    if category_id:
        ports = ports.filter(category_id=category_id)
    if transport:
        ports = ports.filter(transport=transport)
    if query:
        ports = ports.filter(service_name__icontains=query)

    return render(
        request,
        "ports/port_list.html",
        {
            "ports": ports,
            "categories": PortCategory.objects.all(),
            "transports": Port.Transport,
            "selected_category": category_id or "",
            "selected_transport": transport or "",
            "q": query or "",
        },
    )


def port_detail(request, pk: int):
    port = get_object_or_404(Port, pk=pk)
    return render(request, "ports/port_detail.html", {"port": port})
