from django.urls import path

from . import views

app_name = "protocols"

urlpatterns = [
    path("", views.protocol_list, name="list"),
    path("<int:pk>/", views.protocol_detail, name="detail"),
]

