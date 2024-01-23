from django.db import models

from apps.core.models import DateTimeModel


class Service(DateTimeModel):
    title = models.CharField("Our Services Title", max_length=50)
    description = models.TextField("Our Services Description", max_length=500, blank=True, null=True)

    # Image Fields
    desktop_image = models.ImageField(
        "Our Services Image for Desktop",
        upload_to="bridal_gallery/desktop/",
        null=True
    )
    mobile_image = models.ImageField(
        "Our Services Image for Mobile",
        upload_to="bridal_gallery/mobile/",
        null=True
    )

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        ordering = ('-created_at',)
