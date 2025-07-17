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
def test_login_with_keys(driver):
    """Test login by pressing Enter."""
    login_page = LoginPage(driver)
    login_page.load_login_page(config["base_url"])
    login_page.login(
        test_data["login"]["standard_user"]["username"], 
        test_data["login"]["standard_user"]["password"],
        use_button=False  # Use Enter key to submit
    )
    # Verify successful login
    assert "inventory.html" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_login_with_button_click(driver):
    """Test login by clicking the login button."""
    login_page = LoginPage(driver)
    login_page.load_login_page(config["base_url"])
    login_page.login(
        test_data["login"]["standard_user"]["username"], 
        test_data["login"]["standard_user"]["password"],
        use_button=True  # Use the button click to submit
    )
    # Verify successful login
    assert "inventory.html" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_login_with_nonexistent_user(driver):
    """Test login with non-existent user credentials."""
    login_page = LoginPage(driver)
    login_page.load_login_page(config["base_url"])
    login_page.login(
        test_data["login"]["nonexistent_user"]["username"], 
        test_data["login"]["nonexistent_user"]["password"]
    )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/epic_sadface.png")

@pytest.mark.usefixtures("driver")
def test_login_with_locked_out_user(driver):
    """Test login with locked out user credentials."""
    login_page = LoginPage(driver)
    login_page.load_login_page(config["base_url"])
    login_page.login(
        test_data["login"]["locked_out_user"]["username"], 
        test_data["login"]["locked_out_user"]["password"]
    )
    # Verify that the appropriate error message is displayed
    error_message = wait_for_element(driver, LoginLocators.ERROR_MESSAGE).text
    assert "Epic sadface: Sorry, this user has been locked out." in error_message
    # Take a screenshot of the error message
    take_screenshot(driver, "screenshots/epic_sadface.png")

