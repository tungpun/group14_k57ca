from django.test import TestCase
from timetables.models import Timetable
# Create your tests here.

timetable1 = Timetable(code = 1,
                       name = 'Semester1',)
timetable2 = Timetable(code = 2,
                       name = 'Semester2',)
timetable3 = Timetable(code = 3,
                       name = 'Semester2',)
timetable4 = Timetable(code = 1,
                       name = 'Semester4',)

class testTimetable(TestCase):

    # Test Timetable by models
    def testSameTimetableShouldBeEqual(self):
        self.assertTrue(timetable1.equal(timetable1))

    def testDiffirentTimetableShoulNotdBeEqual(self):
        self.assertTrue(timetable1.equal(timetable2))

    def testDiffirenttCodeShoulNotdBeEqual(self):
        self.assertTrue(timetable2.equal(timetable3))

    def testDiffirenttNameShoulNotdBeEqual(self):
        self.assertTrue(timetable1.equal(timetable4))
