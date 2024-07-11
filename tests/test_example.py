
def test_hellow_google(browser):
    browser.get('https://www.google.com')
    assert 'Google' in browser.title
