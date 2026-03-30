=====
Usage
=====

Configuration
-------------

Add `allauth_thaid` to your `INSTALLED_APPS` in `settings.py`:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'allauth',
        'allauth.socialaccount',
        'allauth_thaid',
        ...
    ]

Add the provider to `SOCIALACCOUNT_PROVIDERS` in `settings.py`:

.. code-block:: python

    SOCIALACCOUNT_PROVIDERS = {
        'thaid': {
            'SCOPE': [
                'openid',
                'pid',
                'name',
                'given_name',
                'family_name',
            ],
            'AUTH_PARAMS': {'access_type': 'online'},
        }
    }

Register a SocialApp
--------------------

Go to the Django admin and register a `SocialApp` with the following details from ThaiD:

* **Provider:** ThaiD
* **Name:** ThaiD
* **Client ID:** Your Client ID
* **Secret Key:** Your Client Secret
