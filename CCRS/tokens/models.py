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
    tokenBalance = models.IntegerField(default=1)
    currentTier = models.IntegerField(default=1)
    hoursLastWeek = models.IntegerField(default=0)
    hoursThisWeek = models.IntegerField(default=0)

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


class VolunteerEvent(models.Model):
    class UserStates(models.TextChoices):
        USER_APPLIED = 'USER_APPLIED'
        USER_ADMITTED = 'USER_ADMITTED'
        TOKENS_REQUESTED = 'TOKENS_REQUESTED'
        TOKENS_APPROVED = 'TOKENS_APPROVED'
        TOKENS_CLAIMED = 'TOKENS_CLAIMED'

    userId = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=50, choices=UserStates.choices, default=UserStates.USER_ADMITTED)

    def __str__(self):
        return 'VolunteerEvent: ' + str(self.userId) + ' ' + str(self.eventId)


class Discount(models.Model):
    rewardCode = models.CharField('Reward Code',
                                  max_length=32,
                                  )
    expiryDate = models.DateTimeField()
