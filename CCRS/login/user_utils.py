from tokens.models import Volunteer
def isVolunteer(userId):
    return Volunteer.objects.filter(userId=userId).exists()