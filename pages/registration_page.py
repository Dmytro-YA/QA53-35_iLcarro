import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:

    NAV_REGISTRATION_BTN = (By.CSS_SELECTOR,"a[href='/register']")
    NAME_INPUT = (By.CSS_SELECTOR,"input[name='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR,"input[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    YALLA_BTN = (By.XPATH, "//button[text()='Y’alla!']")
    CHECK_BOX = (By.ID, "terms-of-use")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "h3")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error']")
    OK_BTN = (By.XPATH,"//*[text()='OK']")
    BTN_LOGIN = (By.CSS_SELECTOR,"button[type='submit']")
    LOGIN_FAILED_MESSAGE = (By.XPATH, "//p[contains(text(), 'Login or Password incorrect')]")





    def __init__(self, driver):

        self.wait = WebDriverWait(driver, 5)
        self.driver = driver
        

    def open_registration_form(self):
        self.driver.find_element(*self.NAV_REGISTRATION_BTN).click()
        time.sleep(2)

    def fill_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_registration(self):
        self.driver.find_element(*self.YALLA_BTN).click()

    def check_policy(self):
        self.driver.find_element(*self.CHECK_BOX).click()

    def fill_registration_form(self, user):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_password(user.password)

    def confirmation_text(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text

        element = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))

        return element.text

    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

    def is_submit_button_enabled(self):
        return self.driver.find_element(*self.YALLA_BTN).is_enabled()


    def get_error_message(self):
        element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def get_login_failed_message(self):
        element = self.wait.until(EC.visibility_of_element_located(self.LOGIN_FAILED_MESSAGE))
        return element.text