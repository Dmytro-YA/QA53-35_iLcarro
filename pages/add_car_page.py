import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from pages.base_page import BasePage


class AddCarPage(BasePage):
    CAR_WORK_URL = "https://icarro-v1.netlify.app/let-car-work"
    CAR_WORK_BTN = (By.CSS_SELECTOR, "[href='/let-car-work']")
    CITY_INPUT = (By.ID, "city")
    MANUFACTURE_INPUT = (By.CSS_SELECTOR, "[name='manufacture']")
    MODEL_INPUT = (By.CSS_SELECTOR, "[name='model']")
    YEAR_INPUT = (By.CSS_SELECTOR, "[name='year']")
    FUEL_SELECT = (By.CSS_SELECTOR, "[name='fuel']")
    GEAR_SELECT = (By.CSS_SELECTOR, "[name='gear']")
    WD_SELECT = (By.CSS_SELECTOR, "[name='wheelsDrive']")
    SEATS_INPUT = (By.CSS_SELECTOR, "[name='seats']")
    CAR_CLASS_INPUT = (By.CSS_SELECTOR, "[name='carClass']")
    SERIAL_NUMBER_INPUT = (By.CSS_SELECTOR, "[name='serialNumber']")
    PRICE_INPUT = (By.CSS_SELECTOR, "[name='pricePerDay']")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error']")
    PHOTO_FILE_INPUT = (By.ID, "photo-file")


    def open_car_form(self):
        self.driver.get(self.CAR_WORK_URL)
        time.sleep(2)

    def fill_city(self, city):
        self.fill(self.CITY_INPUT, city)

        # option_locator = (By.CSS_SELECTOR, f"option[value='{city}']")
        option_locator = (By.CSS_SELECTOR, f"[data-testid='city-option'][data-value='{city}']")

        option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(option_locator)
        )
        option.click()
        time.sleep(0.5)

    def fill_manufacture(self, manufacture):
        self.fill(self.MANUFACTURE_INPUT, manufacture)
        time.sleep(0.5)

    def fill_model(self, model):
        self.fill(self.MODEL_INPUT, model)
        time.sleep(0.5)

    def fill_year(self, year):
        self.fill(self.YEAR_INPUT, year)
        time.sleep(0.5)

    def select_fuel(self, fuel):
        Select(self.find(self.FUEL_SELECT)).select_by_visible_text(fuel)
        time.sleep(0.5)

    def select_gear(self, gear):
        Select(self.find(self.GEAR_SELECT)).select_by_visible_text(gear)
        time.sleep(0.5)

    def select_wheels_drive(self, wheels_drive):
        Select(self.find(self.WD_SELECT)).select_by_visible_text(wheels_drive)
        time.sleep(0.5)

    def fill_seats(self, seats):
        self.fill(self.SEATS_INPUT, seats)
        time.sleep(0.5)

    def fill_car_class(self, car_class):
        self.fill(self.CAR_CLASS_INPUT, car_class)
        time.sleep(0.5)

    def fill_serial_number(self, serial_number):
        self.fill(self.SERIAL_NUMBER_INPUT, serial_number)
        time.sleep(0.5)

    def fill_price(self, price):
        self.fill(self.PRICE_INPUT, price)
        time.sleep(0.5)

    def submit_car_form(self):
        self.click(self.SUBMIT_BTN)
        time.sleep(2)

    def fill_car_form(self, car):
        self.fill_city(car.city)
        self.fill_manufacture(car.manufacture)
        self.fill_model(car.model)
        self.fill_year(car.year)
        self.select_fuel(car.fuel)
        self.fill_seats(car.seats)
        self.select_gear(car.gear)
        self.select_wheels_drive(car.wheels_drive)
        self.fill_seats(car.seats)
        self.fill_car_class(car.car_class)
        self.fill_serial_number(car.serial_number)
        self.fill_price(car.price_per_day)
        if car.photo_path:
            self.upload_photo(car.photo_path)


    def error_message(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text

    def upload_photo(self, photo_path):
        absolute_path = os.path.abspath(photo_path)
        self.find(self.PHOTO_FILE_INPUT).send_keys(absolute_path)



