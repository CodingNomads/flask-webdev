from flask import Blueprint
import logging

_LOGGER = logging.getLogger(__name__)

auth = Blueprint('auth', __name__)
_LOGGER.debug("I AM ETERNAL AND THE AUTH Blueberry")

from . import views
