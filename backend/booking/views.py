from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Slot, Booking
from .serializers import SlotSerializer, BookingSerializer


# Get all slots
@api_view(['GET'])
def get_slots(request):
    slots = Slot.objects.all().order_by('date', 'start_time')
    serializer = SlotSerializer(slots, many=True)
    return Response(serializer.data)


# Get all bookings
@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all().order_by('-booked_at')
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


# Book a slot
@api_view(['POST'])
def book_slot(request):
    slot_id = request.data.get('slot_id')
    name = request.data.get('name')
    email = request.data.get('email')

    if not slot_id or not name or not email:
        return Response(
            {"error": "slot_id, name and email are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        slot = Slot.objects.get(id=slot_id)

        if slot.is_booked:
            return Response(
                {"error": "Slot already booked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Booking.objects.create(slot=slot, name=name, email=email)
        slot.is_booked = True
        slot.save()

        return Response(
            {"message": "Slot booked successfully"},
            status=status.HTTP_201_CREATED
        )

    except Slot.DoesNotExist:
        return Response(
            {"error": "Slot not found"},
            status=status.HTTP_404_NOT_FOUND
        )


# Cancel a booking
@api_view(['POST'])
def cancel_booking(request):
    booking_id = request.data.get('booking_id')

    if not booking_id:
        return Response(
            {"error": "booking_id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        booking = Booking.objects.get(id=booking_id)
        slot = booking.slot
        slot.is_booked = False
        slot.save()
        booking.delete()

        return Response(
            {"message": "Booking cancelled successfully"},
            status=status.HTTP_200_OK
        )

    except Booking.DoesNotExist:
        return Response(
            {"error": "Booking not found"},
            status=status.HTTP_404_NOT_FOUND
        )