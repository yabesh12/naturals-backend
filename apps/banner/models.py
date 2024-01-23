from django.db import models

from apps.core.models import DateTimeModel


# Banner Video
class Banner(DateTimeModel):
    desktop_video = models.FileField("Banner Video for Desktop", upload_to='banner_videos/desktop/', null=True)
    mobile_video = models.FileField("Banner Video for Mobile", upload_to='banner_videos/mobile/', null=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ('-created_at',)
