from pages.base_page import BasePage
from .locators import BasketAdd


class BasketPage(BasePage):

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketAdd.messageBasketEmpty), "Сообщение о пустой корзине отсутствует"

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketAdd.productBlockMain), "Блок продукта присутствует на странице"