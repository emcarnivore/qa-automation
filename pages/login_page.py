from selenium.webdriver.common.keys import Keys
from locators.login_locators import LoginLocators
import logging

class LoginPage:
    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance.

        :param driver: The WebDriver instance to interact with the browser.
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
        assert "login.html" in self.driver.current_url, "Failed to load login page"
        self.logger.info("Login page loaded successfully")

    def login(self, username, password, use_button=False):
        """
        Perform login action.

        :param username: The username to login with.
        :param password: The password to login with.
        :param use_button: If True, click the login button instead of pressing Enter.
        """
        self.logger.info(f"Attempting to login with username: {username}")
        self.driver.find_element(*LoginLocators.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
    
        if use_button:
            self.logger.info("Clicking the login button")
            self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        else:
            self.logger.info("Pressing Enter to submit the login form")
            self.driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Keys.RETURN)
            

    def get_error_message(self):
        """
        Get the error message displayed on the login page.

        :return: The error message text.
        """
        self.logger.info("Retrieving error message")
        error_message = self.driver.find_element(*LoginLocators.ERROR_MESSAGE).text
    