import subprocess
import time
import socket
import pytest

# --- Previous single-fixture version (kept for later use) ---
# def _get_free_port() -> int:
#     s = socket.socket()
#     s.bind(("127.0.0.1", 0))
#     port = s.getsockname()[1]
#     s.close()
#     return port
#
# @pytest.fixture(scope="session")
# def web_server():
#     """
#     Start a simple static server for index.html/app.js using Python's http.server.
#     """
#     port = _get_free_port()
#     proc = subprocess.Popen(
#         ["python", "-m", "http.server", str(port), "--bind", "127.0.0.1"],
#         stdout=subprocess.DEVNULL,
#         stderr=subprocess.DEVNULL,
#     )
#
#     # Give server a moment to start
#     time.sleep(0.5)
#
#     yield f"http://127.0.0.1:{port}"
#
#     proc.terminate()
#     proc.wait(timeout=5)
#
# def test_page_fetches_typicode_and_renders(playwright, web_server):
#     browser = playwright.chromium.launch()
#     page = browser.new_page()
#
#     page.goto(web_server + "/index.html")
#
#     # Click button that triggers fetch to JsonPlaceholder
#     with page.expect_response(lambda r: "jsonplaceholder.typicode.com/posts/1" in r.url and r.status == 200):
#         page.click("#loadBtn")
#
#     # Assert UI updated
#     page.wait_for_selector("#status:text('Loaded ✅')")
#     title = page.inner_text("#title")
#     body = page.inner_text("#body")
#
#     assert title.strip() != ""
#     assert body.strip() != ""
#
#     browser.close()


def _get_free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.fixture(scope="session")
def web_server_base_url() -> str:
    """
    Start a simple static server for index.html/app.js using Python's http.server.
    """
    port = _get_free_port()
    proc = subprocess.Popen(
        ["python", "-m", "http.server", str(port), "--bind", "127.0.0.1"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Give server a moment to start
    time.sleep(0.5)

    yield f"http://127.0.0.1:{port}"

    proc.terminate()
    proc.wait(timeout=5)


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch()
    yield browser
    browser.close()


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture()
def app_page(page, web_server_base_url):
    page.goto(web_server_base_url + "/index.html")
    return page


def test_page_fetches_typicode_and_renders(app_page):
    # Click button that triggers fetch to JsonPlaceholder
    with app_page.expect_response(
        lambda r: "jsonplaceholder.typicode.com/posts/1" in r.url and r.status == 200
    ):
        app_page.click("#loadBtn")

    # Assert UI updated
    app_page.wait_for_selector("#status:text('Loaded ✅')")
    title = app_page.inner_text("#title")
    body = app_page.inner_text("#body")

    assert title.strip() != ""
    assert body.strip() != ""
