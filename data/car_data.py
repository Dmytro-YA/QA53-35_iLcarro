
from faker import Faker

import resources
from models.car import Car

fake = Faker()

CITY_OPTIONS = [
    "Tel Aviv", "Jerusalem", "Haifa", "Petah Tikva",
    "Ashdod", "Netanya", "Beersheba", "Bnei Brak",
]
FUEL_OPTIONS = ["Petrol", "Diesel", "Electric", "Hybrid"]

MANUFACTURES_OPTIONS = ["BMW", "Mercedes", "Toyota", "Ford", "Honda", "Audi"]

MODELS_OPTIONS = ["X5", "3 Series", "M3", "M5", "M6", "M7", "Camry", "Civic", "Focus", "A4", "A6", "A8"]

CAR_CLASS_OPTIONS = [ "Economy", "Compact", "Midsize", "Luxury", "SUV", "Sports", "Comfort", "Premium"]
WHEELS_DRIVE_OPTIONS = ["FWD", "RWD", "AWD"]

def create_car(city = None, fuel = None, manufacturer = None, model = None, year = None,
               car_class = None, serial_number = None,wheels_drive = None, price = None, seats = None, gear = None, photo_path = None):
    return Car(
        city = city if city is not None else fake.random_element(CITY_OPTIONS),
        manufacture = manufacturer if manufacturer is not None else fake.random_element(MANUFACTURES_OPTIONS),
        model = model if model is not None else fake.random_element(MODELS_OPTIONS),
        year = year if year is not None else fake.random_int(min = 2000, max = 2023),
        fuel = fuel if fuel is not None else fake.random_element(FUEL_OPTIONS),
        gear = gear if gear is not None else fake.random_element(["Automatic", "Manual"]),
        seats = seats if seats is not None else fake.random_int(min = 2, max = 10),
        photo_path = photo_path  ,
        wheels_drive = wheels_drive if wheels_drive is not None else fake.random_element([WHEELS_DRIVE_OPTIONS[0], WHEELS_DRIVE_OPTIONS[1], WHEELS_DRIVE_OPTIONS[2]]),
        car_class = car_class if car_class is not None else fake.random_element(CAR_CLASS_OPTIONS),
        serial_number = serial_number if serial_number is not None else fake.random_number(digits=10),
        price_per_day = price if price is not None else fake.random_int(min = 20, max = 500)
    )