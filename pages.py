

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

from selenium.webdriver import Keys


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')


    supportive_plan_card = (By.XPATH, '//div[text()="Supportive"]/..')
    get_supportive_plan_button = (By.XPATH, '//div[contains(text(), "Supportive")]')
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    custom_option_locator = (By.XPATH, '//div[@text()="custom"')
    phone_number_button_locator = (By.XPATH, '//div[@class="np-button"]//div[contains(text(), "Phone number")]')
    phone_number_input_locator = (By.ID, 'phone')
    phone_number_next_button = (By.CSS_SELECTOR, '.full')
    get_enter_code_sms_text_locator = (By.ID, 'code')
    confirm_button_locator = (By.XPATH, '//button[contains(text(),"Confirm")]')
    add_card_locator= (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_number_input = (By.ID, 'number')
    card_code_locator = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    comment_locator = (By.ID, 'comment')
    blanket_and_handkerchiefs_locator = (By.XPATH, '(//span[@class="slider round"])[1]')
    blanket_and_handkerchiefs_verification = (By.CLASS_NAME, 'switch-input')
    add_ice_cream_button = (By.CLASS_NAME, 'counter-plus')
    number_of_ice_creams = (By.XPATH, '//div[@class="counter-value"]')
    phone_code = (By.CLASS_NAME,'np-text')
    payment_method_button = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Payment method")]')
    link_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    selected_payment_method = (By.XPATH, '//div[@class="pp-value-text"]')
    close_card_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    click_message_the_driver = (By.XPATH, '//*[@id="comment"]')






    def __init__(self, driver):
        self.driver = driver


    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)


    def selective_supportive_plan(self):
        self.driver.find_element(*self.get_supportive_plan_button).click()

    def get_supportive_class (self):
        return self.driver.find_element(*self.supportive_plan_card).get_attribute("class")

    def add_ice_cream(self, amount: int):
        optional_add_controls = self.driver.find_elements(*self.add_ice_cream_button)
        for count in range(amount):
            optional_add_controls[0].click()

    def get_ice_cream_added_number(self):
        return int(self.driver.find_elements(*self.number_of_ice_creams)[0].text)

    def fill_phone_number(self, pnumber):
        self.driver.find_element(*self.phone_number_button_locator).click()
        self.driver.find_element(*self.phone_number_input_locator).send_keys(pnumber)
        self.driver.find_element(*self.phone_number_next_button).click()
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.get_enter_code_sms_text_locator).send_keys(code)
        self.driver.find_element(*self.confirm_button_locator).click()

    def get_phone(self):
        return self.driver.find_element(*self.phone_code).text

    def select_plan(self, from_address, to_address, card_number, code):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()
        self.selective_supportive_plan()

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method_button).click()

    def add_card_button(self):
        self.driver.find_element(*self.add_card_locator).click()


    def add_card_number(self, card_number_text):
        self.driver.find_element(*self.card_number_input).send_keys(card_number_text)


    def add_code_number(self, code_number_text):
        self.driver.find_element(*self.card_code_locator).send_keys(code_number_text)
        self.driver.find_element(*self.card_code_locator).send_keys(Keys.TAB)


    def click_link_card_button(self):
        self.driver.find_element(*self.link_card_button).click()

    def click_close_payment_button(self):
        self.driver.find_element(*self.close_card_button).click()

    def get_current_payment_method(self):
        return self.driver.find_element(*self.selected_payment_method).text


    def click_message_to_the_driver(self, message_to_the_driver):
        self.driver.find_element(*self.click_message_the_driver).send_keys(message_to_the_driver)

    def get_message_to_driver(self):
        return self.driver.find_element(*self.click_message_the_driver).get_property('value')


    def click_blanket_and_handkerchiefs_locator(self):
        self.driver.find_element(*self.blanket_and_handkerchiefs_locator).click()



    def get_blanket_and_handkerchiefs_verification(self):
        return self.driver.find_element(*self.blanket_and_handkerchiefs_verification).get_property('checked')





