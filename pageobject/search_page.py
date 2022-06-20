from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class SearchPage:
    url_search = "http://tutorialsninja.com/demo/index.php?route=product/search"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def url_search_open(self):
        self.driver.get(self.url_search)

    def get_search_field(self) -> WebElement:
        return self.driver.find_element(By.NAME, "search")

    def get_search_field_button(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, '#search > span')

    def get_name_apple(self) -> str:
        return self.driver.find_element(By.LINK_TEXT, 'Apple Cinema 30"').text

    def get_price_apple(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, '.price > .price-new').text

    def get_name_sony(self) -> str:
        return self.driver.find_element(By.LINK_TEXT, 'Sony VAIO').text

    def get_price_sony(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, 'price').text

    def get_name_nokia(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, '#content > p:nth-child(7)').text

    def search_criteria_field(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-search")

    def checkbox_search_in_product(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, '.checkbox-inline > [name=description]')

    def button_search_criteria(self) -> WebElement:
        return self.driver.find_element(By.ID, 'button-search')

    def get_name_HP(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, 'div.caption > h4 > a').text

    def get_name_iMac(self) -> str:
        return self.driver.find_element(By.LINK_TEXT, 'iMac').text




