# pylint: disable=no-member, unexpected-keyword-arg, too-many-public-methods,
# pylint: too-few-public-methods, import-error, relative-import
from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import *
# Create your tests here.

USER1 = User(username='vuong',
             password='123',)
USER2 = User(username='hoang',
             password='94',)
USER3 = User(username='hoang',
             password='456',)
USER4 = User(username='nguyen',
             password='123',)


def compare_two_users(u1=User, u2=User):
    """
    2 users are different only with unique username and password
    """
    if u1.username != u2.username:
        return False
    if u1.password != u2.password:
        return False
    return True


class TestUsers(TestCase):
    """User unit tests"""
    def test_user_is_valid(self):
        """Check if user is valid"""
        self.assertTrue(isinstance(USER1, User))
        self.assertTrue(isinstance(USER2, User))
        self.assertTrue(isinstance(USER3, User))
        self.assertTrue(isinstance(USER4, User))

    def test_same_user_should_be_equal(self):
        """User is equal to him/herself"""
        self.assertTrue(compare_two_users(USER1, USER1))

    def test_different_user_should_not_be_equal(self):
        """Users with different properties are different"""
        self.assertFalse(compare_two_users(USER1, USER2))

    def test_different_username_should_not_be_equal(self):
        """Users with different username are different"""
        self.assertFalse(compare_two_users(USER1, USER3))

    def test_different_password_should_not_be_equal(self):
        """Users withd different password are different"""
        self.assertFalse(compare_two_users(USER2, USER4))


class TestPeriodsForms(TestCase):
    """Period form unit tests"""
    def test_valid_login_form(self):
        """Check if login form is valid"""
        content = {
            'username': USER1.username,
            'password': USER1.password,
        }
        form = LoginForm(data=content)
        self.assertTrue(form.is_valid())

    def test_valid_register_form(self):
        """Check if register form is valid"""
        user = User(username='hoangvuong',
                    first_name='Vuong',
                    last_name='Nguyen',
                    email='hoangvuong94st@gmail.com',
                    password='123456',)
        content = {
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'password': user.password,
        }
        form = RegisterForm(data=content)
        self.assertFalse(form.is_valid())
