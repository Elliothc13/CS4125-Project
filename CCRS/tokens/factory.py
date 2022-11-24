from abc import ABC, abstractmethod
from __future__ import annotations
from typing import List


class UpgradeVolunteerTierCreator(ABC):
    @abstractmethod
    def createTier(level):
        pass

    def calculateTokens(level, hoursWorked):
        tierProduct = createTier(level)
        return tierProduct.calculateTokens(hoursWorked)


class TierFactoryConcreteCreator(UpgradeVolunteerTierCreator):
    # create new, different types of instances of a parent
    # classes have same methods, but each method behaves differently
    # many factories can exist
    def createTier(self, level):
        if level == 0:
            context = Context(ConcreteStrategyA())
            context.business_logic(1)
            return context()
        elif level == 1:
            context = Context(ConcreteStrategyB())
            context.business_logic(2)
            return context()
        else:
            context = Context(ConcreteStrategyC())
            context.business_logic(3)
            return context()


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
    def calc_hours(self, hoursWorked):
        pass


class ConcreteStrategyA(Strategy):
    def calc_hours(self, hoursWorked) -> List:
        return hoursWorked * 1


class ConcreteStrategyB(Strategy):
    def calc_hours(self, hoursWorked) -> List:
        return hoursWorked * 2


class ConcreteStrategyC(Strategy):
    def calc_hours(self, hoursWorked) -> List:
        return hoursWorked * 3
