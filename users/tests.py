from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class testUser(TestCase):

    #Test User by models
    def testUserModels(self):
        testUsername = 'vuong'
        testPassword = '123456'

        newUser = User(username = testUsername,
                       password = testPassword,)

        self.assertEqual(newUser.username, testUsername)
        self.assertEqual(newUser.password, testPassword)