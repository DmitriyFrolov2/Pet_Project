import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('324')
        self.element_is_visible(self.locators.EMAIL).send_keys('233@imnox.ru')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('current_address')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('permanent_address')
        self.scroll_down(200)  # In this case i should use this way because go_to_element doesn't work
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)
