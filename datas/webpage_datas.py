from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class PageLocators:
    LOCATOR_PRODUCT_CARD = (By.XPATH, "")  # fill your individual product card locator here
    LOCATOR_IMAGE = (By.XPATH, "")  # fill your individual image locator here
