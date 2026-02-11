import pytest


@pytest.mark.parametrize("post_id", [1, 2])
def test_page_fetches_typicode_and_renders(app_page, post_id):
    app_page.fill("#postIdInput", str(post_id))

    with app_page.expect_response(
        lambda r: f"jsonplaceholder.typicode.com/posts/{post_id}" in r.url
        and r.status == 200
    ):
        app_page.click("#loadPostBtn")

    app_page.wait_for_selector(f"#postStatus:text('Loaded {post_id} ✅')")
    title = app_page.inner_text("#postTitle")
    body = app_page.inner_text("#postBody")

    assert title.strip() != ""
    assert body.strip() != ""
