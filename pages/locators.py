from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LoginForm = (By.ID, "login_form")
    LoginUserName = (By.ID, "id_login-username")
    LoginPassword = (By.ID, "id_login-password")
    LoginSubmit = (By.CLASS_NAME, "login_submit")
    LoginRegistrationForm = (By.ID, "register_form")
    LoginRegistrationEmail = (By.ID, "id_registration-email")
    LoginRegistrationPasswordFirst = (By.ID, "id_registration-password1")
    LoginRegistrationPasswordSecond = (By.ID, "id_registration-password2")
    LoginRegistrationSubmit = (By.XPATH, "//button[@name='registration_submit']")

class BasketAdd:
    messageNameAdd = (By.ID, "messages")
    productName = (By.CSS_SELECTOR, ".product_main > h1")
    productBlockMain = (By.CLASS_NAME, "basket-items")
    productCost = (By.CSS_SELECTOR, ".product_main > p")
    buttonAdd = (By.CLASS_NAME, "btn-add-to-basket")
    nameProductAdd = (By.CSS_SELECTOR, ".alertinner > strong")
    costProductAdd = (By.CSS_SELECTOR, ".alertinner >p >strong")
    messageBasketEmpty = (By.CSS_SELECTOR, "#content_inner >p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
