from selenium.webdriver.common.by import By


class LoginPage:

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"a[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"input[name='password']")
    BTN_LOGIN = (By.CSS_SELECTOR,"button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"a[class='btn btn--primary']")
    LOGOUT_LINK = (By.CSS_SELECTOR,"button[class='navigation-link linklike']")

    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()

    def fill_email(self, email):
        field = self.driver.find_element(*self.EMAIL_INPUT)
        field.clear()
        field.send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.BTN_LOGIN).click()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text
