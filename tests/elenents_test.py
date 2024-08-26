import time

from pages.base_page import BasePage


def test_example(driver):
    page = BasePage(driver, 'https://www.google.com')
    page.open()
    time.sleep(2)
