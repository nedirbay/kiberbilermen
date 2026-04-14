from django.db import models

from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    class Role(models.TextChoices):
        USER = "user", "Ulanyjy"
        EDITOR = "editor", "Redaktor"
        ADMIN = "admin", "Admin"

    user = models.OneToOneField(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name="profile",
        verbose_name="Ulanyjy"
    )
    role = models.CharField(
        max_length=16, 
        choices=Role.choices, 
        default=Role.USER,
        verbose_name="Roly"
    )
    bio = models.TextField(blank=True, verbose_name="Terjimehaly")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Döredilen wagty")

    class Meta:
        verbose_name = "Ulanyjy profili"
        verbose_name_plural = "Ulanyjy profilleri"

    def __str__(self) -> str:
        return f"{self.user.username} ({self.role})"
