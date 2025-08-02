import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_shorten_valid_url(client):
    res = client.post('/api/shorten', json={"url": "https://example.com"})
    assert res.status_code == 201
    assert 'short_code' in res.get_json()

def test_shorten_invalid_url(client):
    res = client.post('/api/shorten', json={"url": "invalid-url"})
    assert res.status_code == 400

def test_redirect_and_stats(client):
    # create short URL
    res = client.post('/api/shorten', json={"url": "https://example.com/page"})
    data = res.get_json()
    code = data['short_code']

    # redirect
    redirect_res = client.get(f'/{code}', follow_redirects=False)
    assert redirect_res.status_code == 302

    # stats
    stats_res = client.get(f'/api/stats/{code}')
    stats_data = stats_res.get_json()
    assert stats_data['url'] == "https://example.com/page"
    assert stats_data['clicks'] == 1

def test_redirect_invalid_code(client):
    res = client.get('/nope')
    assert res.status_code == 404

def test_stats_invalid_code(client):
    res = client.get('/api/stats/404notfound')
    assert res.status_code == 404
