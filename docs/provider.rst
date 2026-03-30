=================
ThaiD Implementation
=================

Authentication Endpoints
------------------------

- **Authorize URL:** `https://imauth.bora.dopa.go.th/api/v2/oauth2/auth/`
- **Token URL:** `https://imauth.bora.dopa.go.th/api/v2/oauth2/token/`
- **UserInfo URL:** `https://imauth.bora.dopa.go.th/api/v2/oauth2/userinfo/`

Technical Mappings
------------------

UID
---

By default, the UID is extracted from the `pid` field (Thai Personal Identity Number) or the `sub` field.

Common Fields
-------------

The following fields are mapped for `django-allauth`:

- `first_name`: `given_name`
- `last_name`: `family_name`
- `name`: `name`

Scopes
------

Default scopes are `openid`, `pid`, and `name`. Optional scopes include `given_name`, `family_name`, `birthdate`, `gender`, `address`.
