import os

import requests
import json
import tempfile
import pytest

from src.api import app
from src.logger import logger

URL = 'http://127.0.0.1:5000/tasks/'

