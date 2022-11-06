from django.shortcuts import render, redirect
# impoort data from table
from .models import VolunteerEvent, Event, Volunteer
from .sub import GenerateToken
# Create your views here.
# from blog.models import Blog
# b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
# b.save() actually inserts

def confirmed_events(request):
    volunteerId=request.user.id
    # volunteer_entries = VolunteerEvent.objects.filter(userId=volunteerId)
    if request.user.is_authenticated:
        if request.method == 'POST':
            eventToUpdate = request.POST.get('eventId')
            print('???????', eventToUpdate)
            organisationId = Event.objects.get(eventId=eventToUpdate).organiser
            currentTier = Volunteer.objects.get(userId=volunteerId).currentTier
            service = GenerateToken(volunteerId, eventToUpdate, organisationId)
            service.generateToken()
            return redirect('list-confirmed-events')
        else:
            volunteer_entries = VolunteerEvent.objects.filter(userId=volunteerId)
            events_to_display = []
            print('=1====', volunteer_entries, '=====')
            for entry in volunteer_entries:
                event_temp = entry.eventId
                print('+++++', event_temp)
                event_temp.state = entry.state
                event_temp.btDisabled = not GenerateToken.can_generate_token(event_temp.state)
                events_to_display.append(event_temp) # caution, Django returns the model not the field here
            print('-------', request.user.id)
            tokenBalance = GenerateToken.get_current_tokens(request.user.id)
            return render(request, 'tokens/events_list.html', {'events_list': events_to_display, 'tokenBalance': tokenBalance})
        
    return redirect('list-confirmed-events')