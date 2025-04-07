from selene import browser
from selene.support.conditions import have

WEB_URL = 'https://demowebshop.tricentis.com/'

def set_cookie_from_api_and_open_cart(cookie):
    browser.open(WEB_URL + 'cart')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
    browser.open(WEB_URL + 'cart')

def cart_should_have_product(product_name):
    browser.element('.cart-item-row').should(have.text(product_name))

def cart_should_have_product_with_quantity(product_name, quantity):
    browser.element('.cart-item-row').should(have.text(product_name))
    browser.element('.qty-input').should(have.value(str(quantity)))

def cart_should_be_empty():
    browser.element('.page-body').should(have.text('Your Shopping Cart is empty!'))

def cart_should_have_products(product_name_1, product_name_2):
    browser.all('.cart-item-row').first.should(have.text(product_name_1))
    browser.all('.cart-item-row').second.should(have.text(product_name_2))
