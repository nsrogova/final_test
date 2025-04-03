from pages.base_page import BasePage
from .locators import BasketAdd


class ProductPage(BasePage):

    def add_in_basket(self):
        button = self.browser.find_element(*BasketAdd.buttonAdd)
        button.click()

    def matching_name(self):
        nameProduct = self.browser.find_element(*BasketAdd.productName).text
        messegeAdd = self.browser.find_element(*BasketAdd.nameProductAdd).text
        assert messegeAdd == nameProduct, "Названия не совпадают"

    def matching_cost(self):
        costProduct = self.browser.find_element(*BasketAdd.productCost).text
        messege = self.browser.find_element(*BasketAdd.costProductAdd).text
        assert messege == costProduct, "Цены не совпадают"

    def should_be_newYear_url(self):
        assert '?promo=newYear' in self.browser.current_url, 'newYear не содержится в url'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketAdd.messageNameAdd), "Элемент присутствует на странице"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*BasketAdd.messageNameAdd), "Элемент присутствует на странице"

    def should_be_success_message(self):
        assert self.is_element_present(*BasketAdd.messageNameAdd), "Элемент отсутствует на странице"