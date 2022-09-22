class LinksListBuilder:

    @staticmethod
    def create_products_list(links):
        product_links_list = []

        for link in links:
            link_href = link.get_attribute('href')  # getting the link to the product itself
            product_links_list.append(link_href)  # filling the list with links

        return product_links_list
