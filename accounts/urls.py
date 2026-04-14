from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("me/", views.profile, name="profile"),
    path("me/edit/", views.edit_profile, name="edit"),
    
    # Password Security
    path("password-change/", views.CustomPasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", views.CustomPasswordChangeDoneView.as_view(), name="password_change_done"),
]

