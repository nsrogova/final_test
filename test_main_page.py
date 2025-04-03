import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():


    def test_guest_can_go_to_login_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open_link()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open_link()
        page.should_be_login_link()


def test_should_see_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open_link()
    page.go_to_login_page()
    login_pages = LoginPage(browser, browser.current_url)
    login_pages.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open_link()
    page.go_to_basket_page()
    pageBasket = BasketPage(browser, link)
    pageBasket.should_not_be_product()
    pageBasket.should_be_message_basket_empty()
