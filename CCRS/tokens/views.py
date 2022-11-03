from django.shortcuts import render
# impoort data from table
from .models import Volunteer

# Create your views here.
# from blog.models import Blog
# b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
# b.save() actually inserts

def confirmed_events(request, volunteerId):
    # volunteer = Event.objects
    # voluntee
    # a1.publications.add(p1)
    return render(request, 'tokens/generate_tokens.html', {event_list})