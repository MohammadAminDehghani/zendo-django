# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Additional fields
    family = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Example: User can have multiple addresses (a home address, etc.)
    addresses = models.ManyToManyField("events.Address", related_name='users')  # Use string reference

    # REQUIRED_FIELDS defines additional fields required for creating a superuser
    REQUIRED_FIELDS = ['email', 'family', 'phone']

    def __str__(self):
        return self.username
    
    # Relationship for events created by the user
    def created_events(self):
        return self.event_set.all()

    # Relationship for events the user has joined
    joined_events = models.ManyToManyField(
        'events.Event',  # Reference to Event model in events app
        through='events.EventParticipant',  # Reference to EventParticipant model in events app
        related_name='participants',
    )

