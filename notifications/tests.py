from django.test import TestCase
from notifications.models import Notification
# Create your tests here.
notification1 = Notification(text = 'Hello',
                             new = True,)
notification2 = Notification(text = 'Hi',
                             new = False,)
notification3 = Notification(text = 'Hello',
                             new = False,)
notification4 = Notification(text = 'Bonjour',
                             new = False,)

def compareTwoNotifications(n1 = Notification, n2 = Notification):
        if n1.text != n2.text:
            return False
        if n1.new != n2.new:
            return False
        return True

class testNotifications(TestCase):

    def testNotificationIsValid(self):
        self.assertTrue(isinstance(notification1, Notification))
        self.assertTrue(isinstance(notification2, Notification))
        self.assertTrue(isinstance(notification3, Notification))
        self.assertTrue(isinstance(notification4, Notification))

    def testSameNotificationShouldBeEqual(self):
        self.assertTrue(compareTwoNotifications(notification1,notification1))

    def testDiffirentNotificationShouldNotBeEqual(self):
        self.assertFalse(compareTwoNotifications(notification1,notification2))

    def testDiffirentTextShouldNotBeEqual(self):
        self.assertFalse(compareTwoNotifications(notification1,notification3))

    def testDiffirentNewShouldNotBeEqual(self):
        self.assertFalse(compareTwoNotifications(notification2,notification4))

