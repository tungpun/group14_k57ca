"""Unit tests go here"""
from django.test import TestCase
from periods.forms import EditPeriodForm
from periods.models import Period
# Create your tests here.

PERIOD1 = Period(code=2,
                 name='SE',
                 lecturer='TAH',
                 length='3',
                 position='50', )
PERIOD2 = Period(code=3,
                 name='OS',
                 lecturer='NTT',
                 length='3',
                 position='20', )
PERIOD3 = Period(code=2,
                 name='SE',
                 lecturer='TTMC',
                 length='3',
                 position='50', )
PERIOD4 = Period(code=4,
                 name='OS',
                 lecturer='NTT',
                 length='3',
                 position='20', )


def compare_two_periods(p1=Period, p2=Period):
    """
    2 periods are equal if they have the same code, name, lecturer and position
    Different otherwise
    """
    if p1.code != p2.code:
        return False
    if p1.name != p2.name:
        return False
    if p1.lecturer != p2.lecturer:
        return False
    if p1.position != p2.position:
        return False
    return True


class TestPeriodsModels(TestCase):
    """Different test cases for periods"""
    def test_period_is_valid(self):
        """Check if period is valid"""
        self.assertTrue(isinstance(PERIOD1, Period))
        self.assertTrue(isinstance(PERIOD2, Period))
        self.assertTrue(isinstance(PERIOD3, Period))
        self.assertTrue(isinstance(PERIOD4, Period))

    def test_same_period_should_be_equal(self):
        """A period is equal to itself"""
        self.assertTrue(compare_two_periods(PERIOD1, PERIOD1))

    def test_different_period_should_not_be_equal(self):
        """Periods with different properties are different"""
        self.assertFalse(compare_two_periods(PERIOD1, PERIOD2))

    def test_different_lecturer_should_not_be_equal(self):
        """Periods with different lecturers are different"""
        self.assertFalse(compare_two_periods(PERIOD1, PERIOD3))

    def test_different_code_should_not_be_equal(self):
        """Periods with different code are different"""
        self.assertFalse(compare_two_periods(PERIOD2, PERIOD4))


class TestPeriodsForms(TestCase):
    """Check validation of period forms"""
    def test_valid_form(self):
        """check if form is valid"""
        content = {
            'code': PERIOD1.code,
            'name': PERIOD1.name,
            'lecturer': PERIOD1.lecturer,
            'length': PERIOD1.length,
            'position': PERIOD1.position,
        }
        form = EditPeriodForm(data=content)
        self.assertFalse(form.is_valid())

