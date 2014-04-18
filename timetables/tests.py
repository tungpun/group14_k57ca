from django.test import TestCase
from timetables.models import Timetable
from timetables.forms import InsertTimetableForm
# Create your tests here.

timetable1 = Timetable(code = 1,
                       name = 'Semester1',)
timetable2 = Timetable(code = 2,
                       name = 'Semester2',)
timetable3 = Timetable(code = 3,
                       name = 'Semester2',)
timetable4 = Timetable(code = 1,
                       name = 'Semester4',)

def compareTwoTimetables(t1 = Timetable, t2 = Timetable):
        if t1.code != t2.code:
            return False
        if t1.name != t2.name:
            return False
        return True

class testTimetablesModels(TestCase):

    def testTimetableIsValid(self):
        self.assertTrue(isinstance(timetable1, Timetable))
        self.assertTrue(isinstance(timetable2, Timetable))
        self.assertTrue(isinstance(timetable3, Timetable))
        self.assertTrue(isinstance(timetable4, Timetable))

    def testSamePeriodShouldBeEqual(self):
        self.assertTrue(compareTwoTimetables(timetable1, timetable1))

    def testDiffirentPeriodShouldNotBeEqual(self):
        self.assertFalse(compareTwoTimetables(timetable1, timetable2))

    def testDiffirentLecturerShouldNotBeEqual(self):
        self.assertFalse(compareTwoTimetables(timetable1, timetable3))

    def testDiffirentCodeShouldNotBeEqual(self):
        self.assertFalse(compareTwoTimetables(timetable2, timetable4))

class testTimetablesForms(TestCase):

    def testValidForm(self):
        content = {
            'code':timetable1.code,
            'name':timetable1.name,
        }
        form = InsertTimetableForm(data=content)
        self.assertTrue(form.is_valid())
