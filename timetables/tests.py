from django.test import TestCase
from timetables.models import Timetable
# Create your tests here.

class testTimetable(TestCase):

    # Test Timetable by models
    def testTimetableModels(self):
        testCode = '1'
        testName = 'Semeser 1'
        testOwner = 1

        newTimetable = Timetable(code = testCode,
                                 name = testName,
                                 owner = testOwner,)

        self.assertEqual(newTimetable.code, testCode)
        self.assertEqual(newTimetable.name, testName)
        self.assertEqual(newTimetable.owner, testOwner)