from django.test import TestCase
import unittest
from tokens.models import Event, Volunteer, Organisation, VolunteerEvent
# Create your tests here.

class TestVolunteer(unittest.TestCase):
    def setUp(self):
        pass

    def TearDown(self):
        pass

    def TestVolunteer(self):
        vol_1 = Volunteer("john", "murphy", "10", "1")
        vol_2 = Volunteer("larry", "obrien", "10", "1")
        
        self.assertEqual(vol_1.email, 'john.murphy@email.com')
        self.assertEqual(vol_1.email, 'larry.obrien@email.com')

        vol_1.first = 'tim'
        vol_2.first = 'gary'

        self.assertEqual(vol_1.email, 'tim.murphy@email.com')
        self.assertEqual(vol_1.email, 'gary.obrien@email.com')

    def TestTokenBalance(self):
        vol_1 = Volunteer("john", "murphy", "10", "1")
        vol_2 = Volunteer("larry", "obrien", "10", "1")

        self.assertTrue(vol_1.TokenBalance, 10)
        self.assertFalse(vol_2.TokenBalance, 20)

        vol_2.tokens = 10

        self.assertTrue(vol_2.TokenBalance, 10)

    def TestTokenTier(self):
        vol_1 = Volunteer("john", "murphy", "10", "1")
        vol_2 = Volunteer("larry", "obrien", "10", "1")
        vol_3 = Volunteer("tim", "ryan", "50", "2")
        vol_4 = Volunteer("craig", "coye", "100", "3")

        self.assertTrue(vol_1.TokenTier, 1)
        self.assertFalse(vol_2.TokenTier, 3)
        self.assertTrue(vol_3.TokenTier, 2)
        self.assertFalse(vol_4.TokenTier, 1)

        vol_2.TokenTier = 1
        vol_4.TokenTier = 3

        self.assertTrue(vol_2.TokenTier, 1)
        self.assertTrue(vol_4.TokenTier, 3)

class TestEvents(unittest.TestCase):
    def setUp(self):
        pass

    def TearDown(self):
        pass

    def TestEventId(self):
        Event_1 = Event("23","BagPacking", "03/02/2022", "Tesco", "you will be bag packing!", "6")
        Event_2 = Event("46", "fun run","23/10/2022","St Vincent de pauls", "Run for the boiz in zambia", "30" )

        self.assertEquals(Event_1.EventId, 23)
        self.assertEquals(Event_2.EventId, 46)

        Event_1.Event = 24

        self.assertEquals(Event_1.EventId, 24)

    def TestDate(self):
        Event_1 = Event("23","BagPacking", "03/02/2022", "Tesco", "you will be bag packing!", "6")
        Event_2 = Event("46", "fun run","23/10/2022","St Vincent de pauls", "Run for the boiz in zambia", "30" )

        self.assertTrue(Event_1.Eventdate, "03/02/2022")
        self.assertFalse(Event_2.Eventdate, "22/10/2022")

        Event_2.Eventdate = "23/10/2022"

        self.assertTrue(Event_2.Eventdate, "23/10/2022")

class TestTokenState(unittest.TestCase):
    def setUp(self):
        pass

    def TearDown(self):
        pass

