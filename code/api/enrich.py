from functools import partial

from flask import Blueprint, current_app
from urllib.parse import quote

from api.schemas import ObservableSchema
from api.utils import get_json, jsonify_data

enrich_api = Blueprint('enrich', __name__)


get_observables = partial(get_json, schema=ObservableSchema(many=True))


@enrich_api.route('/deliberate/observables', methods=['POST'])
def deliberate_observables():
    # There are no verdicts to extract.
    return jsonify_data({})


@enrich_api.route('/observe/observables', methods=['POST'])
def observe_observables():
    # Not implemented.
    return jsonify_data({})


def get_browse_pivot(ip):
    return {
        'id': f'ref-detail-ip-{ip}',
        'title': 'Browse IP',
        'description': 'Browse this IP',
        'url': current_app.config['BROWSE_URL'].format(ip=ip),
        'categories': ['Browse', current_app.config['CATEGORY']],
    }


def get_search_pivot(type, value):
    return {
        'id': f'ref-search-{type}-{quote(value, safe="")}',
        'title':
            'Search for this'
            f' {current_app.config["OBSERVABLE_TYPES"][type]}',
        'description':
            'Lookup this '
            f'{current_app.config["OBSERVABLE_TYPES"][type]}',
        'url': current_app.config['SEARCH_URL'].format(
            value=quote(value, safe='')
        ),
        'categories': ['Search', current_app.config['SEARCH_URL']],
    }


@enrich_api.route('/refer/observables', methods=['POST'])
def refer_observables():
    observables = get_observables()
    data = []

    for observable in observables:
        value = observable['value']
        type = observable['type'].lower()

        if type in current_app.config['OBSERVABLE_TYPES']:
            data.append(get_search_pivot(type, value))
            if type == 'ip':
                data.append(get_browse_pivot(value))

    return jsonify_data(data)
