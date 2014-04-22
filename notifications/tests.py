from django.test import TestCase
from notifications.models import Notification
# Create your tests here.
notification1 = Notification(text='Hello',
                             new=True, )
notification2 = Notification(text='Hi',
                             new=False, )
notification3 = Notification(text='Hello',
                             new=False, )
notification4 = Notification(text='Bonjour',
                             new=False, )


def compare_two_notifications(n1=Notification, n2=Notification):
    if n1.text != n2.text:
        return False
    if n1.new != n2.new:
        return False
    return True


class TestNotifications(TestCase):
    def test_notification_is_valid(self):
        self.assertTrue(isinstance(notification1, Notification))
        self.assertTrue(isinstance(notification2, Notification))
        self.assertTrue(isinstance(notification3, Notification))
        self.assertTrue(isinstance(notification4, Notification))

    def test_same_notification_should_be_equal(self):
        self.assertTrue(compare_two_notifications(notification1, notification1))

    def test_different_notification_should_not_be_equal(self):
        self.assertFalse(compare_two_notifications(notification1, notification2))

    def test_different_text_should_not_be_equal(self):
        self.assertFalse(compare_two_notifications(notification1, notification3))

    def test_different_new_should_not_be_equal(self):
        self.assertFalse(compare_two_notifications(notification2, notification4))

