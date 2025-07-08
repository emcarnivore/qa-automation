from selenium.webdriver.common.by import By

class LoginLocators:
    """
    This class contains locators for the login page elements.
    """
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")
