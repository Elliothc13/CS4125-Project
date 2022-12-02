from abc import ABC, abstractmethod
#from __future__ import annotations
from typing import List
from .models import VolunteerEvent, Volunteer


class TierUpgraderConcreteObserver:
    """ Concrete Observer that tries to upgrade tier when the organisation approves tokens for a volunteer"""
    def __init__(self, volunteerId) -> None:
        self.volunteerId = volunteerId

    def update(self, state, entryId):
        print("----- Tokens approved, checking if need to upgrade tier")
        """ When update is called with a state, checks if the state change requires an action """
        if state == VolunteerEvent.UserStates.TOKENS_APPROVED: # hours have been confirmed
            UpgradeVolunteerTierCreator.tryUpgradeTier(self.volunteerId)


class UpgradeVolunteerTierCreator(ABC):
    """Abstract class for creating the tier for calculating tokens to be added to a volunteer balance"""
    @abstractmethod
    def createTier(level):
        pass

    @staticmethod
    def calculateTokens(currentBalance, currentTier, hoursWorked):
        """ Uses factory method to create a tier depending on hours worked and then calculates the token """
        assert (currentBalance >= 0) #makes sure you dont have a negative ballance of tokens 
        tierProduct : TierProduct = createTier(currentTier)
        return tierProduct.calculateTokens(currentBalance, hoursWorked)

    @staticmethod
    def tryUpgradeTier(volunteerId):
        """ Uses factory to produce a Tier strategy and upgrades its value in the model """
        assert int(volunteerId) # checks that the volunteerID is an int 
        user = Volunteer.objects.get(volunteerId=volunteerId)
        tierProduct = createTier(user.currentTier)
        if tierProduct.canBeUpgraded(user.hoursLastWeek, user.hoursThisWeek):
            print("----- Upgrading tier")
            user.currentTier += 1
            print("===== Tier of user", user + "upgraded to", user.currentTier)
            user.save()

class TierFactoryConcreteCreator(UpgradeVolunteerTierCreator):
    """ Concrete factory class, produces tiers for calculating tokens"""
    # create new, different types of instances of a parent
    # classes have same methods, but each method behaves differently
    # many factories can exist
    def createTier(self, level):
        """ Produces a concrete tier (Bronze, Silver or Gold) """
        if level == 0:
            context = Context(BronzeTier())
            #context.business_logic(1)
            print("----- Returning Bronze Tier")
            return context
        elif level == 1:
            context = Context(SilverTier())
            #context.business_logic(2)
            print("----- Returning Silver Tier")
            return context
        else:
            context = Context(GoldTier())
            #context.business_logic(3)
            print("----- Returning Gold Tier")
            return context


class TierProduct(ABC):
    """ Interface for producing tier strategies"""
    def calculateTokens(self, currentBalance, hours_worked):
        pass


class Strategy(ABC):
    """ Interface for calculating volunteer tokens """
    @abstractmethod
    def calculateTokens(self, currentBalance, hoursWorked):
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

    # def business_logic(self, hoursWorked) -> None:
    #     result = self._strategy.calculateTokens(hoursWorked)
    #     return result




class BronzeTier(Strategy, TierProduct):
    """ Used by factory to produce a strategy for calculating tokens for bronze tier volunteers """
    def calculateTokens(self, currentBalance, hoursWorked):
        print("----- Calculating new token balance with Bronze Tier")
        return currentBalance + hoursWorked * 1


class SilverTier(Strategy, TierProduct):
    """ Used by factory to produce a strategy for calculating tokens for silver tier volunteers """
    
    def calculateTokens(self, currentBalance, hoursWorked):
        print("----- Calculating new token balance with Silver Tier")
        return currentBalance + hoursWorked * 2


class GoldTier(Strategy, TierProduct):
    """ Used by factory to produce a strategy for calculating tokens for gold tier volunteers """
    def calculateTokens(self, currentBalance, hoursWorked):
        print("----- Calculating new token balance with Gold Tier")
        return currentBalance + hoursWorked * 3
