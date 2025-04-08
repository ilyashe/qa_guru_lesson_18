import json
import logging
from requests import Session
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import allure

class TestSession(Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def demoshop_api_request(self, path, method='POST', *args, **kwargs):
        full_url = self.base_url + path
        with step('API Request'):
            result = self.request(url=full_url, method=method, *args, **kwargs)
            self.log_to_allure(result)
            self.log_to_console(result)
            return result

    def log_to_allure(self, result):
        allure.attach(
            body=f'Method: {result.request.method}\nURL: {result.request.url}',
            name='Request Info',
            attachment_type=AttachmentType.TEXT,
            extension='txt'
        )

        allure.attach(
            body=result.request.body or '',
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

        try:
            allure.attach(
                body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                name='Response',
                attachment_type=AttachmentType.JSON,
                extension='json'
            )
        except Exception:
            allure.attach(
                body=result.text,
                name='Response (non-JSON)',
                attachment_type=AttachmentType.TEXT,
                extension='txt'
            )

        cookies_dict = {cookie.name: cookie.value for cookie in result.cookies}
        allure.attach(
            body=json.dumps(cookies_dict, indent=4),
            name='Cookies',
            attachment_type=AttachmentType.TEXT,
            extension='json'
        )

    def log_to_console(self, result):
        try:
            body = json.dumps(json.loads(result.text), indent=4, ensure_ascii=False)
        except Exception:
            body = result.text or "None"

        log_message = f'''
==== HTTP Request ====
Method: {result.request.method}
URL: {result.request.url}
Body:
{result.request.body}

==== HTTP Response ====
Status Code: {result.status_code}
Body:
{body}

==== Cookies ====
{chr(10).join([f'{c.name} = {c.value}' for c in result.cookies])}
'''
        logging.info(log_message)
