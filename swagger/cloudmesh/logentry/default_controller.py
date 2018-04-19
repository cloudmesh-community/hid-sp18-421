import connexion
import six

from swagger_server.models.log import LOG  # noqa: E501
from swagger_server import util
from log_stub import get_log_entry

def log_get():  # noqa: E501
    """log_get

    Returns log entry from the system # noqa: E501


    :rtype: LOG
    """
    return LOG(get_log_entry())
