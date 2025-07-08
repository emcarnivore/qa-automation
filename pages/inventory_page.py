from selenium.webdriver.common.keys import Keys
from locators.login_locators import LoginLocators
from pages.login_page import LoginPage
import logging

class InventoryPage:
    def __init__(self, driver):
        """
        Initialize the InventoryPage with a WebDriver instance.

        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def load_page(self, base_url, username, password):
        """
        Log in and load the inventory page.

        :param base_url: The base URL of the application.
        :param username: The username to log in with.
        :param password: The password to log in with.
        """
        self.logger.info(f"Logging in and loading inventory page: {base_url}")
        login_page = LoginPage(self.driver)  # Use LoginPage to log in
        login_page.load_page(base_url)  # Load the login page
        login_page.login(username, password)  # Perform login
        assert "inventory.html" in self.driver.current_url, "Failed to load inventory page"
        self.logger.info("Inventory page loaded successfully")

    # TODO - Implement methods for interacting with the inventory page