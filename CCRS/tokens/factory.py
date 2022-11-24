from abc import ABC, abstractmethod
from .models import VolunteerEvent, Volunteer

class TierUpgraderConcreteObserver:
    def __init__(self, volunteerId) -> None:
        self.volunteerId = volunteerId

    def update(self, state, entryId):
        if state == VolunteerEvent.UserStates.TOKENS_APPROVED: # hours have been confirmed
            UpgradeVolunteerTierCreator.tryUpgradeTier(self.volunteerId)


class UpgradeVolunteerTierCreator(ABC):
    @abstractmethod
    def createTier(level):
        pass

    @staticmethod
    def calculateTokens(currentBalance, currentTier, hoursWorked):
        tierProduct = createTier(currentTier)
        return tierProduct.calculateTokens(currentBalance, hoursWorked)

    @staticmethod
    def tryUpgradeTier(volunteerId):
        user = Volunteer.objects.get(volunteerId=volunteerId)
        tierProduct = createTier(user.currentTier)
        if tierProduct.canBeUpgraded(user.hoursLastWeek, user.hoursThisWeek):
            user.currentTier += 1
            print("===== Tier of user", user + "upgraded to", user.currentTier)
            user.save()



class TierFactoryConcreteCreator(UpgradeVolunteerTierCreator):
# create new, different types of instances of a parent
# classes have same methods, but each method behaves differently
# many factories can exist
# 
#
    def createTier(self, level):
        if level == 0:
            return BronzeTierConcreteProduct()
        elif level == 2:
            return SilverTierConcreteProduct()
        else:
            return GoldenTierConcreteProduct()

class TierProduct(ABC):
    def calculateTokens(self, hours_worked):
        pass

class BronzeTierConcreteProduct(TierProduct):
    def calculateTokens(self, hoursWorked):
        return hoursWorked * 1
class SilverTierConcreteProduct(TierProduct):
    def calculateTokens(self, hoursWorked):
        return hoursWorked * 2
class GoldenTierConcreteProduct(TierProduct):
    def calculateTokens(self, hoursWorked):
        return hoursWorked * 3