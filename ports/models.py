from django.db import models

class Port(models.Model):
    class Transport(models.TextChoices):
        TCP = "tcp", "TCP"
        UDP = "udp", "UDP"

    class Category(models.TextChoices):
        WELL_KNOWN = "well_known", "Meşhur (Well-known)"
        REGISTERED = "registered", "Hasaba alnan (Registered)"
        DYNAMIC_PRIVATE = "dynamic_private", "Dinamyk/Hususy"

    number = models.PositiveIntegerField(verbose_name="Port belgisi")
    transport = models.CharField(
        max_length=16, 
        choices=Transport.choices, 
        default=Transport.TCP,
        verbose_name="Ulag protokoly"
    )
    service_name = models.CharField(max_length=64, verbose_name="Hyzmatyň ady")
    category = models.CharField(
        max_length=32, 
        choices=Category.choices, 
        default=Category.WELL_KNOWN,
        verbose_name="Kategoriýasy"
    )

    what_it_does = models.TextField(verbose_name="Bu näme?")
    where_used = models.TextField(blank=True, verbose_name="Nirede ulanylýar?")
    security_risks = models.TextField(blank=True, verbose_name="Howpsuzlyk töwekgelçilikleri")

    class Meta:
        ordering = ["number", "transport", "service_name"]
        verbose_name = "Port"
        verbose_name_plural = "Portlar"
        constraints = [
            models.UniqueConstraint(fields=["number", "transport"], name="unique_port_number_transport")
        ]

    def __str__(self) -> str:
        return f"{self.number}/{self.transport.upper()} - {self.service_name}"
