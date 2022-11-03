from django.db import models
import django.contrib.auth

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userEmail = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + str(self.userId)

    class Meta:
        abstract = True
    
class Volunteer(User):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    tokenBalance = models.IntegerField()
    
    def get_name(self):
        return self.firstName + ' ' + self.lastName
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + str(self.userId)

class Business(User):
    name = models.CharField(max_length=200)


class Organisation(User):
    name = models.CharField(max_length=200)

class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    name = models.CharField('Event Name', max_length=200)
    date = models.DateTimeField()
    organiser = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    confirmedVolunteers = models.ManyToManyField(Volunteer, blank=True)

    def __str__(self):
        return self.name + ' ' + str(self.eventId)

# class UserEvent(models.Model):
#     class UserStates(models.IntegerChoices):
#         USER_APPLIED = 1
#         USER_ADMITTED = 2
#         TOKENS_REQUESTED = 3
#         TOKENS_CLAIMED = 4
    
#     userId = models.ForeignKey(User)
#     eventId = models.ForeignKey(Event)
#     state = models.IntegerField(choices=UserStates.choices)
    

#     class 
class Discount(models.Model):
    rewardCode = models.CharField('Reward Code', 
                                  max_length=32, 
                                  # validators=[MinLengthValidator(32)]
                                 )
    expiryDate = models.DateTimeField()