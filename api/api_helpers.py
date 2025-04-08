def add_product(api_session, product_id, quantity):
    return api_session.demoshop_api_request(
        path=f'addproducttocart/details/{product_id}/1',
        data={f'addtocart_{product_id}.EnteredQuantity': quantity}
    )


def add_product_with_cookie(api_session, product_id, quantity, cookie):
    headers = {
        'Cookie': f'Nop.customer={cookie}'
    }
    return api_session.demoshop_api_request(
        path=f'addproducttocart/details/{product_id}/1',
        data={f'addtocart_{product_id}.EnteredQuantity': quantity},
        headers=headers
    )


def get_cookie_from_api(result):
    return result.cookies.get('Nop.customer')
