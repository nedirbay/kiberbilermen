from django.db import models

class AttackCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name="Ady")

    class Meta:
        verbose_name = "Hüjüm kategoriýasy"
        verbose_name_plural = "Hüjüm kategoriýalary"

    def __str__(self) -> str:
        return self.name


class Attack(models.Model):
    name = models.CharField(max_length=64, verbose_name="Ady")
    attack_type = models.ForeignKey(
        AttackCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kategoriýasy",
        related_name="attacks"
    )

    what_it_does = models.TextField(verbose_name="Bu näme?")
    how_it_works = models.TextField(verbose_name="Nähili işleýär?")
    goal = models.TextField(blank=True, verbose_name="Maksady")
    example = models.TextField(blank=True, verbose_name="Mysal")
    prevention = models.TextField(blank=True, verbose_name="Goranyş")
    image = models.ImageField(upload_to='attacks/', blank=True, null=True, verbose_name="Surat")

    class Meta:
        ordering = ["attack_type", "name"]
        verbose_name = "Hüjüm"
        verbose_name_plural = "Hüjümler"

    def __str__(self) -> str:
        return self.name
