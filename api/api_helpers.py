from utils.utils import demoshop_api_post

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
