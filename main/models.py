from django.db import models

class HistoryEvent(models.Model):
    year_start = models.PositiveIntegerField()
    year_end = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "year_start"]

    def __str__(self) -> str:
        year = str(self.year_start) if self.year_end is None else f"{self.year_start}–{self.year_end}"
        return f"{year}: {self.title}"


class HomeHighlight(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title
