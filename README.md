# Typicode E2E (pytest + Playwright)

A tiny static webpage that includes a simple component (counter) and fetches posts from JsonPlaceholder (typicode.com), with both component and E2E tests.

## Files
- `index.html` + `app.js` : the webpage
- `tests/test_component_ui.py` : component UI tests (pytest + Playwright)
- `tests/test_e2e_typicode.py` : E2E tests (pytest + Playwright)
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
- The E2E tests make real requests to `https://jsonplaceholder.typicode.com/posts/1` and `/posts/2`
