import json
import logging

import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import allure

def demoshop_api_post(url, data, **kwargs):
    with step('API Request'):
        result = requests.post(url=url, data=data, **kwargs)

        log_to_allure(result)
        log_to_console(result)
        return result

def log_to_allure(result):
    allure.attach(
        body=f'Method: {result.request.method}\nURL: {result.request.url}',
        name='Request Info',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )
    allure.attach(
        body=result.request.body,
        name='Request Body',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    allure.attach(
        body=f'Status code: {result.status_code}',
        name='Response status code',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    allure.attach(
        body=json.dumps(result.json(), indent=4, ensure_ascii=True),
        name='Response',
        attachment_type=AttachmentType.JSON,
        extension='json'
    )

    cookies_dict = {cookie.name: cookie.value for cookie in result.cookies}
    allure.attach(
        body=json.dumps(cookies_dict, indent=4),
        name='Cookies',
        attachment_type=AttachmentType.TEXT,
        extension='json'
    )

def log_to_console(result):
    log_message = f'''
            ==== HTTP Request ====
            Method: {result.request.method}
            URL: {result.request.url}
            Body:
            {result.request.body}

            ==== HTTP Response ====
            Status Code: {result.status_code}
            Body:
            {result.text}

            ==== Cookies ====
            {'\n'.join([f'{c.name} = {c.value}' for c in result.cookies])}
            '''

    logging.info(log_message)