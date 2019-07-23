from django.contrib import admin
from .models import Flight, Booking
# Register your models here.

admin.site.register(Flight)
# code to register Flight to the site
admin.site.register(Booking)