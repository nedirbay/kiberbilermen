from django.db import models

class DefenseCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name="Ady")

    class Meta:
        verbose_name = "Goranyş kategoriýasy"
        verbose_name_plural = "Goranyş kategoriýalary"

    def __str__(self) -> str:
        return self.name


class DefenseTool(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Ady")
    category = models.ForeignKey(
        DefenseCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kategoriýasy",
        related_name="tools"
    )

    why_needed = models.TextField(verbose_name="Näme üçin gerek?")
    how_it_works = models.TextField(verbose_name="Nähili işleýär?")
    image = models.ImageField(upload_to='defense/', blank=True, null=True, verbose_name="Surat")

    class Meta:
        ordering = ["category", "name"]
        verbose_name = "Goranyş guraly"
        verbose_name_plural = "Goranyş gurallary"

    def __str__(self) -> str:
        return self.name
