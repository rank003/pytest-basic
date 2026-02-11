def test_counter_increment_and_decrement(app_page):
    assert app_page.inner_text("#counterValue") == "0"

    app_page.click("#counterIncBtn")
    assert app_page.inner_text("#counterValue") == "1"

    app_page.click("#counterDecBtn")
    assert app_page.inner_text("#counterValue") == "0"


def test_counter_reset(app_page):
    app_page.click("#counterIncBtn")
    app_page.click("#counterIncBtn")
    assert app_page.inner_text("#counterValue") == "2"

    app_page.click("#counterResetBtn")
    assert app_page.inner_text("#counterValue") == "0"
