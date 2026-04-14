from django.db import models

class HistoryEvent(models.Model):
    year_start = models.PositiveIntegerField(verbose_name="Başlan senesi (ýyl)")
    year_end = models.PositiveIntegerField(blank=True, null=True, verbose_name="Gutarýan senesi (ýyl)")
    title = models.CharField(max_length=128, verbose_name="Sözbaşy")
    description = models.TextField(verbose_name="Mazmuny")
    order = models.PositiveIntegerField(default=0, verbose_name="Tertibi")

    class Meta:
        ordering = ["order", "year_start"]
        verbose_name = "Taryhy waka"
        verbose_name_plural = "Taryhy wakalar"

    def __str__(self) -> str:
        year = str(self.year_start) if self.year_end is None else f"{self.year_start}–{self.year_end}"
        return f"{year}: {self.title}"


class HomeHighlight(models.Model):
    title = models.CharField(max_length=128, verbose_name="Sözbaşy")
    body = models.TextField(verbose_name="Mazmuny")
    order = models.PositiveIntegerField(default=0, verbose_name="Tertibi")

    class Meta:
        ordering = ["order"]
        verbose_name = "Esasy maglumat"
        verbose_name_plural = "Esasy maglumatlar"

    def __str__(self) -> str:
        return self.title
