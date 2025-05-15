from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage
import time

class TestUrbanRoutes:


    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selective_supportive_plan()
        assert routes_page.get_supportive_class() == 'tcard active'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        phone_number = data.PHONE_NUMBER
        routes_page.fill_phone_number(phone_number)
        assert routes_page.get_phone() == phone_number

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(1)
        routes_page.click_payment_method()
        routes_page.add_card_button()
        routes_page.add_card_number(data.CARD_NUMBER)
        routes_page.add_code_number(data.CARD_CODE)
        routes_page.click_link_card_button()
        routes_page.click_close_payment_button()
        assert routes_page.get_current_payment_method() == 'Card'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        message_to_the_driver = data.MESSAGE_FOR_DRIVER
        routes_page.click_message_to_the_driver(message_to_the_driver)
        assert routes_page.get_message_to_driver() == message_to_the_driver

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selective_supportive_plan()
        time.sleep(2)
        routes_page.click_blanket_and_handkerchiefs_locator()
        assert routes_page.get_blanket_and_handkerchiefs_verification() == True


    def test_order_2_ice_creams(self):
        self.driver.maximize_window()
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selective_supportive_plan()
        time.sleep(2)
        number_of_ice_creams = 2
        routes_page.add_ice_cream(number_of_ice_creams)
        assert routes_page.get_ice_cream_added_number() == 2


    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        routes_page.click_call_taxi_button()
        routes_page.selective_supportive_plan()
        message_to_the_driver = data.MESSAGE_FOR_DRIVER
        routes_page.click_message_to_the_driver(message_to_the_driver)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
