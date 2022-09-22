import requests  # to load web pages into an object
from bs4 import BeautifulSoup  # creating and filtering descriptions


class DescsBuilder:

    @staticmethod
    def create_raw_descs(link_inside):

        def _remove_all_attrs(text):  # removing tag attributes
            for tag in text.find_all(True):
                tag.attrs = {}
            return text

        # FORMING THE DESCRIPTIONS

        page = requests.get(link_inside)  # getting the object from url
        soup = BeautifulSoup(page.content, 'html.parser')  # loading it into the soup
        desc_divs = []  # a list for all descs' divs

        # do something with the attrs
        """
        YOUR CODE HERE
        """

        soup.clear()  # clearing the old soup

        for desc_div in desc_divs:  # loading the new soup with objects from the list
            soup.append(desc_div)

        soup_without_attrs = _remove_all_attrs(soup)  # removing all unnecessary attrs

        return soup_without_attrs

    @staticmethod
    def add_attrs(soup):

        # ADDING NEEDED ATTRIBUTES, E.G.:

        def create_new_breakline_tag():
            breakline_tag = soup.new_tag('br')
            return breakline_tag

        def create_new_bold_tag():
            bold_tag = soup.new_tag('b')
            return bold_tag

        # add new attrs
        """
        YOUR CODE HERE
        """

        pretty_text = soup.prettify().encode('utf-8')  # final pretty version

        return pretty_text
