from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    userEmail = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Volunteer(User):
    def zero():
        return 0
    firstName = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    tokenBalance = models.IntegerField()
    
    
class Business(User):
    businessName =models.CharField(max_length=200)

class Organisation(User):
    organisationName = models.CharField(max_length=200)

class Discount(models.Model):
    rewardCode = models.CharField('Reward Code', 
                                  max_length=32, 
                                  validators=[MinLengthValidator(32)]
                                 )
    expiryDate = models.DateTimeField()
