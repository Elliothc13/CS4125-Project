from django.shortcuts import render
# impoort data from table
from .models import Volunteer

# Create your views here.
# from blog.models import Blog
# b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
# b.save() actually inserts

def confirmed_events(request):
    if request.user.is_authenticated:
        volunteer = Volunteer.objects.get(userId=request.user.id)
        print('=========', dir(volunteer), '========')
        events_list = volunteer.event_set.all()
        print('=========', events_list, '========')
        # voluntee
        # a1.publications.add(p1)
        return render(request, 'tokens/events_list.html', {'events_list': events_list})