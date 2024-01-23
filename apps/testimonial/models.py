from django.db import models

from apps.core.models import DateTimeModel


class Testimonial(DateTimeModel):
    name = models.CharField("Customer Name", max_length=50)
    description = models.TextField("Customer Testimonial Review", max_length=1000, null=True, blank=True)
    desktop_video = models.FileField("Customer Testimonial Video for Desktop",
                                     upload_to='customer_testimonial/desktop/', null=True)
    mobile_video = models.FileField("Customer Testimonial Video for Mobile", upload_to='customer_testimonial/mobile/', null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ('-created_at',)
