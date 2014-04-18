from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import *
# Create your tests here.

user1 = User(username = 'vuong',
             password = '123',)
user2 = User(username = 'hoang',
             password = '94',)
user3 = User(username = 'hoang',
             password = '456',)
user4 = User(username = 'nguyen',
             password = '123',)

def compareTwoUsers(u1 = User, u2 = User):
        if u1.username != u2.username:
            return False
        if u1.password != u2.password:
            return False
        return True

class testUsers(TestCase):

    def testUserIsValid(self):
        self.assertTrue(isinstance(user1, User))
        self.assertTrue(isinstance(user2, User))
        self.assertTrue(isinstance(user3, User))
        self.assertTrue(isinstance(user4, User))

    def testSamePeriodShouldBeEqual(self):
        self.assertTrue(compareTwoUsers(user1,user1))

    def testDiffirentPeriodShouldNotBeEqual(self):
        self.assertFalse(compareTwoUsers(user1,user2))

    def testDiffirentLecturerShouldNotBeEqual(self):
        self.assertFalse(compareTwoUsers(user1,user3))

    def testDiffirentCodeShouldNotBeEqual(self):
        self.assertFalse(compareTwoUsers(user2,user4))

class testPeriodsForms(TestCase):

    def testValidLoginForm(self):
        content = {
            'username':user1.username,
            'password':user1.password,
        }
        form = LoginForm(data=content)
        self.assertTrue(form.is_valid())

    def testValidRegisterForm(self):
        user = User(username = 'hoangvuong',
                    first_name = 'Vuong',
                    last_name = 'Nguyen',
                    email = 'hoangvuong94st@gmail.com',
                    password = '123456',)
        content = {
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'password': user.password,
        }
        form = RegisterForm(data=content)
        self.assertFalse(form.is_valid())
