from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from . import forms
from . import views

# Create your tests here.
class CustomUserTest(TestCase):

    def test_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(
            username='will_smith',
            email='will@gmail.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'will_smith')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@gmail.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

class SignUpPageTests(TestCase):

    def setUp(self):

        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):

        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertNotContains(self.response, 'i respect niggers')

    def test_signup_view(self):

        view = resolve('/signup/')
        self.assertEqual(
            view.func.__name__,
            views.SignUpPageView.as_view().__name__
        )
