from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name="Ady")

    class Meta:
        verbose_name = "Täzelik kategoriýasy"
        verbose_name_plural = "Täzelik kategoriýalary"

    def __str__(self) -> str:
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sözbaşy")
    content = models.TextField(verbose_name="Mazmuny")
    published_at = models.DateField(verbose_name="Çap edilen senesi")
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kategoriýasy",
        related_name="news"
    )
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Surat")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Döredilen wagty")

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "Täzelik"
        verbose_name_plural = "Täzelikler"

    def __str__(self) -> str:
        return self.title
