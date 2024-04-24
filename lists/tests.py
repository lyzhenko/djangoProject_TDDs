from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class SmokeTest(TestCase):
    """ Тест на токсичность """

    def test_bad_math(self):
        self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):
    """ Тест на главную страницу """

    def test_root_url_resolve_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
