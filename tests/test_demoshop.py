from allure_commons._allure import step
from api import api_helpers
from ui import cart_methods

def test_add_product_to_cart():
    '''Successful adding product to cart (API)'''
    with step('Add product'):
        result = api_helpers.add_product(product_id = 13, quantity = 1)

    with step('Get cookie from API'):
        cookie = api_helpers.get_cookie_from_api(result)

    with step('Set cookie from API and open Cart'):
        cart_methods.set_cookie_from_api_and_open_cart(cookie)

    with step('Check successful adding to Cart'):
        cart_methods.cart_should_have_product(product_name = 'Computing and Internet')

def test_add_products_to_cart():
    '''Successful adding products to cart (API)'''
    with step('Add products'):
        result = api_helpers.add_product(product_id = 13, quantity = 5)

    with step('Get cookie from API'):
        cookie = api_helpers.get_cookie_from_api(result)

    with step('Set cookie from API and open Cart'):
        cart_methods.set_cookie_from_api_and_open_cart(cookie)

    with step('Check successful adding to Cart'):
        cart_methods.cart_should_have_product_with_quantity(product_name = 'Computing and Internet', quantity = 5)

def test_add_product_to_cart_with_quantity_zero():
    '''Adding product to cart with quantity 0 (API)'''
    with step('Add product'):
        result = api_helpers.add_product(product_id = 13, quantity = 0)

    with step('Get cookie from API'):
        cookie = api_helpers.get_cookie_from_api(result)

    with step('Set cookie from API and open Cart'):
        cart_methods.set_cookie_from_api_and_open_cart(cookie)

    with step('Check Cart is empty'):
        cart_methods.cart_should_be_empty()

def test_add_different_products_to_cart():
    '''Successful adding different products to cart (API)'''
    with step('Add first product'):
        result_1 = api_helpers.add_product(product_id=13, quantity=1)

    with step('Get cookie from API'):
        cookie = api_helpers.get_cookie_from_api(result_1)

    with step('Add second product'):
        api_helpers.add_product_with_cookie(product_id=31, quantity=1, cookie=cookie)

    with step('Set cookie from API and open Cart'):
        cart_methods.set_cookie_from_api_and_open_cart(cookie)

    with step('Check successful adding to Cart'):
        cart_methods.cart_should_have_products(product_name_1 = 'Computing and Internet',
                                        product_name_2 = '14.1-inch Laptop')
