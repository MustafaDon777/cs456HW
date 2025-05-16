"""E2E test: Django admin login flow using Playwright"""

from playwright.sync_api import sync_playwright

def test_admin_login():
    with sync_playwright() as playwright:
        browser_instance = playwright.chromium.launch(headless=True)
        context = browser_instance.new_context()
        admin_page = context.new_page()

        # Open the Django admin login page
        admin_page.goto("http://127.0.0.1:8000/admin/")

        # Enter credentials
        admin_page.fill("input[name='username']", "user")
        admin_page.fill("input[name='password']", "password")

        # Trigger form submission
        admin_page.press("input[name='password']", "Enter")

        # Waiting for page content to load post-login
        admin_page.wait_for_selector("body")

        # Verify login by checking for dashboard content
        page_content = admin_page.inner_text("body")
        assert "Site administration" in page_content, "Login fail."

        # Clean up
        browser_instance.close()
