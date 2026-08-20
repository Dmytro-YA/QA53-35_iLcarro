import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"a[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"input[name='password']")
    BTN_LOGIN = (By.CSS_SELECTOR,"button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"h3")
    LOGOUT_LINK = (By.CSS_SELECTOR,"button[class='navigation-link linklike']")
    OK_BTN = (By.XPATH,"//*[text()='OK']")
    LOGIN_FAILED_MESSAGE = (By.XPATH, "//p[contains(text(), 'Login or Password incorrect')]")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()


    def fill_email(self, email):
        field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))        
        field.clear()
        field.send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.BTN_LOGIN).click()

    def get_success_message(self):
        # return self.driver.find_element(*self.SUCCESS_MESSAGE).text
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)

        )
        return element.text
    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

    def is_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.LOGOUT_LINK)
            )
            return True
        except TimeoutException:
            return False

    def is_login_button_enabled(self):
        return self.driver.find_element(*self.BTN_LOGIN).is_enabled()

    def get_login_failed_message(self):
        element = self.wait.until(EC.visibility_of_element_located(self.LOGIN_FAILED_MESSAGE))
        return element.text

    def log_out_success(self):
        self.driver.find_element(*self.LOGOUT_LINK).click()


