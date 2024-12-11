__version__ = "1.0.1"

from .client import Client
from .sync_support import add_sync_support

add_sync_support()
