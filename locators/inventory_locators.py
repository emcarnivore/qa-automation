from selenium.webdriver.common.by import By

class InventoryLocators:
    """
    This class contains locators for the inventory page elements.
    """
    HAMBURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    CROSS_BUTTON = (By.ID, "react-burger-cross-btn")
    ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE_LINK = (By.ID, "reset_sidebar_link")

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    NAME_AZ_OPTION = (By.XPATH, "//option[@value='az']")
    NAME_ZA_OPTION = (By.XPATH, "//option[@value='za']")
    PRICE_LOW_HIGH_OPTION = (By.XPATH, "//option[@value='lohi']")
    PRICE_HIGH_LOW_OPTION = (By.XPATH, "//option[@value='hilo']")

    # TODO - Add locators for inventory items
