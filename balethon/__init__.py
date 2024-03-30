__version__ = "0.6.6"

from .client import Client
from .sync_support import add_sync_support

add_sync_support()
