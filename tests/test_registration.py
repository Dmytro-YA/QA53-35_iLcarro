import random
import uuid

from data.user_data import create_user
from models.user import User
from pages import login_page
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    # random_suffix = random.randint(1, 1000000)
    random_suffix = uuid.uuid4().hex[:8]

    user = create_user( )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registered"
    registration_page.close_window()

def test_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)


    user = create_user(name="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Name is required"


def test_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)


    user = create_user(last_name="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Last name is required"

def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)


    user = create_user(email="tony@gmail")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Wrong email format"

def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)


    user = create_user(email="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Email is required"

def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)


    user = create_user(password="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Password is required"

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)


    user = create_user(password="123")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Password must contain minimum 6 symbols"

def test_registration_without_checkbox(driver):
    registration_page = RegistrationPage(driver)


    user = create_user()

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()

    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "You must accept the terms"