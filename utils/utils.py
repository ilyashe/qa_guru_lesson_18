import json
import logging
import allure
from allure_commons.types import AttachmentType
from allure_commons._allure import step


def log_api_call(func):
    def wrapper(*args, **kwargs):
        with step('API Request'):
            result = func(*args, **kwargs)

            # Request info
            allure.attach(
                body=f'Method: {result.request.method}\nURL: {result.request.url}',
                name='Request Info',
                attachment_type=AttachmentType.TEXT
            )

            allure.attach(
                body=result.request.body,
                name='Request Body',
                attachment_type=AttachmentType.TEXT
            )

            # Response
            allure.attach(
                body=f'Status code: {result.status_code}',
                name='Response status code',
                attachment_type=AttachmentType.TEXT
            )

            try:
                response_body = json.dumps(result.json(), indent=4, ensure_ascii=True)
                allure.attach(
                    body=response_body,
                    name='Response',
                    attachment_type=AttachmentType.JSON
                )
            except Exception:
                pass  # не JSON

            cookies_dict = {cookie.name: cookie.value for cookie in result.cookies}
            allure.attach(
                body=json.dumps(cookies_dict, indent=4),
                name='Cookies',
                attachment_type=AttachmentType.JSON
            )

            # Console log
            log_message = f'''
                ==== HTTP Request ====
                Method: {result.request.method}
                URL: {result.request.url}
                Body:
                {result.request.body}

                ==== HTTP Response ====
                Status Code: {result.status_code}
                Body:
                {json.dumps(json.loads(result.text), indent=4, ensure_ascii=False) if result.text else "None"}

                ==== Cookies ====
                {'\n'.join([f'{c.name} = {c.value}' for c in result.cookies])}
            '''
            logging.info(log_message)

            return result
    return wrapper