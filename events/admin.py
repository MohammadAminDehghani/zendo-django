from django.contrib import admin
from .models import Event, Address, EventSchedule

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'capacity', 'origin_address', 'destination_address')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country')

@admin.register(EventSchedule)
class EventScheduleAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'departure_time', 'return_time')

