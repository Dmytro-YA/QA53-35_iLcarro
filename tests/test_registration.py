import random
import uuid

from models.user import User
from pages import login_page
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    # random_suffix = random.randint(1, 1000000)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        "Tonny",
        "Yalla",
        f"tony_{random_suffix}11111@gmail.com",
        "Test@123456"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registered"
    registration_page.close_window()

def test_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)


    user = User(
        "",
        "Yalla",
        f"tony11111@gmail.com",
        "Test@123456"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Name is required"


def test_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)


    user = User(
        "Tony",
        "",
        f"tony11111@gmail.com",
        "Test@123456"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Last name is required"

def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)


    user = User(
        "Tony",
        "Yalla",
        f"tony11111gmail.com",
        "Test@123456"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Wrong email format"

def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)


    user = User(
        "Tony",
        "Yalla",
        "",
        "Test@123456"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Email is required"

def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)


    user = User(
        "Tony",
        "Yalla",
        "tony@gmail.com",
        ""
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Password is required"

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)


    user = User(
        "Tony",
        "Yalla",
        "tony@gmail.com",
        "P123"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "Password must contain minimum 6 symbols"

def test_registration_without_checkbox(driver):
    registration_page = RegistrationPage(driver)


    user = User(
        "Tony",
        "Yalla",
        "tony@gmail.com",
        "P123@123s"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()

    assert not registration_page.is_submit_button_enabled()
    assert registration_page.get_error_message() == "You must accept the terms"