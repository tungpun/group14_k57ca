from django.test import TestCase
from periods.forms import EditPeriodForm
from periods.models import Period
# Create your tests here.

period1 = Period(code=2,
                 name='SE',
                 lecturer='TAH',
                 length='3',
                 position='50', )
period2 = Period(code=3,
                 name='OS',
                 lecturer='NTT',
                 length='3',
                 position='20', )
period3 = Period(code=2,
                 name='SE',
                 lecturer='TTMC',
                 length='3',
                 position='50', )
period4 = Period(code=4,
                 name='OS',
                 lecturer='NTT',
                 length='3',
                 position='20', )


def compare_two_periods(p1=Period, p2=Period):
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
    def test_period_is_valid(self):
        self.assertTrue(isinstance(period1, Period))
        self.assertTrue(isinstance(period2, Period))
        self.assertTrue(isinstance(period3, Period))
        self.assertTrue(isinstance(period4, Period))

    def test_same_period_should_be_equal(self):
        self.assertTrue(compare_two_periods(period1, period1))

    def test_different_period_should_not_be_equal(self):
        self.assertFalse(compare_two_periods(period1, period2))

    def test_different_lecturer_should_not_be_equal(self):
        self.assertFalse(compare_two_periods(period1, period3))

    def test_different_code_should_not_be_equal(self):
        self.assertFalse(compare_two_periods(period2, period4))


class TestPeriodsForms(TestCase):
    def test_valid_form(self):
        content = {
            'code': period1.code,
            'name': period1.name,
            'lecturer': period1.lecturer,
            'length': period1.length,
            'position': period1.position,
        }
        form = EditPeriodForm(data=content)
        self.assertFalse(form.is_valid())

