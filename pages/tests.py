from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from . import views


# Create your tests here.
class HomePageTest(SimpleTestCase):

    def setUp(self):

        response = reverse('home')
        self.response = self.client.get('/')

    def test_homepage_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):

        self.assertTemplateUsed(self.response, 'pages/home.html')

    def test_homepage_contains_correct(self):

        self.assertContains(self.response, 'hello nigger')
        self.assertNotContains(self.response, 'i respect niggers')

    def test_homepage_does_not_containts_incorrect_html(self):

        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            views.HomePageView.as_view().__name__
        )

class AboutPageTest(SimpleTestCase):

    def setUp(self):

        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_templates(self):

        self.assertTemplateUsed(self.response, 'pages/about.html')

    def test_aboutpage_contains_correct_html(self):

        self.assertContains(self.response, 'About page')

    def test_aboutpage_resolves_aboutpageview(self):

        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            views.AboutPageView.as_view().__name__
        )