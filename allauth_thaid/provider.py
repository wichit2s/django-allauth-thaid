from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

class ThaiDAccount(ProviderAccount):
    def get_avatar_url(self):
        return None

    def to_str(self):
        d = self.account.extra_data
        name = d.get("name")
        if name:
            return name
        return super(ThaiDAccount, self).to_str()

class ThaiDProvider(OAuth2Provider):
    id = "thaid"
    name = "ThaiD"
    account_class = ThaiDAccount

    def extract_uid(self, data):
        return str(data.get("pid") or data.get("sub"))

    def extract_common_fields(self, data):
        return dict(
            first_name=data.get("given_name"),
            last_name=data.get("family_name"),
            name=data.get("name"),
        )

    def get_default_scope(self):
        return ["openid", "pid", "name"]

provider_classes = [ThaiDProvider]
