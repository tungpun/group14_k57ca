from django.test import TestCase
from notifications.models import Notification
# Create your tests here.

class testNotification(TestCase):


    # Test Notification by models
    def testNotificationModels(self):
        # Create new notification
        testText = 'The first notification!!!'
        testUserID = 2
        testNew = True

        newNotification = Notification(text = testText,
                                        userID = testUserID,
                                        new = testNew, )

        self.assertEqual(newNotification.text, testText)
        self.assertEqual(newNotification.userID, testUserID)
        self.assertEqual(newNotification.new, testNew)
