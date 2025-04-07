from allure_commons._allure import step
from selene import browser
from selene.support.conditions import have
from utils.utils import demoshop_api_post


WEB_URL = 'https://demowebshop.tricentis.com/'
API_URL = 'https://demowebshop.tricentis.com/'


def test_add_product_to_cart():
    '''Successful adding product to cart (API)'''
    with step('Add product'):
        product_id = 13
        quantity = 1
        product_name = 'Computing and Internet'

        result = demoshop_api_post(
            url=API_URL + f'addproducttocart/details/{product_id}/1',
            data={f'addtocart_{product_id}.EnteredQuantity': {quantity}}
        )

    with step('Get cookie from API'):
        cookie = result.cookies.get('Nop.customer')

    with step('Set cookie from API and open Cart'):
        browser.open(WEB_URL + 'cart')
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
        browser.open(WEB_URL + 'cart')

    with step('Check successful adding to Cart'):
        browser.element('.cart-item-row').should(have.text(product_name))
        browser.quit()

def test_add_products_to_cart():
    '''Successful adding products to cart (API)'''
    with step('Add products'):
        product_id = 13
        quantity = 5
        product_name = 'Computing and Internet'

        result = demoshop_api_post(
            url=API_URL + f'addproducttocart/details/{product_id}/1',
            data={f'addtocart_{product_id}.EnteredQuantity': {quantity}}
        )

    with step('Get cookie from API'):
        cookie = result.cookies.get('Nop.customer')

    with step('Set cookie from API and open Cart'):
        browser.open(WEB_URL + 'cart')
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
        browser.open(WEB_URL + 'cart')

    with step('Check successful adding to Cart'):
        browser.element('.cart-item-row').should(have.text(product_name))
        browser.element('.qty-input').should(have.value(str(quantity)))
        browser.quit()

def test_add_product_to_cart_with_quantity_zero():
    '''Adding product to cart with quantity 0 (API)'''
    with step('Add product'):
        product_id = 13
        quantity = 0

        result = demoshop_api_post(
            url=API_URL + f'addproducttocart/details/{product_id}/1',
            data={f'addtocart_{product_id}.EnteredQuantity': {quantity}}
        )

    with step('Get cookie from API'):
        cookie = result.cookies.get('Nop.customer')

    with step('Set cookie from API and open Cart'):
        browser.open(WEB_URL + 'cart')
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
        browser.open(WEB_URL + 'cart')

    with step('Check Cart is empty'):
        browser.element('.page-body').should(have.text('Your Shopping Cart is empty!'))
        browser.quit()

def test_add_different_products_to_cart():
    '''Successful adding different products to cart (API)'''
    with step('Add first product'):
        product_id_1 = 13
        quantity_1 = 1
        product_name_1 = 'Computing and Internet'

        result_1 = demoshop_api_post(
            url=API_URL + f'addproducttocart/details/{product_id_1}/1',
            data={f'addtocart_{product_id_1}.EnteredQuantity': {quantity_1}}
        )

    with step('Get cookie from API'):
        cookie = result_1.cookies.get('Nop.customer')

    with step('Add second product'):
        product_id_2 = 31
        quantity_2 = 1
        product_name_2 = '14.1-inch Laptop'
        headers = {
            'Cookie': f'Nop.customer={cookie}'
        }
        result_2 = demoshop_api_post(
            url=API_URL + f'addproducttocart/details/{product_id_2}/1',
            data={f'addtocart_{product_id_2}.EnteredQuantity': {quantity_2}},
            headers=headers
        )

    with step('Set cookie from API and open Cart'):
        browser.open(WEB_URL + 'cart')
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
        browser.open(WEB_URL + 'cart')

    with step('Check successful adding to Cart'):
        browser.all('.cart-item-row').first.should(have.text(product_name_1))
        browser.all('.cart-item-row').second.should(have.text(product_name_2))
        browser.quit()
