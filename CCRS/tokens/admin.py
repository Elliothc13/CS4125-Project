from django.contrib import admin
from .models import Event, Volunteer, Organisation
# Register your models here.

admin.site.register(Event)
admin.site.register(Volunteer)
admin.site.register(Organisation)