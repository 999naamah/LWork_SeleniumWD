from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ProductPage:
    url_Apple = "http://tutorialsninja.com/demo/index.php?route=product/product&product_id=42"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def url_apple_open(self):
        self.driver.get(self.url_Apple)

    """Ищем информацию о продукте на странице"""

    def get_name_page(self) -> str:
        name_page = self.driver.find_element(By.LINK_TEXT, 'Apple Cinema 30"')
        return name_page.text

    def get_name_brand(self) -> str:
        name_brand = self.driver.find_element(By.CSS_SELECTOR, 'a[href ="http://tutorialsninja.com/demo/index.php'
                                                               '?route=product/manufacturer/info&manufacturer_id=8"]')
        return name_brand.text

    def get_product_code(self) -> str:
        product_code = self.driver.find_element(By.XPATH, '//li[text()="Product Code: Product 15"]')
        return product_code.text[14:24]

    def get_price(self) -> str:
        price = self.driver.find_element(By.XPATH, '//h2[text()="$110.00"]')
        return price.text

    def get_description(self) -> str:
        description = self.driver.find_element(By.XPATH,
                                               '//font[contains(text(), "The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution")]')
        return description.text[0:85]

    """Элементы для добавления отзыва"""

    def click_tab_review(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='#tab-review']").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "button-review")))

    def click_button_continue(self) -> WebElement:
        return self.driver.find_element(By.ID, "button-review").click()

    def click_check_rating(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, 'input[type=radio]:nth-child(4)').click()

    def get_your_name_field(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-name")

    def get_your_review_field(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-review")

        """Предупреждение после ввода"""
    def expected_text_alert(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "alert-dismissible").text




