from tokens.models import Volunteer, VolunteerEvent
def isVolunteer(userId):
    return Volunteer.objects.filter(userId=userId).exists()

def check_can_approve(entry, approverId, requesterId):
    #entry = VolunteerEvent.objects.get(entryId=entryId)
    assert(entry.userId == requesterId)
    assert(entry.eventId.organiser == approverId)
    return True