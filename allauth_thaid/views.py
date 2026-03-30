import requests
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import ThaiDProvider


class ThaiDOAuth2Adapter(OAuth2Adapter):
    provider_id = ThaiDProvider.id
    access_token_url = "https://imauth.bora.dopa.go.th/api/v2/oauth2/token/"
    authorize_url = "https://imauth.bora.dopa.go.th/api/v2/oauth2/auth/"
    profile_url = "https://imauth.bora.dopa.go.th/api/v2/oauth2/userinfo/"

    def complete_login(self, request, app, token, **kwargs):
        headers = {"Authorization": f"Bearer {token.token}"}
        response = requests.get(self.profile_url, headers=headers)
        response.raise_for_status()
        extra_data = response.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(ThaiDOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(ThaiDOAuth2Adapter)
