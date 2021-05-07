import json


class Config:
    settings = {}
    VERSION = 1.0

    CTR_HEADERS = {
        'User-Agent': (
            'SecureX Threat Response Integrations '
            '<tr-integrations-support@cisco.com>'
        )
    }

    UI_URL = 'http://www.website.com'
    SEARCH_URL = 'https://www.website.com/search?query={value}'

    BROWSE_URL = 'https://www.website.com/host/{ip}'

    OBSERVABLE_TYPES = {
        'ip': 'IP',
        'domain': 'domain',
    }

    CATEGORY = 'Generic Relay'
