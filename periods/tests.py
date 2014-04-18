from django.test import TestCase
from periods.forms import EditPeriodForm
from periods.models import Period
#from django.utils.unittest import *
from periods.views import enroll, edit

period1 = Period(code=2,
                 name='SE',
                 lecturer='TAH',
                 length='3',
                 position='50',)
period2 = Period(code=3,
                 name='OS',
                 lecturer='NTT',
                 length='3',
                 position='20',)
period3 = Period(code=2,
                 name='SE',
                 lecturer='TTMC',
                 length='3',
                 position='50',)
period4 = Period(code=4,
                 name='OS',
                 lecturer='NTT',
                 length='3',
                 position='20',)

def compareTwoPeriods(p1 = Period, p2 = Period):
        if p1.code != p2.code:
            return False
        if p1.name != p2.name:
            return False
        if p1.lecturer != p2.lecturer:
            return False
        if p1.position != p2.position:
            return False
        return True

class testPeriodsModels(TestCase):

    def testPeriodIsValid(self):
        self.assertTrue(isinstance(period1, Period))
        self.assertTrue(isinstance(period2, Period))
        self.assertTrue(isinstance(period3, Period))
        self.assertTrue(isinstance(period4, Period))

    def testSamePeriodShouldBeEqual(self):
        self.assertTrue(compareTwoPeriods(period1,period1))

    def testDiffirentPeriodShouldNotBeEqual(self):
        self.assertFalse(compareTwoPeriods(period1,period2))

    def testDiffirentLecturerShouldNotBeEqual(self):
        self.assertFalse(compareTwoPeriods(period1,period3))

    def testDiffirentCodeShouldNotBeEqual(self):
        self.assertFalse(compareTwoPeriods(period2,period4))

class testPeriodsForms(TestCase):

    def testValidForm(self):
        content = {
            'code':period1.code,
            'name':period1.name,
            'lecturer':period1.lecturer,
            'length':period1.length,
            'position':period1.position,
        }
        form = EditPeriodForm(data=content)
        self.assertFalse(form.is_valid())

