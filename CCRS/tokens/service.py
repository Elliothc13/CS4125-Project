from abc import ABC

class Subject(ABC):
    def notify(self):
        pass

    def attach(self, observer: Observer):
        pass

    def detach(self, observer: Observer):
        pass

class Observer(ABC):
    def update(self, subject: Subject):
        pass

# class VolunteeringFlow():

class GenerateToken():
    def __init__(self, userId, organisationId):
        self._userModel = userModel

# for view
    confirmed_events = userModel.getConfirmedEvents()
    for event in confirmed events:
        render

# for process
    def gen_token():
        validate
    

