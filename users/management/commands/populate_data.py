from django.core.management.base import BaseCommand
from users.models import User
from events.models import Event, Address

class Command(BaseCommand):
    help = "Populate database with test data"

    def handle(self, *args, **kwargs):
        # Create a user
        user = User.objects.create(username="newuser1", email="newuser@example.com")
        user.set_password("newpassword")
        user.save()

        # Create addresses
        origin = Address.objects.create(
            title="Origin Address",
            line1="123 Main St",
            city="City A",
            country="Country X",
            latitude = "1651.51",
            longitude = "5165.485",
            description = "nothing"
        )
        destination = Address.objects.create(
            title="Destination Address",
            line1="456 Elm St",
            city="City B",
            country="Country Y",
            latitude = "1651.51",
            longitude = "5165.485",
            description = "nothing"
        )

        # Create an event
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            capacity=100,
            created_by=user,
            origin_address=origin,
            destination_address=destination
        )

        self.stdout.write(self.style.SUCCESS(f"Successfully created event: {event}"))
