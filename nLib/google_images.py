from selenium import webdriver

class GoogleSearch(object):
    """
    To represent a search engine and query results from Google.
    """

    def __init__(self):
        """
        Initializes a new search engine
        """
        self.driver = webdriver.Chrome()

    def query(self, query):
        """
        Navigates to the search page with the query
        """
        self.driver.get("https://google.com/search?tbm=isch&safe=true&q=" + query)

    def extend_page(self):
        """
        Scrolls to the bottom of the page and waits for more results to load.
        Returns the new height
        """
        ch = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")
        nh = ch
        while nh == ch:
            nh = self.driver.execute_script("return document.body.scrollHeight;")
        return nh

    def get_html(self):
        """
        Returns the current page HTML
        """
        return self.driver.page_source

e = GoogleSearch()
e.query("dog")
print e.get_html() 