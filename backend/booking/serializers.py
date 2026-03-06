from rest_framework import serializers
from .models import Slot, Booking


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    slot_detail = SlotSerializer(source='slot', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'slot', 'slot_detail', 'name', 'email', 'booked_at']