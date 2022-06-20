import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.product_page import ProductPage


class AddReviewTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product_page = ProductPage(self.driver)
        self.product_page.url_apple_open()
        self.expected_text_alert_0_symbol = "Warning: Please select a review rating!"
        self.expected_text_alert_24_symbol = "Warning: Review Text must be between 25 and 1000 characters!"
        self.expected_text_accept = "Thank you for your review. It has been submitted to the webmaster for approval."
        self.name = "John"
        self.symbol_24_text = "123456789qwertyuioasdfgh"
        self.symbol_25_text = "123456789qwertyuioasdfgh+"

    def tearDown(self) -> None:
        self.driver.close()

        """Пустой ввод данных"""
    def testReview_1(self):
        self.product_page.click_tab_review()
        self.product_page.click_button_continue()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert-dismissible")))

        self.assertEqual(
            self.expected_text_alert_0_symbol,
            self.product_page.expected_text_alert()
        )

        """Неправильный ввод (рейтинг + 24 символа)"""
    def testTapRatingError(self):
        self.product_page.click_tab_review()
        self.product_page.click_check_rating()
        self.product_page.get_your_name_field().send_keys(self.name)
        self.product_page.get_your_review_field().send_keys(self.symbol_24_text)
        self.product_page.click_button_continue()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert-dismissible")))

        self.assertEqual(
            self.expected_text_alert_24_symbol,
            self.product_page.expected_text_alert()
        )

        """Правильный ввод (рейтинг + 25 символов)"""
    def testTapRatingNormal(self):
        self.product_page.click_tab_review()
        self.product_page.click_check_rating()
        self.product_page.get_your_name_field().send_keys(self.name)
        self.product_page.get_your_review_field().send_keys(self.symbol_25_text)
        self.product_page.click_button_continue()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert-dismissible")))

        self.assertEqual(
            self.expected_text_accept,
            self.product_page.expected_text_alert()
        )
