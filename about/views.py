from django.shortcuts import render

from .models import ProjectInfo


def about(request):
    return render(
        request,
        "about/about.html",
        {
            "project": ProjectInfo.objects.first(),
        },
    )
