import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_loader import load_config

config = load_config()

def wait_for_element(driver, locator, timeout=config["timeout"]):
    """
    Wait for an element to be present on the page.

    :param driver: The WebDriver instance.
    :param locator: The locator tuple (By, value) of the element to wait for.
    :param timeout: The maximum time to wait for the element (default is the value from config).
    :return: The WebElement if found, else raises TimeoutException.
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def take_screenshot(driver, file_path):
    """
    Take a screenshot of the current browser window.

    :param driver: The WebDriver instance.
    :param file_path: The file path to save the screenshot.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    driver.save_screenshot(file_path)
