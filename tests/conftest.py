import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.config_loader import load_config
import logging

config = load_config()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    browser = config.get("browser", "chrome").lower()
    options = None
    service = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if config["headless"]:
            options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if config["headless"]:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    logger.info(f"Starting {browser} browser in {'headless' if config['headless'] else 'headed'} mode")
    driver.implicitly_wait(config["timeout"])
    yield driver
    logger.info(f"Quitting {browser} browser")
    driver.quit()
