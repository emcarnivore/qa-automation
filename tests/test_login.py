import pytest
from utils.config_loader import load_config
from utils.data_loader import load_test_data

config = load_config()
test_data = load_test_data()

@pytest.mark.usefixtures("driver")
def test_valid_login(driver):
    driver.get(config["base_url"])
    driver.find_element_by_id("user-name").send_keys(test_data["login"]["standard_user"]["username"])
    driver.find_element_by_id("password").send_keys(test_data["login"]["standard_user"]["password"])
    driver.find_element_by_id("login-button").click()
    assert "inventory.html" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_invalid_login(driver):
    driver.get(config["base_url"])
    driver.find_element_by_id("user-name").send_keys(test_data["login"]["no_user"]["username"])
    driver.find_element_by_id("password").send_keys(test_data["login"]["no_user"]["password"])
    driver.find_element_by_id("login-button").click()
    assert "Epic sadface" in driver.page_source
