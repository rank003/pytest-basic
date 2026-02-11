import socket
import subprocess
import time
from typing import Generator
import sys

import pytest


def _get_free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.fixture(scope="session")
def web_server_base_url() -> Generator[str, None, None]:
    """
    Start a simple static server for index.html/app.js using Python's http.server.
    """
    port = _get_free_port()
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
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
