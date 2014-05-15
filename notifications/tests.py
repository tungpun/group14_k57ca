"""Unit tests go here"""
from django.test import TestCase
from notifications.models import Notification
# Create your tests here.
NOTIFICATION1 = Notification(text='Hello',
                             new=True, )
NOTIFICATION2 = Notification(text='Hi',
                             new=False, )
NOTIFICATION3 = Notification(text='Hello',
                             new=False, )
NOTIFICATION4 = Notification(text='Bonjour',
                             new=False, )


def compare_notifications(self=Notification, other=Notification):
    """
    If 2 notifications have the same text, they are equal (return TRUE)
    Otherwise, they are different (return FALSE)
    """
    if self.text != other.text:
        return False
    if self.new != other.new:
        return False
    return True


class TestNotifications(TestCase):
    """Notification testing"""
    def test_notification_is_valid(self):
        """Check whether notification is valid"""
        self.assertTrue(isinstance(NOTIFICATION1, Notification))
        self.assertTrue(isinstance(NOTIFICATION2, Notification))
        self.assertTrue(isinstance(NOTIFICATION3, Notification))
        self.assertTrue(isinstance(NOTIFICATION4, Notification))

    def test_same_notification_should_be_equal(self):
        """Whether the same notification equal to itself"""
        self.assertTrue(compare_notifications(NOTIFICATION1, NOTIFICATION1))

    def test_different_notification_should_not_be_equal(self):
        """Notification with different text will not be equal"""
        self.assertFalse(compare_notifications(NOTIFICATION1, NOTIFICATION2))

    def test_different_text_should_not_be_equal(self):
        """Old and new notifications will not be equal """
        self.assertFalse(compare_notifications(NOTIFICATION1, NOTIFICATION3))

    def test_different_new_should_not_be_equal(self):
        """Notification with different text and age will not be equal"""
        self.assertFalse(compare_notifications(NOTIFICATION2, NOTIFICATION4))

