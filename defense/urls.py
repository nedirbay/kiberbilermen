from django.urls import path

from . import views

app_name = "defense"

urlpatterns = [
    path("", views.defense_tool_list, name="list"),
    path("<int:pk>/", views.defense_tool_detail, name="detail"),
]

