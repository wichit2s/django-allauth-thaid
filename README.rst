====================
django-allauth-thaid
====================

ThaiD (Thai Digital Identity) OAuth2 provider for `django-allauth`.

Prerequisites
-------------

* `django>=4.2`
* `django-allauth>=0.56.0`

Installation
------------

Install using `pip`::

    pip install django-allauth-thaid

Configuration
-------------

Add ``allauth_thaid`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'allauth',
        'allauth.socialaccount',
        'allauth_thaid',
        ...
    ]

Add the provider to ``SOCIALACCOUNT_PROVIDERS`` in ``settings.py``::

    SOCIALACCOUNT_PROVIDERS = {
        'thaid': {
            'SCOPE': [
                'openid',
                'pid',
                'name',
                'given_name',
                'family_name',
            ],
        }
    }

Register a ``SocialApp`` with the following details from ThaiD:

* **Provider:** ThaiD
* **Name:** ThaiD
* **Client ID:** Your Client ID
* **Secret Key:** Your Client Secret
