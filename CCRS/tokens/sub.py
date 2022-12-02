from abc import ABC, abstractmethod
from threading import currentThread
from typing import List, Self

from traitlets import ObserveHandler, observe
from .models import Event, Volunteer, VolunteerEvent, Organisation
from .emails import EmailSender
from .upgrade_tiers import LinkMaker, LinkComponent


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: observe):
        pass

    @abstractmethod
    def detach(self, observer: observe):
        pass

    @abstractmethod
    def notify(self):
        pass


class VolunteeringFlow:
    def __init__(self, entryId) -> None:

        super().__init__()

        self.state = None
        self.entryId = entryId
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.state, self.entryId)

    def setState(self, updatedState):
        self.state = updatedState
        self.notify()

# add abstract before class definition


class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass


class OrganisationNotifier(Observer):
    def __init__(self, organisationId, reactableStates):
        self.organisationId = organisationId
        self.reactableStates = reactableStates

    def update(self, state, entryId):
        if state in self.reactableStates:
            print("========Notifying organisation a user applied for a position")
            orgEmail = Organisation.objects.get(
                userId=self.organisationId).userEmail
            EmailSender.sendEmail("system@email.com", orgEmail, "User needs approval", "User has requested your approval. To approve click here: " +
                                  LinkMaker(LinkComponent('http://127.0.0.1:8000/tokens'), '/entryid/' + str(entryId)).getLink())


class VolunteerNotifier(Observer):
    def __init__(self, volunteerId, reactableStates):
        self.volunteerId = volunteerId
        self.reactableStates = reactableStates

    def update(self, state, entryId):
        if state in self.reactableStates:
            print("========Notifying volunteer organisation approved the tokens to claim")


# responsible for setting state on VolunteeringFlow
class GenerateToken:
    def __init__(self, volunteerId, eventId, organisationId):
        self.volunteerId = volunteerId
        self.eventId = eventId
        self.organisationId = organisationId
        self.subject = VolunteeringFlow(self.fetchEntryId())
        self.states = VolunteerEvent.UserStates
        self.subject.attach(OrganisationNotifier(
            self.organisationId.userId, self.generateOrgStates()))
        self.subject.attach(VolunteerNotifier(
            self.volunteerId, self.generateVolStates()))

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

    def fetchEntryId(self):
        return VolunteerEvent.objects.get(userId=self.volunteerId, eventId=int(self.eventId)).id

    def request_token(self):
        entry = VolunteerEvent.objects.get(
            userId=self.volunteerId, eventId=self.eventId)
        updated_state = self.states.TOKENS_REQUESTED
        entry.state = updated_state
        entry.save()
        self.subject.setState(updated_state)  # notifies the organisation

    def claim_token(self):
        entry = VolunteerEvent.objects.get(
            userId=self.volunteerId, eventId=self.eventId)
        updated_state = self.states.TOKENS_CLAIMED
        entry.state = updated_state
        entry.save()
        user = Volunteer.objects.get(userId=self.volunteerId)
        current_balance = user.tokenBalance
        current_tier = user.currentTier
        updated_balance = self.calculateTokens(current_balance, current_tier)
        user.tokenBalance = updated_balance
        user.save()
        self.subject.setState(self.states.TOKENS_CLAIMED)  # notifies the user

    def generateToken(self):  # updates tokens
        currentState = self.fetchState()
        if self.can_request_token(currentState):
            self.request_token()

        elif self.can_claim_token(currentState):
            self.claim_token()
