import pytest
from locators.login_locators import LoginLocators 
from pages.login_page import LoginPage
from utils.config_loader import load_config
from utils.data_loader import load_test_data
from utils.helpers import wait_for_element, take_screenshot

config = load_config()
test_data = load_test_data()

@pytest.mark.usefixtures("driver")
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        test_data["login"]["standard_user"]["username"], 
        test_data["login"]["standard_user"]["password"]
    )
    assert "inventory.html" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        test_data["login"]["no_user"]["username"], 
        test_data["login"]["no_user"]["password"]
    )
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface" in error_message
    take_screenshot(driver, "screenshots/invalid_login.png")
