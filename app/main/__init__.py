from flask import Blueprint
from ..models import Permission
import logging

_LOGGER = logging.getLogger(__name__)

main = Blueprint('main', __name__)
_LOGGER.debug("MAIN BLUEPRINT INITIALIZING")

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

from . import views
