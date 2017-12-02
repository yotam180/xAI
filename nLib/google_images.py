from selenium import webdriver
from json import loads, dumps
import re


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

    def get_image_objects(self):
        """
        Returns a list of the image objects in the google page
        """
        r = re.findall("(\{\"clt?\"\:(.+?)\})", self.driver.page_source)
        g = []
        for i in r:
            try:
                j = loads(i[0])
                if "tu" in j.keys() and j["tu"].startswith("http"):
                    g.append(j)
            except:
                pass
        return g

    def search(self, query, min_results = 0):
        """
        Performs a google image search
        """
        self.query(query)
        while len(self.get_image_objects()) < min_results:
            self.extend_page()
        return self.get_image_objects()
