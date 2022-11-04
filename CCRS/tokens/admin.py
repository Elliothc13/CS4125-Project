from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Event)
admin.site.register(Volunteer)
admin.site.register(Organisation)
admin.site.register(VolunteerEvent)