from django.urls import path
from . import views

urlpatterns = [
    path('slots/', views.get_slots),
    path('book/', views.book_slot),
    path('bookings/', views.get_bookings),
    path('cancel/', views.cancel_booking),
]