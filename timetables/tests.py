from django.test import TestCase
from timetables.models import Timetable
from timetables.forms import InsertTimetableForm
# Create your tests here.

timetable1 = Timetable(code=1,
                       name='Semester1', )
timetable2 = Timetable(code=2,
                       name='Semester2', )
timetable3 = Timetable(code=3,
                       name='Semester2', )
timetable4 = Timetable(code=1,
                       name='Semester4', )


def compare_two_timetables(t1=Timetable, t2=Timetable):
    if t1.code != t2.code:
        return False
    if t1.name != t2.name:
        return False
    return True


class TestTimetablesModels(TestCase):
    def test_timetable_is_valid(self):
        self.assertTrue(isinstance(timetable1, Timetable))
        self.assertTrue(isinstance(timetable2, Timetable))
        self.assertTrue(isinstance(timetable3, Timetable))
        self.assertTrue(isinstance(timetable4, Timetable))

    def test_same_period_should_be_equal(self):
        self.assertTrue(compare_two_timetables(timetable1, timetable1))

    def test_different_period_should_not_be_equal(self):
        self.assertFalse(compare_two_timetables(timetable1, timetable2))

    def test_different_lecturer_should_not_be_equal(self):
        self.assertFalse(compare_two_timetables(timetable1, timetable3))

    def test_different_code_should_not_be_equal(self):
        self.assertFalse(compare_two_timetables(timetable2, timetable4))


class TestTimetablesForms(TestCase):
    def test_valid_form(self):
        content = {
            'code': timetable1.code,
            'name': timetable1.name,
        }
        form = InsertTimetableForm(data=content)
        self.assertTrue(form.is_valid())
