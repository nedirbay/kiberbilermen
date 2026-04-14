from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Attack


def attack_list(request):
    attacks_list = Attack.objects.all()
    attack_type = request.GET.get("type")
    query = request.GET.get("q")

    if attack_type:
        attacks_list = attacks_list.filter(attack_type=attack_type)
    if query:
        attacks_list = attacks_list.filter(name__icontains=query)

    # Pagination: 9 items per page (3x3 grid)
    paginator = Paginator(attacks_list, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "attacks/attack_list.html",
        {
            "page_obj": page_obj,
            "types": Attack.AttackType,
            "selected_type": attack_type or "",
            "q": query or "",
        },
    )


def attack_detail(request, pk: int):
    attack = get_object_or_404(Attack, pk=pk)
    return render(request, "attacks/attack_detail.html", {"attack": attack})
