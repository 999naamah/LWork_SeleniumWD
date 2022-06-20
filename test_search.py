import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobject.search_page import SearchPage


class SearchPageTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.apple = "apple"
        self.sony = "sony"
        self.nokia = "nokia"
        self.stunning = "stunning"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.search_page = SearchPage(self.driver)
        self.search_page.url_search_open()

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.close()

    def testApple(self):
        """Поиск Apple"""

        self.search_page.get_search_field().send_keys(self.apple)
        self.search_page.get_search_field_button().click()

        self.assertEqual(
            'Apple Cinema 30"',
            self.search_page.get_name_apple()
        )

        self.assertEqual(
            '$110.00',
            self.search_page.get_price_apple()
        )

    def testSony(self):
        """Поиск Sony"""
        self.search_page.get_search_field().send_keys(self.sony)
        self.search_page.get_search_field_button().click()

        self.assertEqual(
            'Sony VAIO',
            self.search_page.get_name_sony()
        )

        self.assertEqual(
            '$1,202.00',
            self.search_page.get_price_sony()[:9]
        )

    def testNokia(self):
        """Поиск Nokia"""
        self.search_page.get_search_field().send_keys(self.nokia)
        self.search_page.get_search_field_button().click()

        self.assertEqual(
            'There is no product that matches the search criteria.',
            self.search_page.get_name_nokia()
        )

    def testStunning(self):
        """Поиск stunning"""
        self.search_page.search_criteria_field().send_keys(self.stunning)
        self.search_page.checkbox_search_in_product().click()
        self.search_page.button_search_criteria().click()

        self.assertEqual(
            "HP LP3065",
            self.search_page.get_name_HP()
        )

        self.assertEqual(
            "iMac",
            self.search_page.get_name_iMac()
        )
