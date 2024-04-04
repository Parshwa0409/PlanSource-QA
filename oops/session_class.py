from base_class import BaseClass
from selenium.webdriver.common.by import By


class SessionClass(BaseClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.username_locator_txt = 'username'
        self.password_locator_txt = 'password'
        self.username = 'Admin'
        self.password = 'admin123'

    def login_admin(self):
        username_field = self.driver.find_element(By.NAME, self.username_locator_txt)
        password_field = self.driver.find_element(By.NAME, self.password_locator_txt)
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        self.click_submit('Login')

    def logout_admin(self):
        self.explicit_wait(self.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.click_submit('Logout', 'a')
