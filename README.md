# Typicode E2E (pytest + Playwright)

A tiny static webpage that fetches a post from JsonPlaceholder (typicode.com) and an E2E test that verifies the UI updates.

## Files
- `index.html` + `app.js` : the webpage
- `tests/test_e2e_typicode.py` : E2E test (pytest + Playwright)
- `requirements.txt` : python deps
- `pytest.ini` : pytest config

## Run locally

### 1) Create and activate a virtual env (optional but recommended)
```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows
# .venv\Scripts\activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 3) Run the E2E tests
```bash
pytest -v
```

Notes:
- The test starts a local static server using `python -m http.server`
- The test makes a real request to `https://jsonplaceholder.typicode.com/posts/1`
