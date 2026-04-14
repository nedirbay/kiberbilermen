from django.db import models

class Port(models.Model):
    class Transport(models.TextChoices):
        TCP = "tcp", "TCP"
        UDP = "udp", "UDP"

    class Category(models.TextChoices):
        WELL_KNOWN = "well_known", "Well-known"
        REGISTERED = "registered", "Registered"
        DYNAMIC_PRIVATE = "dynamic_private", "Dynamic/Private"

    number = models.PositiveIntegerField()
    transport = models.CharField(max_length=16, choices=Transport.choices, default=Transport.TCP)
    service_name = models.CharField(max_length=64)
    category = models.CharField(max_length=32, choices=Category.choices, default=Category.WELL_KNOWN)

    what_it_does = models.TextField()
    where_used = models.TextField(blank=True)
    security_risks = models.TextField(blank=True)

    class Meta:
        ordering = ["number", "transport", "service_name"]
        constraints = [
            models.UniqueConstraint(fields=["number", "transport"], name="unique_port_number_transport")
        ]

    def __str__(self) -> str:
        return f"{self.number}/{self.transport.upper()} - {self.service_name}"
