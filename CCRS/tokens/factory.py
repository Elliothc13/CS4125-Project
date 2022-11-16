from abc import ABC, abstractmethod
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
# 
#
    def createTier(self, level):
        if level == 0:
            return BronzeTierConcreteProduct()
        elif level == 1:
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