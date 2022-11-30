from django.shortcuts import render, redirect
from tokens.models import Event
from .sub import OrganisationNotifier


def confirmed_events(request):
    volunteerId = request.user.id
    if request.user.is_authenticated:
        #buttons on page then do this
        if request.method == 'POST':
            eventToUpdate = request.POST.get('eventId')
            print('???????', eventToUpdate)
            return redirect('list-recommendations')
        else:
            #default and what the home button will do
            volunteer_entries = Event.objects.all()
            events_to_display = []
            print('=1====', volunteer_entries, '=====')
            for entry in volunteer_entries:
                event_temp = entry
                print('+++++', event_temp)
                # caution, Django returns the model not the field here
                events_to_display.append(event_temp)
            print('-------', request.user.id)
            return render(request, 'recommender/recommendations_list.html', {'events_list': events_to_display})

    return redirect('list-recommendations')
