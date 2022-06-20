from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ShoppingCartPage:
    url_HP = "http://tutorialsninja.com/demo/index.php?route=product/product&product_id=47"
    url_Samsung = "http://tutorialsninja.com/demo/index.php?route=product/product&product_id=33"
    url_Cart = "http://tutorialsninja.com/demo/index.php?route=checkout/cart"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def url_HP_open(self):
        self.driver.get(self.url_HP)

    def url_samsung_open(self):
        self.driver.get(self.url_Samsung)

    def url_cart_open(self):
        self.driver.get(self.url_Cart)

    def get_qty_field(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-quantity")

    def click_add_to_card(self) -> WebElement:
        return self.driver.find_element(By.ID, "button-cart").click()

    def alert_success(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "alert-success").text[0:-2]

    """Проверяем наличие товара в корзине"""

    def get_samsung_text(self) -> str:
        return self.driver.find_element(By.LINK_TEXT, "Samsung SyncMaster 941BW").text

    def get_HP_text(self) -> str:
        return self.driver.find_element(By.LINK_TEXT, "HP LP3065").text

    def get_sum_card(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, "#content > div.row > div > table > tbody > tr:nth-child(4) > "
                                                         "td:nth-child(2)").text

    """Удаляем товар из корзины"""

    def click_remove(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(4) > div > span > button.btn.btn-danger").click()

    def empty_card_text(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, "#content > p").text
