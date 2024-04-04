from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.ID = "id"
        self.XPATH = "xpath"
        self.LINK_TEXT = "link text"
        self.PARTIAL_LINK_TEXT = "partial link text"
        self.NAME = "name"
        self.TAG_NAME = "tag name"
        self.CLASS_NAME = "class name"
        self.CSS_SELECTOR = "css selector"


    def chrome_driver(self):
        return self.driver

    def current_url(self):
        return self.driver.current_url

    def implicit_wait(self, sec=7):
        self.driver.implicitly_wait(sec)

    def explicit_wait(self, locator_tag, locator, multiple=False) -> WebElement or TimeoutException or NoSuchElementException:
        if not multiple:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator_tag, locator))
            )
        else:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((locator_tag, locator))
            )

    def click_submit(self, link_text: str, locator_tag='button'):
        self.driver.find_element(self.XPATH, f"//{locator_tag}[contains(normalize-space(), '{link_text}')]").click()
