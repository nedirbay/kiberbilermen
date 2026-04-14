from django.db import models

class DefenseTool(models.Model):
    class Category(models.TextChoices):
        ANTIVIRUS = "antivirus", "Antiwirus"
        FIREWALL = "firewall", "Brandmauer (Firewall)"
        IDS_IPS = "ids_ips", "IDS/IPS"
        ENCRYPTION = "encryption", "Şifrlemek"
        OTHER = "other", "Başga"

    name = models.CharField(max_length=64, unique=True, verbose_name="Ady")
    category = models.CharField(max_length=24, choices=Category.choices, verbose_name="Kategoriýasy")

    why_needed = models.TextField(verbose_name="Näme üçin gerek?")
    how_it_works = models.TextField(verbose_name="Nähili işleýär?")
    image = models.ImageField(upload_to='defense/', blank=True, null=True, verbose_name="Surat")

    class Meta:
        ordering = ["category", "name"]
        verbose_name = "Goranyş guraly"
        verbose_name_plural = "Goranyş gurallary"

    def __str__(self) -> str:
        return self.name
