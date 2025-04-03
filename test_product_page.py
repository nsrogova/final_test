import time
from re import fullmatch

import pytest

from conftest import browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


def test_guest_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open_link()
    page.add_in_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.matching_name()
    page.matching_cost()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_link(browser, link):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    page = ProductPage(browser, link)
    page.open_link()
    page.add_in_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.matching_name()
    page.matching_cost()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open_link()
    page.add_in_basket()
    # page.should_be_success_message()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open_link()
    # page.should_be_success_message()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open_link()
    page.add_in_basket()
    # page.should_be_success_message()
    page.should_not_be_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open_link()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open_link()
    page.should_be_login_link()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open_link()
    page.go_to_basket_page()
    pageBasket = BasketPage(browser, link)
    pageBasket.should_not_be_product()
    pageBasket.should_be_message_basket_empty()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        email = str(time.time()) + "@mail.ru"
        page = ProductPage(browser, link)
        page.open_link()
        page.should_be_login_link()
        page.go_to_login_page()
        pageLogin = LoginPage(browser, link)
        pageLogin.register_new_user(email,"qwerty@mail.ru")
        pageLogin.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open_link()
        page.add_in_basket()
        # page.solve_quiz_and_get_code()
        time.sleep(5)
        page.matching_name()
        page.matching_cost()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open_link()
        page.add_in_basket()
        page.should_be_success_message()
        # page.should_not_be_success_message()