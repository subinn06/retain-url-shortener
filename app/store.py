from datetime import datetime

store = {}

# Schema: short_code -> {
#   'url': str,
#   'created_at': datetime,
#   'clicks': int
# }

def save_url_mapping(code, original_url):
    store[code] = {
        'url': original_url,
        'created_at': datetime.utcnow(),
        'clicks': 0
    }

def get_url(code):
    return store.get(code)

def increment_click(code):
    if code in store:
        store[code]['clicks'] += 1
