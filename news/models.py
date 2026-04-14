from django.db import models

class NewsItem(models.Model):
    class Category(models.TextChoices):
        ATTACK = "attack", "Hüjüm"
        DATA_BREACH = "data_breach", "Maglumat syzyşmasy"
        AI_SECURITY = "ai_security", "AI howpsuzlygy"
        OTHER = "other", "Başga"

    title = models.CharField(max_length=200, verbose_name="Sözbaşy")
    content = models.TextField(verbose_name="Mazmuny")
    published_at = models.DateField(verbose_name="Çap edilen senesi")
    category = models.CharField(
        max_length=32, 
        choices=Category.choices, 
        default=Category.OTHER,
        verbose_name="Kategoriýasy"
    )
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Surat")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Döredilen wagty")

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "Täzelik"
        verbose_name_plural = "Täzelikler"

    def __str__(self) -> str:
        return self.title
