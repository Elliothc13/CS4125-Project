from abc import ABC, abstractmethod
from .models import Organisation
from tokens.emails import EmailSender
from tokens.upgrade_tiers import LinkMaker, LinkComponent

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
            EmailSender.sendEmail("system@email.com", orgEmail, "User needs admittion", "User has requested to work with you. To approve click here: " +
                                  LinkMaker(LinkComponent('http://127.0.0.1:8000/reccomendation'), '/entryid/' + str(entryId)).getLink())