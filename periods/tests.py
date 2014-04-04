from django.test import TestCase
from periods.models import Period
from periods.views import get, edit

class test_Periods(TestCase):

    # Test function Period on models
    def test_part_of_period(self):
        code = 3
        name = 'Kien truc may tinh'
        lecturer = 'sonpb'
        length = '5'
        position = '31'

        period = Period(code=code,
                         name=name,
                         lecturer=lecturer,
                         length=length,
                         position=position,)

        self.assertEqual(period.name, name)
        self.assertEqual(period.lecturer, lecturer)
        self.assertEqual(period.position, position)
        self.assertEqual(period.length, length)
