from selenium.webdriver.common.keys import Keys
from locators.login_locators import LoginLocators
import logging

class LoginPage:
    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance.
        """
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def load_page(self, base_url):
        """
        Load the login page.
        
        :param base_url: The base URL of the application.
        """
        self.logger.info(f"Loading page: {base_url}")
        self.driver.get(base_url)

    def login(self, username, password):
        """
        Perform login action.
        
        :param username: The username to login with.
        :param password: The password to login with.
        """
        self.logger.info(f"Attempting to login with username: {username}")
        self.driver.find_element(*LoginLocators.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password + Keys.RETURN)

    def get_error_message(self):
        """
        Get the error message displayed on the login page.
        
        :return: The error message text.
        """
        self.logger.info("Retrieving error message")
        return self.driver.find_element(*LoginLocators.ERROR_MESSAGE).text
    