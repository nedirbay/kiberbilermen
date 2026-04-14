from django.db import models

class DefenseTool(models.Model):
    class Category(models.TextChoices):
        ANTIVIRUS = "antivirus", "Antivirus"
        FIREWALL = "firewall", "Firewall"
        IDS_IPS = "ids_ips", "IDS/IPS"
        ENCRYPTION = "encryption", "Encryption"
        OTHER = "other", "Other"

    name = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=24, choices=Category.choices)

    why_needed = models.TextField()
    how_it_works = models.TextField()

    class Meta:
        ordering = ["category", "name"]

    def __str__(self) -> str:
        return self.name
