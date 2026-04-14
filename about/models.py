from django.db import models

class ProjectInfo(models.Model):
    goal = models.TextField()
    audience = models.TextField(blank=True)
    author_name = models.CharField(max_length=128, blank=True)
    author_bio = models.TextField(blank=True)
    future_plans = models.TextField(blank=True)

    class Meta:
        verbose_name = "Project info"
        verbose_name_plural = "Project info"

    def __str__(self) -> str:
        return "Project info"
