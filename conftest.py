import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")
    driver.maximize_window()
    yield driver
    driver.quit()
