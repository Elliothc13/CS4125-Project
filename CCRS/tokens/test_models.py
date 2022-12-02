#from django import setup
#from django.test import TestCase
from unittest import TestCase
#import unittest

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
#setup()
from tokens.models import Volunteer, Discount

# Create your tests here.
#Testing models 


class test_testVolunteer(TestCase):
    def setUp(self):
        pass

    


    def test_Volunteer(self):
        from tokens.models import Volunteer
        vol_1 = Volunteer("john", "murphy","@gmail", "10", "1")
        vol_2 = Volunteer("larry", "obrien","@gmail", "10", "1")
        
        self.assertEqual(vol_1.email, 'john.murphy@gmail.com')
        self.assertEqual(vol_1.email, 'larry.obrien@gmail.com')

        vol_1.first = 'tim'
        vol_2.first = 'gary'

        self.assertEqual(vol_1.email, 'tim.murphy@gmail.com')
        self.assertEqual(vol_1.email, 'gary.obrien@gmail.com')

    def test_TokenBalance(self):
        from tokens.models import Volunteer
        vol_1 = Volunteer("john", "murphy", "10", "1")
        vol_2 = Volunteer("larry", "obrien", "10", "1")

        self.assertTrue(vol_1.TokenBalance, 10)
        self.assertFalse(vol_2.TokenBalance, 20)

        vol_2.tokens = 10

        self.assertTrue(vol_2.TokenBalance, 10)

    def test_TokenTier(self):
        from tokens.models import Volunteer
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

    def test_VolunteerExists(self):
        from tokens.models import Volunteer
        qs = Volunteer.objects.all()
        print(qs)
        self.assertTrue(qs.exists())
        
    def TearDown(self): 
        pass


class Test_Events(TestCase):
    def test_setUp(self):
        pass

    

    def test_EventId(eventId, self):
        from tokens.models import Event 
        Event_1 = Event("23","BagPacking", "03/02/2022", "Tesco", "you will be bag packing!", "6")
        Event_2 = Event("46", "fun run","23/10/2022","St Vincent de pauls", "Run for zambia", "30" )

        self.assertEquals(Event_1.eventId, 23)
        self.assertEquals(Event_2.eventId, 46)

        Event_1.Event = 24

        self.assertEquals(Event_1.Event, 24)

    def test_Date(Eventid, date, self):
        from tokens.models import Event 
        Event_1 = Event("23","BagPacking", "03/02/2022", "Tesco", "you will be bag packing!", "6")
        Event_2 = Event("46", "fun run","23/10/2022","St Vincent de pauls", "Run for zambia", "30" )

        self.assertTrue(Event_1.date, "03/02/2022")
        self.assertFalse(Event_2.date, "22/10/2022")

        Event_2.Eventdate = "23/10/2022"

        self.assertTrue(Event_2.date, "23/10/2022")


    def test_tearDown(self):
        pass
    
    
class test_testOrganisation(TestCase):
    def test_setUp(self):
        pass
    
    def test_OrganisationExists(self):
        from tokens.models import Organisation
        qs = Organisation.objects.all()
        print(qs)
        self.assertTrue(qs.exists())
        
    def test_tearDown(self):
        pass
        

class Test_TokenStatus(TestCase):
    
    def setUp(self):
        pass
    
    def test_UsersState(self):
        
        from tokens.models import VolunteerEvent 
        Userstate1 = VolunteerEvent("john","USER_APPLIED")
        Userstate2 = VolunteerEvent("larry","USER_ADMITTED")
        Userstate3 = VolunteerEvent("tim","USER_APPlIED")
        
        
        self.assertTrue(Userstate1.UserState, "USER_APPLIED")
        self.assertFalse(Userstate2.UserState, "USER_APPLIED")
        self.assertFalse(Userstate3.UserState, "USER_ADMITTED")
        
        Userstate2.UserState = "USER_ADMITTED"
        Userstate3.UserState = "USER_ADMITTED"
        
        self.assertTrue(Userstate2.UserState, "USER_ADMITTED")
        self.assertTrue(Userstate3.UserState, "USER_APPLIED")
        
        
        
        
    def test_TokenState(self):  
        from tokens.models import VolunteerEvent  
        Tokenstate1 =  VolunteerEvent("Kim","TOKENS_REQUESTED")
        Tokenstate2 =  VolunteerEvent("Sarah","TOKENS_APPROVED")
        Tokenstate3 =  VolunteerEvent("Johanna","TOKENS_CLAIMED")
        
        self.assertTrue(Tokenstate1.TokenState, "TOKENS_REQUESTED")
        self.assertTrue(Tokenstate2.TokenState, "TOKENS_APPROVED")
        self.assertFalse(Tokenstate3.TokenState, "TOKENS_APPROVED")
        
        Tokenstate3.TokenState = "TOKENS_CLAIMED"
        
        self.assertTrue(Tokenstate3.TokenState, "TOKENS_CLAIMED")
        
    def TearDown(self):
        pass

    


class testDiscount(TestCase):
    from tokens.models import Discount
    
    def setUp(self):
        pass

    
    def test_RewardCode(self, Charfield):
        Reward1 = Discount('12342', "supermac's coupon", "02/03/2023")
        Reward2 = Discount('12343', "cinema ticket", "04/05/2023")
        Reward3 = Discount('12344', "one for all voucher", "27,04,2023")
        Reward4 = Discount('12345', "Dunnes 20 Percent off!", "27,04,2023")
        
        self.assertTrue(Reward1.Discount, "12342")
        self.assertFalse(Reward2.Discount, "12322")
        self.assertTrue(Reward3.Discount, "12344")
        self.assertFalse(Reward4.Discount, "12332")
        
        Reward2.Discount = "12343"
        Reward4.Discount = "12345"
        
        self.assertTrue(Reward2.Discount, "12343")
        self.assertTrue(Reward4.Discount, "12345")
    
    def test_Expirydate(self):
        ExpiryDate1 = Discount('12342', "supermac's coupon", "02/03/2023")
        ExpiryDate2 = Discount('12343', "cinema ticket", "04/05/2023")
        ExpiryDate3 = Discount('12344', "one for all voucher", "27/04/2023")
        ExpiryDate4 = Discount('12345', "Dunnes 20 Percent off!", "16/02/2023")
        
        self.assertTrue(ExpiryDate1.Discount,"02/03/2023")
        self.assertFalse(ExpiryDate2.Discount,"07/03/2023")
        self.assertTrue(ExpiryDate3.Discount,"27/04/2023")
        self.assertFalse(ExpiryDate4.Discount,"14/04/2023")
        
        ExpiryDate2.Discount = "04/05/2023"
        ExpiryDate4.Discount = "14/04/2023"
        
        self.assertTrue(ExpiryDate2.Discount,"04/05/2023")
        self.assertTrue(ExpiryDate4.Discount,"16/02/2023")


    def TearDown(self):
        pass