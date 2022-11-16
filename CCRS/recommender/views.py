from django.shortcuts import render, redirect
# impoort data from table
# from .models import VolunteerEvent, Event, Volunteer
# from .sub import GenerateToken

def confirmed_events(request):
    volunteerId=request.user.id
    # volunteer_entries = VolunteerEvent.objects.filter(userId=volunteerId)
    if request.user.is_authenticated:
        if request.method == 'POST':
            eventToUpdate = request.POST.get('eventId')
            print('???????', eventToUpdate)
            return redirect('list-recommendations')
        else:
            print('-------', request.user.id)
            tokenBalance = 2
            return render(request, 'recommender/recommendations_list.html')
        
        return redirect('list-recommendations')