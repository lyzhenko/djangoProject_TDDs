import unittest
from selenium import webdriver


class NewVisitorTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title, 'Тест пройден')
        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
