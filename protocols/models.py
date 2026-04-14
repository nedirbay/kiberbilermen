from django.db import models

class ProtocolCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name="Ady")

    class Meta:
        verbose_name = "Protokol kategoriýasy"
        verbose_name_plural = "Protokol kategoriýalary"

    def __str__(self) -> str:
        return self.name


class Protocol(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="Ady")
    category = models.ForeignKey(
        ProtocolCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kategoriýasy",
        related_name="protocols"
    )

    purpose = models.TextField(verbose_name="Maksady")
    how_it_works = models.TextField(verbose_name="Nähili işleýär?")
    real_world_use = models.TextField(blank=True, verbose_name="Amaly ulanylyşy")
    security_notes = models.TextField(blank=True, verbose_name="Howpsuzlyk bellikleri")

    highlight_dns = models.BooleanField(
        default=False,
        help_text="DNS-i sahypada has aýdyň görkezmek üçin işlediň.",
        verbose_name="DNS aýratynlygy"
    )

    class Meta:
        ordering = ["category", "name"]
        verbose_name = "Protokol"
        verbose_name_plural = "Protokollar"

    def __str__(self) -> str:
        return self.name
