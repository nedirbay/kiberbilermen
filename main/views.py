from django.shortcuts import render

from .models import HistoryEvent, HomeHighlight


def home(request):
    return render(
        request,
        "main/home.html",
        {
            "highlights": HomeHighlight.objects.all(),
            "history_events": HistoryEvent.objects.all(),
        },
    )
