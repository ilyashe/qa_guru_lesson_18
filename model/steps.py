from selene import browser
from selene.support.conditions import have
from utils.utils import demoshop_api_post

WEB_URL = 'https://demowebshop.tricentis.com/'
API_URL = 'https://demowebshop.tricentis.com/'

def add_product(product_id, quantity):
    result = demoshop_api_post(
        url=API_URL + f'addproducttocart/details/{product_id}/1',
        data={f'addtocart_{product_id}.EnteredQuantity': {quantity}}
    )
    return result

def add_product_with_cookie(product_id, quantity, cookie):
    headers = {
        'Cookie': f'Nop.customer={cookie}'
    }
    result = demoshop_api_post(
        url=API_URL + f'addproducttocart/details/{product_id}/1',
        data={f'addtocart_{product_id}.EnteredQuantity': {quantity}},
        headers=headers
    )
    return result

def get_cookie_from_api(result):
    cookie = result.cookies.get('Nop.customer')
    return cookie

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
