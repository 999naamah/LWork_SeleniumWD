import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.compare_page import ComparePage


class CompareTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.compare_page = ComparePage(self.driver)
        self.expected_text_success_apple = 'Success: You have added Apple Cinema 30" to your product comparison!'
        self.expected_text_success_samsung = 'Success: You have added Samsung SyncMaster 941BW to your product comparison!'
        self.expected_text_not_chosen = 'You have not chosen any products to compare.'

    def tearDown(self) -> None:
        self.driver.close()

    def testCompareAppleSamsung(self):
        """Добавляем в сравнение Apple"""
        self.compare_page.url_apple_open()
        self.compare_page.click_button_compare_this_product()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,
                                                                                                "alert-success")))
        self.assertEqual(
            self.expected_text_success_apple,
            self.compare_page.alert_success_apple()
        )
        """Добавляем в сравнение Samsung"""

        self.compare_page.url_samsung_open()
        self.compare_page.click_button_compare_this_product()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a[href*="http://tutorialsninja.com/demo/index.php?route'
                              '=product/compare"]')))

        self.compare_page.click_link_product_compare()

        """Проверяем есть ли Apple и Samsung в сравнении"""
        self.assertEqual(
            'Apple Cinema 30"',
            self.compare_page.apple_link_product()
        )
        self.assertEqual(
            'Samsung SyncMaster 941BW',
            self.compare_page.samsung_link_product()
        )

        """Удаляем товар из сравнения"""
        self.compare_page.click_remove_apple_btn()
        self.driver.implicitly_wait(5)
        self.compare_page.click_remove_samsung_btn()
        self.driver.implicitly_wait(5)

        self.assertEqual(
            self.expected_text_not_chosen,
            self.compare_page.text_not_chosen()
        )
