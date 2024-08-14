class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_catalog_page(self,base_url):
        self.browser.get(base_url + "en-gb/catalog/smartphone")

    def go_to_main_page(self,base_url):
        self.browser.get(base_url)

    def go_to_macbook_page(self,base_url):
        self.browser.get(base_url + "en-gb/product/macbook")

    def go_to_reg_page(self,base_url):
        self.browser.get(base_url + "/index.php?route=account/register")

