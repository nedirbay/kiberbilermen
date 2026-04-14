from django.db import models

class PortCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name="Ady")

    class Meta:
        verbose_name = "Port kategoriýasy"
        verbose_name_plural = "Port kategoriýalary"

    def __str__(self) -> str:
        return self.name


class Port(models.Model):
    class Transport(models.TextChoices):
        TCP = "tcp", "TCP"
        UDP = "udp", "UDP"

    number = models.PositiveIntegerField(verbose_name="Port belgisi")
    transport = models.CharField(
        max_length=16, 
        choices=Transport.choices, 
        default=Transport.TCP,
        verbose_name="Ulag protokoly"
    )
    service_name = models.CharField(max_length=64, verbose_name="Hyzmatyň ady")
    category = models.ForeignKey(
        PortCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kategoriýasy",
        related_name="ports"
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
