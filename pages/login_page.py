import time
from pages.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"a[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"input[name='password']")
    BTN_LOGIN = (By.CSS_SELECTOR,"button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"h3")
    LOGOUT_LINK = (By.CSS_SELECTOR,"button[class='navigation-link linklike']")
    OK_BTN = (By.XPATH,"//*[text()='OK']")
    LOGIN_FAILED_MESSAGE = (By.XPATH, "//p[contains(text(), 'Login or Password incorrect')]")


    def open_login_form(self):
        self.click(self.LOGIN_NAV_LINK)
        time.sleep(2)

    def fill_email(self, email):
        self.fill(self.EMAIL_INPUT, email)
        time.sleep(2)

    def fill_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)
        time.sleep(2)

    def click_login_button(self):
        self.driver.find_element(*self.BTN_LOGIN).click()
        time.sleep(2)

    def get_success_message(self):
        # return self.driver.find_element(*self.SUCCESS_MESSAGE).text
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)

        )
        return element.text
    def close_window(self):
        self.click(self.OK_BTN)

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
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.LOGIN_FAILED_MESSAGE)
        )
        return element.text

    def log_out_success(self):
        self.driver.find_element(*self.LOGOUT_LINK).click()


