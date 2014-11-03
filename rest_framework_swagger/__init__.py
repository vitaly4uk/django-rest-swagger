VERSION = '0.2.0'

DEFAULT_SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '',
    'api_path': '/',
    'api_key': '',
    'enabled_methods': ['get', 'post', 'put', 'patch', 'delete'],
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
}

try:
    from django.conf import settings
    from django.utils import six
    SWAGGER_SETTINGS = getattr(settings, 'SWAGGER_SETTINGS', DEFAULT_SWAGGER_SETTINGS)

    for key, value in six.iteritems(DEFAULT_SWAGGER_SETTINGS):
        if key not in SWAGGER_SETTINGS:
            SWAGGER_SETTINGS[key] = value

except Exception:
    SWAGGER_SETTINGS = DEFAULT_SWAGGER_SETTINGS
