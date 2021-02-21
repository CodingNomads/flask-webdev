from flask import Blueprint
import logging
_LOGGER = logging.getLogger(__name__)

api = Blueprint('api', __name__)
_LOGGER.debug("I AM ETERNAL AND THE API Blueberry")

from . import authentication, compositions, users, comments, errors