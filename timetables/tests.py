"""Unit tests go here"""
from django.test import TestCase
from timetables.models import Timetable
from timetables.forms import InsertTimetableForm
# Create your tests here.

TIMETABLE1 = Timetable(code=1,
                       name='Semester1', )
TIMETABLE2 = Timetable(code=2,
                       name='Semester2', )
TIMETABLE3 = Timetable(code=3,
                       name='Semester2', )
TIMETABLE4 = Timetable(code=1,
                       name='Semester4', )


def compare_two_timetables(t1=Timetable, t2=Timetable):
    """Define way to compare 2 timetables"""
    if t1.code != t2.code:
        return False
    if t1.name != t2.name:
        return False
    return True


class TestTimetablesModels(TestCase):
    """Test cases for checking timetables"""
    def test_timetable_is_valid(self):
        """Check timetable validation"""
        self.assertTrue(isinstance(TIMETABLE1, Timetable))
        self.assertTrue(isinstance(TIMETABLE2, Timetable))
        self.assertTrue(isinstance(TIMETABLE3, Timetable))
        self.assertTrue(isinstance(TIMETABLE4, Timetable))

    def test_same_period_should_be_equal(self):
        """A timetable is equal to itself"""
        self.assertTrue(compare_two_timetables(TIMETABLE1, TIMETABLE1))

    def test_different_period_should_not_be_equal(self):
        """Timetables with different properties are not equal"""
        self.assertFalse(compare_two_timetables(TIMETABLE1, TIMETABLE2))

    def test_different_semester_should_not_be_equal(self):
        """Timetables of different semester are different"""
        self.assertFalse(compare_two_timetables(TIMETABLE1, TIMETABLE3))

    def test_different_code_should_not_be_equal(self):
        """Timetables with different code are different"""
        self.assertFalse(compare_two_timetables(TIMETABLE2, TIMETABLE4))


class TestTimetablesForms(TestCase):
    """Timetable form validation checking"""
    def test_valid_form(self):
        """Check validation of timetable form"""
        content = {
            'code': TIMETABLE1.code,
            'name': TIMETABLE1.name,
        }
        form = InsertTimetableForm(data=content)
        self.assertTrue(form.is_valid())
