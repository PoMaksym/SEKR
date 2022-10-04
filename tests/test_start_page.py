from selenium import webdriver
from selenium.webdriver.common.by import By

from constants.base import DRIVER_PATH, BASE_URL


class TestStartPage:

    def test_start_page(self):
        # Pre-conditions

        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)

        element = driver.find_element(by=By.XPATH,
                                      value='.//a[@class="AppButton_linkBtn__rmRkI HeaderNav_linkBtn__rZZ6c"][@href="/contact-us"]')
        print(element)
