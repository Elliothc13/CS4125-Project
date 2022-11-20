from django.shortcuts import render, redirect
from tokens.models import Organisation, Event, Volunteer
from tokens.sub import GenerateToken

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
            return redirect('list-recommendations')
        else:
            volunteer_entries = Event.objects.all()
            events_to_display = []
            print('=1====', volunteer_entries, '=====')
            for entry in volunteer_entries:
                event_temp = entry
                print('+++++', event_temp)
                events_to_display.append(event_temp) # caution, Django returns the model not the field here
            print('-------', request.user.id)
            tokenBalance = GenerateToken.get_current_tokens(request.user.id)
            return render(request, 'recommender/recommendations_list.html', {'events_list': events_to_display, 'tokenBalance': tokenBalance})
        
    return redirect('list-recommendations')