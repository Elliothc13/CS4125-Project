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
            context = Context(ConcreteStrategy())
            context.do_some_business_logic(1)
            return context()
        elif level == 1:
            context = Context(ConcreteStrategy())
            context.do_some_business_logic(2)
            return context()
        else:
            context = Context(ConcreteStrategy())
            context.do_some_business_logic(3)
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


    def do_some_business_logic(self, hoursWorked, n) -> None:
        result = self._strategy.do_algorithm(hoursWorked, n)
        return result

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, hoursWorked, n):
        pass

class ConcreteStrategy(Strategy):
    def do_algorithm(self, hoursWorked, n) -> List:
        return hoursWorked * n
