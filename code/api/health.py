import requests
from http import HTTPStatus
from flask import Blueprint, current_app

from api.utils import jsonify_data
from api.errors import (
    UnexpectedError,
    InternalServerError,
    NotFoundError,
    SSLError
)

health_api = Blueprint('health', __name__)


@health_api.route('/health', methods=['POST'])
def health():
    try:
        response = requests.head(current_app.config['UI_URL'],
                                 headers=current_app.config['CTR_HEADERS'])
    except requests.exceptions.SSLError as error:
        raise SSLError(error)

    if response.ok:
        return jsonify_data({'status': 'ok'})

    else:
        expected_response_errors = {
            HTTPStatus.NOT_FOUND: NotFoundError,
            HTTPStatus.INTERNAL_SERVER_ERROR: InternalServerError
        }
        if response.status_code in expected_response_errors:
            raise expected_response_errors[response.status_code]
        else:
            raise UnexpectedError(response)
