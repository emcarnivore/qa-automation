from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from locators.inventory_locators import InventoryLocators
import logging

class InventoryPage:
    def __init__(self, driver):
        """
        Initialize the InventoryPage with a WebDriver instance.

        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def load_inventory_page(self, base_url, username, password):
        """
        Log in and load the inventory page.

        :param base_url: The base URL of the application.
        :param username: The username to log in with.
        :param password: The password to log in with.
        """
        self.logger.info(f"Logging in and loading inventory page: {base_url}")
        login_page = LoginPage(self.driver)  # Use LoginPage to log in
        login_page.load_login_page(base_url)  # Load the login page
        login_page.login(username, password)  # Perform login
        assert "inventory.html" in self.driver.current_url, "Failed to load inventory page"
        self.logger.info("Inventory page loaded successfully")

    def get_inventory_items(self):
        """
        Retrieve a list of inventory items displayed on the page.

        :return: A list of inventory item elements.
        """
        self.logger.info("Retrieving inventory items")
        items = self.driver.find_elements(*InventoryLocators.INVENTORY_ITEMS)
        self.logger.info(f"Found {len(items)} inventory items")
        return items
    
# TODO - Implement more methods for interacting with the inventory page
