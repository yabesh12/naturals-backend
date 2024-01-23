from django.db import models

from apps.core.models import DateTimeModel


class BridalGallery(DateTimeModel):
    # Image Fields
    desktop_image = models.ImageField(
        "Bridal Gallery Image for Desktop",
        upload_to="bridal_gallery/desktop/",
        null=True

    )
    mobile_image = models.ImageField(
        "Bridal Gallery Image for Mobile",
        upload_to="bridal_gallery/mobile/",
        null=True
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Bridal Gallery"
        verbose_name_plural = "Bridal Galleries"
        ordering = ('-created_at',)
