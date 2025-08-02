import re
import random
import string
from urllib.parse import urlparse

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)