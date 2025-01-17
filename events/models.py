# events/models.py
from django.db import models

class Address(models.Model):
    title = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}, {self.city}"

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.IntegerField()
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)  # Use string reference
    origin_address = models.ForeignKey(Address, related_name='origin_events', on_delete=models.CASCADE)
    destination_address = models.ForeignKey(Address, related_name='destination_events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class EventParticipant(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)  # Use string reference
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')  # E.g., 'joined', 'left', etc.
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

class EventSchedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    departure_time = models.TimeField()
    return_time = models.TimeField(blank=True, null=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)  # E.g., 'Monday'

    def __str__(self):
        return f"{self.event.title} - {self.date}"
