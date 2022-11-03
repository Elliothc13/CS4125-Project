from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
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
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + str(self.userId)

class Business(User):
    businessName = models.CharField(max_length=200)

class Organisation(User):
    organisationName = models.CharField(max_length=200)
    # events = models.ForeignKey(Event, blank=True, null=True)
    #usersWorkedWith = model.

class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    name = models.CharField('Event Name', max_length=200)
    date = models.DateTimeField()
    organiser = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    confirmedVolunteers = models.ManyToManyField(Volunteer, blank=True)

    def __str__(self):
        return self.name + ' ' + str(self.eventId)

class Discount(models.Model):
    rewardCode = models.CharField('Reward Code', 
                                  max_length=32, 
                                  # validators=[MinLengthValidator(32)]
                                 )
    expiryDate = models.DateTimeField()