from django.db import models

class Attack(models.Model):
    class AttackType(models.TextChoices):
        PHISHING = "phishing", "Fişing"
        DDOS = "ddos", "DDoS hüjümi"
        MALWARE = "malware", "Zyýanly programma"
        MITM = "mitm", "Aralygyndaky adam (MITM)"
        OTHER = "other", "Başga"

    name = models.CharField(max_length=64, verbose_name="Ady")
    attack_type = models.CharField(
        max_length=24, 
        choices=AttackType.choices, 
        default=AttackType.OTHER,
        verbose_name="Görnüşi"
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
