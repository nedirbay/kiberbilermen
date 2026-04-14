from django.db import models

class Attack(models.Model):
    class AttackType(models.TextChoices):
        PHISHING = "phishing", "Phishing"
        DDOS = "ddos", "DDoS"
        MALWARE = "malware", "Malware"
        MITM = "mitm", "Man-in-the-middle"
        OTHER = "other", "Other"

    name = models.CharField(max_length=64)
    attack_type = models.CharField(max_length=24, choices=AttackType.choices, default=AttackType.OTHER)

    what_it_does = models.TextField()
    how_it_works = models.TextField()
    goal = models.TextField(blank=True)
    example = models.TextField(blank=True)
    prevention = models.TextField(blank=True)

    class Meta:
        ordering = ["attack_type", "name"]

    def __str__(self) -> str:
        return self.name
