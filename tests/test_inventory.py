import pytest
from locators.login_locators import LoginLocators 
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_loader import load_config
from utils.data_loader import load_test_data
from utils.helpers import wait_for_element, take_screenshot

# Load configuration settings and test data
config = load_config()
test_data = load_test_data()

# TODO - Implement tests for the InventoryPage

@pytest.mark.usefixtures("driver")
def test_inventory_page_load(driver):
    """Test loading the inventory page after logging in."""
    inventory_page = InventoryPage(driver)
    inventory_page.load_page(
        config["base_url"],
        test_data["login"]["standard_user"]["username"],
        test_data["login"]["standard_user"]["password"]
    )
    # Verify successful load of inventory page
    assert "inventory.html" in driver.current_url
