from django.urls import path
from .views import add_reading, view_readings, home

urlpatterns = [
    path('add_reading', add_reading),
    path('view_readings', view_readings),
    path('home', home)
]
