from django.db import models

from apps.core.models import DateTimeModel


class BridalExpert(DateTimeModel):
    designation = models.CharField("Bridal Expert Designation", max_length=50)
    name = models.CharField("Bridal Expert Name", max_length=50)
    description = models.TextField("Description", max_length=500, blank=True, null=True)

    # Image Fields
    desktop_image = models.ImageField(
        "Bridal Expert Image for Desktop",
        upload_to="Bridal_experts/desktop/",
        null=True,
    )
    mobile_image = models.ImageField(
        "Bridal Expert Image for Image",
        upload_to="Bridal_experts/mobile/",
        null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.name} - {self.designation}"

    class Meta:
        ordering = ('-created_at',)
