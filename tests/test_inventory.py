import pytest
from pages.inventory_page import InventoryPage
from utils.config_loader import load_config
from utils.data_loader import load_test_data
from utils.helpers import wait_for_element, take_screenshot

# Load configuration settings and test data
config = load_config()
test_data = load_test_data()

@pytest.mark.usefixtures("driver")
def test_inventory_page_load(driver):
    """Test loading the inventory page after logging in."""
    inventory_page = InventoryPage(driver)
    inventory_page.load_inventory_page(
        config["base_url"],
        test_data["login"]["standard_user"]["username"],
        test_data["login"]["standard_user"]["password"]
    )
    # Verify successful load of inventory page
    assert "inventory.html" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_product_count(driver):
    """Test that the correct number of products are displayed."""
    inventory_page = InventoryPage(driver)
    inventory_page.load_inventory_page(
        config["base_url"],
        test_data["login"]["standard_user"]["username"],
        test_data["login"]["standard_user"]["password"]
    )
    items = inventory_page.get_inventory_items()
    # SauceDemo should display exactly 6 products
    assert len(items) == 6, f"Expected 6 products, but found {len(items)}"

@pytest.mark.usefixtures("driver")
def test_product_names(driver):
    """Test that product names match expected values."""
    inventory_page = InventoryPage(driver)
    inventory_page.load_inventory_page(
        config["base_url"],
        test_data["login"]["standard_user"]["username"],
        test_data["login"]["standard_user"]["password"]
    )
    # Add a method to get product names to your InventoryPage class
    product_names = inventory_page.get_product_names()
    expected_names = [product["name"] for product in test_data["products"]]
    assert set(product_names) == set(expected_names), "Product names don't match expected values"

@pytest.mark.usefixtures("driver")
def test_add_to_cart(driver):
    """Test adding a product to the cart."""
    inventory_page = InventoryPage(driver)
    inventory_page.load_inventory_page(
        config["base_url"],
        test_data["login"]["standard_user"]["username"],
        test_data["login"]["standard_user"]["password"]
    )
    # Add method to InventoryPage to add first product to cart
    inventory_page.add_product_to_cart(0)  # Add first product
    # Verify cart badge shows "1"
    cart_count = inventory_page.get_cart_count()
    assert cart_count == "1", f"Expected cart count to be 1, but got {cart_count}"

# TODO - Implement more tests for the InventoryPage
