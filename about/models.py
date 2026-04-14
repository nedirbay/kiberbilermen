from django.db import models

class ProjectInfo(models.Model):
    goal = models.TextField(verbose_name="Maksady")
    audience = models.TextField(blank=True, verbose_name="Diňleýjiler (Auditoriýa)")
    author_name = models.CharField(max_length=128, blank=True, verbose_name="Awtoryň ady")
    author_bio = models.TextField(blank=True, verbose_name="Awtor barada maglumat")
    future_plans = models.TextField(blank=True, verbose_name="Gelejekki meýiller")

    class Meta:
        verbose_name = "Taslama maglumaty"
        verbose_name_plural = "Taslama maglumatlary"

    def __str__(self) -> str:
        return "Project info"
