from django.contrib import admin
from .models import Slot, Booking


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'start_time', 'end_time', 'is_booked']
    list_filter = ['is_booked', 'date']
    search_fields = ['date']
    ordering = ['date', 'start_time']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'slot', 'booked_at']
    search_fields = ['name', 'email']
    ordering = ['-booked_at']