from abc import ABC, abstractmethod
from __future__ import annotations
from typing import List
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
    def createTier(self, level):
        if level == 0:
            context = Context(BronzeTier())
            context.business_logic(1)
            return context
        elif level == 1:
            context = Context(SilverTier())
            context.business_logic(2)
            return context
        else:
            context = Context(GoldTier())
            context.business_logic(3)
            return context


class TierProduct(ABC):
    def calculateTokens(self, hours_worked):
        pass


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def business_logic(self, hoursWorked) -> None:
        result = self._strategy.calc_hours(hoursWorked)
        return result


class Strategy(ABC):
    @abstractmethod
    def calculateTokens(self, currentBalance, hoursWorked):
        pass


class BronzeTier(Strategy, TierProduct):
    def calculateTokens(self, currentBalance, hoursWorked) -> List:
        return currentBalance + hoursWorked * 1


class SilverTier(Strategy, TierProduct):
    def calculateTokens(self, currentBalance, hoursWorked) -> List:
        return currentBalance + hoursWorked * 2


class GoldTier(Strategy, TierProduct):
    def calculateTokens(self, currentBalance, hoursWorked) -> List:
        return currentBalance + hoursWorked * 3
