import pytest
from locators.login_locators import LoginLocators 
from pages.login_page import LoginPage
from utils.config_loader import load_config
from utils.data_loader import load_test_data
from utils.helpers import wait_for_element, take_screenshot

# Load configuration settings and test data
config = load_config()
test_data = load_test_data()

@pytest.mark.usefixtures("driver")
def test_valid_login(driver):
    """Test login with valid standard user credentials."""
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        test_data["login"]["standard_user"]["username"], 
        test_data["login"]["standard_user"]["password"]
    )
    # Verify that the user is redirected to the inventory page
    assert "inventory.html" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_invalid_login_username(driver):
    """Test login with invalid username."""
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        test_data["login"]["invalid_user"]["username"], 
        test_data["login"]["invalid_user"]["password"]
    )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/invalid_username.png")

@pytest.mark.usefixtures("driver")
def test_invalid_login_password(driver):
    """Test login with invalid password."""
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        test_data["login"]["invalid_password"]["username"], 
        test_data["login"]["invalid_password"]["password"]
    )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/invalid_password.png")

@pytest.mark.usefixtures("driver")
def test_login_locked_out_user(driver):
    """Test login with locked out user credentials."""
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        test_data["login"]["locked_out_user"]["username"], 
        test_data["login"]["locked_out_user"]["password"]
        )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Sorry, this user has been locked out." in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/locked_out_user.png")

@pytest.mark.usefixtures("driver")
def test_login_empty_username(driver):
    """Test login with empty username field."""
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        "", 
        test_data["login"]["standard_user"]["password"]
        )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Username is required" in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/empty_username.png")

@pytest.mark.usefixtures("driver")
def test_login_empty_password(driver):
    """Test login with empty password field."""
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        test_data["login"]["standard_user"]["username"], 
        ""
        )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Password is required" in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/empty_password.png")

@pytest.mark.usefixtures("driver")
def test_login_empty_fields(driver):
    """Test login with empty password field."""
    login_page = LoginPage(driver)
    login_page.load_page(config["base_url"])
    login_page.login(
        "", 
        ""
        )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Username is required" in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/empty_fields.png")

# TODO: Test Login button with click and Enter key press
