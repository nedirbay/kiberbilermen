from django.db import models

from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    class Role(models.TextChoices):
        USER = "user", "User"
        EDITOR = "editor", "Editor"
        ADMIN = "admin", "Admin"

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=16, choices=Role.choices, default=Role.USER)
    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} ({self.role})"
