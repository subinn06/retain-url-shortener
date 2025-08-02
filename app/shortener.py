from flask import Blueprint, request, jsonify, redirect
from .utils import generate_code, is_valid_url
from .store import save_url_mapping, get_url, increment_click

shortener_bp = Blueprint('shortener', __name__)

@shortener_bp.route('/api/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    code = generate_code()
    while get_url(code):  # ensure uniqueness
        code = generate_code()

    save_url_mapping(code, original_url)

    return jsonify({
        "short_code": code,
        "short_url": f"http://localhost:5000/{code}"
    }), 201

@shortener_bp.route('/<code>', methods=['GET'])
def redirect_short_url(code):
    record = get_url(code)
    if not record:
        return jsonify({"error": "Short URL not found"}), 404

    increment_click(code)
    return redirect(record['url'])

@shortener_bp.route('/api/stats/<code>', methods=['GET'])
def stats(code):
    record = get_url(code)
    if not record:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "url": record['url'],
        "clicks": record['clicks'],
        "created_at": record['created_at'].isoformat()
    })
