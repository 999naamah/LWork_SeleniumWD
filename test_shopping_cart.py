import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.shopping_cart_page import ShoppingCartPage


class ShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.shopping_cart_page = ShoppingCartPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def testSamsungAndAppleCart(self):

        """Добавляем Samsung"""
        self.shopping_cart_page.url_samsung_open()
        self.shopping_cart_page.get_qty_field().clear()
        self.shopping_cart_page.get_qty_field().send_keys("2")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "button-cart")))
        self.shopping_cart_page.click_add_to_card()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert-success")))

        self.assertEqual(
            "Success: You have added Samsung SyncMaster 941BW to your shopping cart!",
            self.shopping_cart_page.alert_success()
        )

        """Добавляем HP"""
        self.shopping_cart_page.url_HP_open()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "button-cart")))
        self.shopping_cart_page.click_add_to_card()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert-success")))

        self.assertEqual(
            "Success: You have added HP LP3065 to your shopping cart!",
            self.shopping_cart_page.alert_success()
        )

        """Проверяем товар в корзине"""

        self.shopping_cart_page.url_cart_open()

        self.assertEqual(
            'Samsung SyncMaster 941BW',
            self.shopping_cart_page.get_samsung_text()
        )

        self.assertEqual(
            'HP LP3065',
            self.shopping_cart_page.get_HP_text()
        )

        self.assertEqual(
            "$606.00",
            self.shopping_cart_page.get_sum_card()
        )

        """Удаляем товар из корзины"""
        self.shopping_cart_page.click_remove()
        sleep(5)
        self.shopping_cart_page.click_remove()
        sleep(5)

        self.assertEqual(
            "Your shopping cart is empty!",
            self.shopping_cart_page.empty_card_text()
        )

