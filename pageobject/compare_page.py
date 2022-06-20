from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class ComparePage:
    url_Apple = "http://tutorialsninja.com/demo/index.php?route=product/product&product_id=42"
    url_Samsung = "http://tutorialsninja.com/demo/index.php?route=product/product&product_id=33"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def url_apple_open(self):
        self.driver.get(self.url_Apple)

    def url_samsung_open(self):
        self.driver.get(self.url_Samsung)

    def click_button_compare_this_product(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, "div.btn-group > button:nth-child(2) > i").click()

    def click_link_product_compare(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, 'a[href*="http://tutorialsninja.com/demo/index.php?route'
                                                         '=product/compare"]').click()

    """Удаляем товар из сравнения"""

    def click_remove_apple_btn(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, 'a[href *= "remove=42"]').click()
        self.driver.implicitly_wait(5)

    def click_remove_samsung_btn(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, 'a[href *= "remove=33"]').click()

    """Alert-success"""

    def alert_success_apple(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "alert-success").text[0:-2]

    def alert_success_samsung(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "alert-success").text

    def apple_link_product(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a').text

    def samsung_link_product(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, 'td:nth-child(3) > a').text

    def text_not_chosen(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, "#content >p").text
