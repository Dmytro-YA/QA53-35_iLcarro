import time

from pages.login_page import LoginPage

VALID_EMAIL = "yakubdmitriy@gmail.com"
VALID_PASSWORD = "Yakub123*"
INVALID_EMAIL = "yakubdmitriygmail.com"
INVALID_PASSWORD = "Yakub123"

def test_login_success(driver):
    login_page = LoginPage(driver)

    driver.implicitly_wait(3)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.click_login_button()
    assert login_page.get_success_message() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True
    login_page.log_out_success()

def test_email_error(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)

    assert not login_page.is_login_button_enabled()

def test_password_error(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.click_login_button()
    assert login_page.get_login_failed_message() == '"Login or Password incorrect"'

def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password("")
    assert not login_page.is_login_button_enabled()


