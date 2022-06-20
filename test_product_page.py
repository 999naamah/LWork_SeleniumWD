import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.product_page import ProductPage


class ProductPageTest(unittest.TestCase):
    """"Проверяем что на странице присутсвует Apple Cinema 30"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.name_page = 'Apple Cinema 30"'
        self.name_brand = 'Apple'
        self.product_code = 'Product 15'
        self.price = '$110.00'
        self.description = 'The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution.'
    
    def tearDown(self) -> None:
        self.driver.close()
    
    def testProductInfo(self):
        product_page = ProductPage(self.driver)
        product_page.url_apple_open()


        """Ищем информацию о товаре на странице"""
        self.assertEqual(
            self.name_page,
            product_page.get_name_page()
        )

        self.assertEqual(
            self.name_brand,
            product_page.get_name_brand()
        )

        self.assertEqual(
            self.product_code,
            product_page.get_product_code()
        )

        self.assertEqual(
            self.price,
            product_page.get_price()
        )

        self.assertEqual(
            self.description,
            product_page.get_description()
        )

