from abc import ABC

#from sub import VolunteeringFlow, VolunteerEvent, 
#from tokens.emails import EmailSender

# class UpgradeTiersControl:
#     def __init__(self, volunteerId, eventId, organisationId, entryId) -> None:
#         self.volunteerId = volunteerId
#         self.eventId = eventId
#         self.organisationId = organisationId
#         self.service = NotificationService()
#         self.states = VolunteerEvent.UserStates
#         self.subject.attach(OrganisationNotifier(organisationId, self.generateOrgStates()))
#         self.subject.attach(VolunteerNotifier(volunteerId, self.generateVolStates()))
#         self.subject.attach(TierUpgraderConcreteObserver(volunteerId))
#         self.subject.setState()

#     def approveHours():



# class UpgradeTiersSubject():
# class Client
# class NotificationService_Publisher:

# class EventListener(ABC):
#     def update():
#         pass

# class EmailListener(EventListener):
#     def __init__(self, email, entry) -> None:
#         super().__init__()
#         self.email = email
#         self.entry = entry

#     def update(self, state):
#         if state == 'TOKEN_REQUESTED':
#             #link = 
#             EmailSender.sendEmail(None, self.email, 'Hours approval', 'A user has requested hours approval <Link>')

# Decorator


class Component(ABC):
    def appendToLink(self, text):
        pass

class LinkComponent(Component):
    _link: str
    def __init__(self, baseUrl) -> None:
        super().__init__()
        self._link = baseUrl

    def appendToLink(self, text):
        self._link = self._link + text

    def getLink(self):
        return self._link

class LinkDecorator():
    _component: Component
    _text: str
    def __init__(self, component: Component) -> None:
        # super().__init__()
        self._component = component

    def appendToLink(self, text):
        self._component.appendToLink(text)
    
    def getLink(self):
        return self._component.getLink()

class LinkMaker(LinkDecorator):
    def __init__(self, component: LinkDecorator, text: str) -> None:
        super().__init__(component)
        self.appendToLink(text)

    def appendToLink(self, text):
        super().appendToLink(text)

# class OrganisationIdDecorator(LinkDecorator):
#     def __init__(self, component: Component, text: str) -> None:
#         super().__init__(component)
#         # self.appendToLink(text)

#     def appendToLink(self, text):
#         super().appendToLink('/orgId/' + text)

# class EventIdDecorator(LinkDecorator):
#     def __init__(self, component: Component, text: str) -> None:
#         super().__init__(component)
#         self.appendToLink(text)

#     def appendToLink(self, text):
#         super().appendToLink('/eventId/' + text)



# aComponent = LinkComponent('https://127.0.0.1:8000')
# aComponent = LinkMaker(aComponent, )
# print(aComponent.getLink())
# aComponent = UserIdDecorator(aComponent, entry['volunteerId'])
# print(aComponent.getLink())
# aComponent = EventIdDecorator(aComponent, entry['eventId'])
# print(aComponent.getLink())