
from pages.login_page import LoginPage

VALID_EMAIL = "yakubdmitriy@gmail.com"
VALID_PASSWORD = "Yakub123*"

def test_login_success(driver):
    login_page = LoginPage(driver)
    driver.maximize_window()
    driver.implicitly_wait(3)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.click_login_button()

