from django.shortcuts import get_object_or_404, render

from .models import Attack


def attack_list(request):
    attacks = Attack.objects.all()
    attack_type = request.GET.get("type")
    query = request.GET.get("q")

    if attack_type:
        attacks = attacks.filter(attack_type=attack_type)
    if query:
        attacks = attacks.filter(name__icontains=query)

    return render(
        request,
        "attacks/attack_list.html",
        {
            "attacks": attacks,
            "types": Attack.AttackType,
            "selected_type": attack_type or "",
            "q": query or "",
        },
    )


def attack_detail(request, pk: int):
    attack = get_object_or_404(Attack, pk=pk)
    return render(request, "attacks/attack_detail.html", {"attack": attack})
