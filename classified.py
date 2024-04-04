import datetime as DT
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
driver.implicitly_wait(14)


def wait_a_sec(sec=1.25):
    time.sleep(sec)


def submit(link_text: str, locator_tag='button'):
    driver.find_element(By.XPATH, f"//{locator_tag}[contains(normalize-space(), '{link_text}')]").click()


def login_admin(user_locator: str, passwd_locator: str, user: str, passwd: str):
    username_field = driver.find_element(By.NAME, user_locator)
    password_field = driver.find_element(By.NAME, passwd_locator)
    username_field.send_keys(user)
    password_field.send_keys(passwd)
    submit("Login")


def choose_from_nav(link_text: str):
    driver.find_element(By.LINK_TEXT, link_text).click()


def open_leave_page():
    wait_a_sec()

    leave_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Leave']"))
    )
    leave_link.click()


def choose_from_dropdown(option_text: str):
    driver.find_element(By.XPATH, "//div[contains(text(),'Select')]").click()

    wait_a_sec()

    driver.find_element(By.XPATH, f"//span[contains(text(),'{option_text}')]").click()


def choose_date(date_info: DT.datetime, index: int):
    date_field = driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")[index]
    date_field.click()

    wait_a_sec()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='oxd-calendar-dates-grid']//div[text()='{date_info.day}']")
        )
    ).click()


def comment_for_leave(content: str, from_date: DT.datetime, to_date: DT.datetime):
    comment = f"{content} - from {from_date.date()} to {to_date.date()}"
    driver.find_element(By.XPATH, " //textarea").send_keys(comment)
    return content


def view_details(msg: str):
    driver.find_element(By.XPATH,
                        f"//div[contains(text(),'{msg}')]/parent::div/following-sibling::div/div/li/button").click()

    driver.find_element(By.XPATH, "//p[text() = 'View Leave Details']").click()


