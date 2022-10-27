from django.contrib import admin
from recommender.models import Business, Organisation, Volunteer

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Business)
admin.site.register(Organisation)