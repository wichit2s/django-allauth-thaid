from allauth.socialaccount.tests import create_oauth2_tests
from allauth.tests import MockedResponse
from .settings import *

from allauth_thaid.provider import ThaiDProvider

class ThaiDTests(create_oauth2_tests(ThaiDProvider)):
    def get_mocked_response(self):
        return MockedResponse(200, """
        {
            "pid": "1234567890123",
            "name": "Wichit Sombat",
            "given_name": "Wichit",
            "family_name": "Sombat",
            "birthdate": "1990-01-01"
        }
        """)
