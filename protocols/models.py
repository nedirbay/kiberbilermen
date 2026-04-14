from django.db import models

class Protocol(models.Model):
    class Category(models.TextChoices):
        TRANSPORT = "transport", "Transport"
        APPLICATION = "application", "Application"
        NETWORK = "network", "Network"

    name = models.CharField(max_length=32, unique=True)
    category = models.CharField(max_length=32, choices=Category.choices)

    purpose = models.TextField()
    how_it_works = models.TextField()
    real_world_use = models.TextField(blank=True)
    security_notes = models.TextField(blank=True)

    highlight_dns = models.BooleanField(
        default=False,
        help_text="Enable for DNS to show extra emphasis on the page.",
    )

    class Meta:
        ordering = ["category", "name"]

    def __str__(self) -> str:
        return self.name
