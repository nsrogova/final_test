import time
from re import fullmatch

import pytest
from selenium import webdriver

from conftest import browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

def auth():
    driver = webdriver.Chrome()
    url = "https://auth.okd.t-global.bcs/auth/realms/perseus/login-actions/authenticate?execution=8920f10c-b9b7-42b1-9004-70747a3e6ea5&client_id=ef-front&tab_id=7SSPCmz_-LE"



