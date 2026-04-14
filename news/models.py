from django.db import models

class NewsItem(models.Model):
    class Category(models.TextChoices):
        ATTACK = "attack", "Attack"
        DATA_BREACH = "data_breach", "Data breach"
        AI_SECURITY = "ai_security", "AI security"
        OTHER = "other", "Other"

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateField()
    category = models.CharField(max_length=32, choices=Category.choices, default=Category.OTHER)
    image_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:
        return self.title
