# URL Shortener Service

This project is a minimal Flask-based URL shortening service, similar to bit.ly or TinyURL.

## 📦 Features

* Shorten long URLs with a POST request
* Redirect via short code
* Track click counts
* View stats (clicks, timestamp, original URL)
* In-memory store (no database)

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file:

```bash
pip install flask pytest
```

### 2. Run the Server

```bash
python run.py
```

Server will start at:

```
http://localhost:5000
```

---

## 🔌 API Endpoints

### `POST /api/shorten`

Shorten a long URL

```bash
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/very/long/url"}'
```

**Response:**

```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

### `GET /<short_code>`

Redirect to the original URL

### `GET /api/stats/<short_code>`

Returns click stats, creation time, and original URL

---

## ✅ Running Tests

Make sure Flask is installed, then:

```bash
pytest test_app.py
```

Tests cover:

* URL shortening
* Invalid input
* Redirects
* Stats
* 404s

---

## 📁 Project Structure

```
url-shortener/
├── app/
│   ├── __init__.py
│   ├── shortener.py
│   ├── utils.py
│   └── store.py
├── run.py
├── test_app.py
├── requirements.txt
└── README.md
```

---

## ✍️ Notes

* URLs must be valid and contain a scheme (http/https)
* Short codes are 6-char alphanumeric and unique
* All data is stored in-memory (resets on restart)

---

✅ Built with Flask — no external database or dependencies required.
