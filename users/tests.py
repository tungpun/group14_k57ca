from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

user1 = User(username = 'vuong',
             password = '123',)
user2 = User(username = 'hoang',
             password = '94',)
user3 = User(username = 'hoang',
             password = '456',)
user4 = User(username = 'nguyen',
             password = '123',)

class testUser(TestCase):

    #Test User by models
    def testSameUserShouldBeEqual(self):
        self.assertTrue(user1.equal(user1))

    def testDiffirentUserShouldNotBeEqual(self):
        self.assertFalse(user1.equal(user2))

    def testDiffirentUsernameShouldNotBeEqual(self):
        self.assertFalse(user1.equal(user4))

    def testDiffirentPasswordShouldNotBeEqual(self):
        self.assertFalse(user2.equal(user3))