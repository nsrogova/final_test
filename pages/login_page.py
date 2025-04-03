from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_text = self.browser.current_url
        assert "login" in url_text, "В ссылке нет слова 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LoginForm), "Форма логина отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LoginRegistrationForm), "Форма регистрации отсутствует"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LoginRegistrationEmail).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LoginRegistrationPasswordFirst).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LoginRegistrationPasswordSecond).send_keys(password)
        assert self.is_element_present(*LoginPageLocators.LoginRegistrationSubmit), "Кнопка отсутствует на странице"
        self.browser.find_element(*LoginPageLocators.LoginRegistrationSubmit).click()
