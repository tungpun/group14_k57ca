from django.test import TestCase
from periods.models import Period
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

class testPeriods(TestCase):

    def testSamePeriodShouldBeEqual(self):
        self.assertTrue(period1.equal(period1))

    def testDiffirentPeriodShouldNotBeEqual(self):
        self.assertFalse(period1.equal(period2))

    def testDiffirentLecturerShouldNotBeEqual(self):
        self.assertFalse(period1.equal(period3))

    def testDiffirentCodeShouldNotBeEqual(self):
        self.assertFalse(period2.equal(period4))
