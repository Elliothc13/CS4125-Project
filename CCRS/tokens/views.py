from django.shortcuts import render, redirect
# impoort data from table
from .models import VolunteerEvent, Event, Volunteer, Organisation
from .sub import GenerateToken
from .upgrade_tiers import UpgradeTiersControl
from login.user_utils import check_can_approve

def confirmed_events(request):
    volunteerId = request.user.id
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
            volunteer_entries = VolunteerEvent.objects.filter(
                userId=volunteerId)
            events_to_display = []
            print('=1====', volunteer_entries, '=====')
            for entry in volunteer_entries:
                event_temp = entry.eventId
                print('+++++', event_temp)
                event_temp.state = entry.state
                event_temp.btDisabled = not GenerateToken.can_generate_token(
                    event_temp.state)
                # caution, Django returns the model not the field here
                events_to_display.append(event_temp)
            print('-------', request.user.id)
            tokenBalance = GenerateToken.get_current_tokens(request.user.id)
            return render(request, 'tokens/events_list.html', {'events_list': events_to_display, 'tokenBalance': tokenBalance})

    return redirect('list-confirmed-events')



def approve_tokens(request, pk):
    currentId = request.user.id
    if request.user.is_authenticated:
        entry = VolunteerEvent.objects.get(id=pk)
        if request.method == 'POST':
            if check_can_approve(entry, currentId, entry.userId):
                attemptUpgrade = UpgradeTiersControl(entry.userId, entry.eventId, currentId)
                attemptUpgrade.approveHours()
            else:
                return render('logout')
        else:
            if entry.eventId.organiser == currentId: # if current user is the organiser
                name = Volunteer.objects.get(userId=entry.userId).get_name()
                eventName = Event.objects.get(eventId=entry.eventId).name
                # show the approval page
                return render(request, 'tokens/approve_tokens.html', { 'approveForName': name, 'approveForEvent': eventName})
            return redirect('logout')
    else:
        return redirect('login')