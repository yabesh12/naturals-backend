from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.core.models import DateTimeModel


class Service(DateTimeModel):
    service = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.id} - {self.service}"

    class Meta:
        ordering = ('-created_at',)


class State(DateTimeModel):
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.state}"

    class Meta:
        ordering = ('-created_at',)


class City(DateTimeModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.state} -{self.city}"

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ('-created_at',)


class Booking(DateTimeModel):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, max_length=100, related_name="booking_service",
                                null=True)
    booking_date = models.DateField("Service Booking Date", null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, max_length=100, related_name="booking_state",
                              null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, max_length=100, related_name="booking_city", null=True)
    message = models.TextField(max_length=600, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.first_name} - {self.service} - {self.booking_date} - {self.city}"

    class Meta:
        ordering = ('-created_at',)
