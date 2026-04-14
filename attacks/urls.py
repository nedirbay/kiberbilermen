from django.urls import path

from . import views

app_name = "attacks"

urlpatterns = [
    path("", views.attack_list, name="list"),
    path("<int:pk>/", views.attack_detail, name="detail"),
]

