from django.db import models

from apps.core.models import DateTimeModel


# Glimpse Video Carousel
class GlimpseVideoCarousel(DateTimeModel):
    desktop_video = models.FileField("Glimpse Video for Desktop", upload_to='glimpse_videos/desktop/', null=True)
    mobile_video = models.FileField("Glimpse Video for Mobile", upload_to='glimpse_videos/mobile/', null=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ('-created_at',)
