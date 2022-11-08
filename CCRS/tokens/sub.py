from abc import ABC, abstractmethod
from typing import List
from .models import Event, Volunteer, VolunteerEvent

# class Subject(ABC):
#     @abstractmethod
#     def attach(self, observer: Observer):
#         pass
#     @abstractmethod
#     def detach(self, observer: Observer):
#         pass
#     @abstractmethod
#     def notify(self):
#         pass

class VolunteeringFlow:
    def __init__(self) -> None:
        super().__init__()
        self.state = None
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.state)
    
    def setState(self, updatedState):
        self.state = updatedState
        self.notify()

# add abstract before class definition
# class Observer(ABC):
#     @abstractmethod
#     def update(self, subject: Subject):
#         pass

class OrganisationNotifier:
    def __init__(self, organisationId, reactableStates):
        self.organisationId = organisationId
        self.reactableStates = reactableStates


    def update(self, state):
        if state in self.reactableStates:
            print("========Notifying organisation a user applied for a position")

class VolunteerNotifier:
    def __init__(self, volunteerId, reactableStates):
        self.volunteerId = volunteerId
        self.reactableStates = reactableStates


    def update(self, state):
        if state in self.reactableStates:
            print("========Notifying volunteer organisation approved the tokens to claim")


# responsible for setting state on VolunteeringFlow
class GenerateToken:
    def __init__(self, volunteerId, eventId, organisationId):
        self.volunteerId = volunteerId
        self.eventId = eventId
        self.organisationId = organisationId
        self.subject = VolunteeringFlow()
        self.states = VolunteerEvent.UserStates
        self.subject.attach(OrganisationNotifier(organisationId, self.generateOrgStates()))
        self.subject.attach(VolunteerNotifier(volunteerId, self.generateVolStates()))
    

    def generateOrgStates(self):
        return [self.states.USER_APPLIED, self.states.TOKENS_REQUESTED]

    def generateVolStates(self):
        all_states = VolunteerEvent.UserStates
        return [all_states.USER_ADMITTED, all_states.TOKENS_CLAIMED]

    
    def calculateTokens(self, current_balance, currentTier):
        return current_balance + currentTier
    
    @staticmethod
    def can_generate_token(currentState):
        return GenerateToken.can_request_token(currentState) or GenerateToken.can_claim_token(currentState)

    @staticmethod
    def can_request_token(currentState):
        return currentState == VolunteerEvent.UserStates.USER_ADMITTED

    @staticmethod
    def can_claim_token(currentState):
        return currentState == VolunteerEvent.UserStates.TOKENS_APPROVED
    
    @staticmethod
    def get_current_tokens(userId):
        print(Volunteer.objects.get(userId=userId).tokenBalance)
        return Volunteer.objects.get(userId=userId).tokenBalance
    
    def fetchState(self):
        return VolunteerEvent.objects.get(userId=self.volunteerId, eventId=int(self.eventId)).state

    def request_token(self):
        entry = VolunteerEvent.objects.get(userId=self.volunteerId, eventId=self.eventId)
        updated_state = self.states.TOKENS_REQUESTED
        entry.state = updated_state
        entry.save()
        self.subject.setState(updated_state) # notifies the organisation

    def claim_token(self):
        entry = VolunteerEvent.objects.get(userId=self.volunteerId, eventId=self.eventId)
        updated_state = self.states.TOKENS_CLAIMED
        entry.state = updated_state
        entry.save()
        user = Volunteer.objects.get(userId=self.volunteerId)
        current_balance = user.tokenBalance
        current_tier = user.currentTier
        updated_balance = self.calculateTokens(current_balance, current_tier)
        user.tokenBalance = updated_balance
        user.save()
        self.subject.setState(self.states.TOKENS_CLAIMED) # notifies the user


    def generateToken(self): # updates tokens
        currentState = self.fetchState()
        if self.can_request_token(currentState):
            self.request_token()
           
        elif self.can_claim_token(currentState):
            self.claim_token()

    # class VolunteeringFlowState:
    #     def flow_clear():
    #         pass
    #     def advance_flow(current):
    #         pass

    # class TokensRequestedState:
    #     def flow_clear():
    #         return True
    #     def advance_flow():
    #         if current_state == VolunteerEvent.UserStates.TOKENS_REQUESTED
    #             user = Volunteer.objects.get(id=self.volunteerId)
    #             current_balance = user.tokenBalance
    #             updated_balance = self.calculateTokens(current_balance, currentTier)
    #             user.tokenBalance = updated_balance
    #             user.save()
    #             return True
    #         return False
    # class TokensClaimedState:
    #     def flow_clear():
    #         return True
    #     def advance_flow():
    #         return True