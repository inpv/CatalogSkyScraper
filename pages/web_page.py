from pages.base_page import BasePage


class NavHelper(BasePage):

    def enter_text_into_input(self, locator, text):
        input_field = self.find_element(locator)
        input_field.click()
        input_field.send_keys(text)

    def click_on_button(self, locator):
        return self.find_element(locator, time=10).click()

    def click_on_buttons(self, locator):
        for btn in self.find_elements(locator, time=10):
            btn.click()
