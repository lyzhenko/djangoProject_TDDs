from django.http import HttpRequest
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

    def test_home_page_returns_correct_html(self):
        """ Тест: Домашняя страница возвращает правильный HTML """

        requests = HttpRequest()
        responses = home_page(requests)
        html = responses.content.decode('utf-8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do List</title>', html)
        self.assertTrue(html.endswith('</html>'))
