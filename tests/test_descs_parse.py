import time
import allure
from pages.web_page import NavHelper
from utils.file_util import FileUtil
from utils.pytest_marks import browser, title
from utils.common_check import *
from datas.builders.descs_builder import DescsBuilder
from datas.builders.link_list_builder import LinksListBuilder
from datas.webpage_datas import PageLocators
from datas.connection_datas import ConnectionDatas


@allure.suite('Test Descs Parsing')
@browser
class TestDescsParse:
    @title('Scrape the descriptions text from pages and download them into .html format')
    def test_descs_parse(self):
        with allure.step('Initialize page object'):
            web_page = NavHelper(browser)  # initialize page object
            check_if_variable_is_not_empty(web_page)

        for url in ConnectionDatas.URLS_TO_PARSE:
            with allure.step('Load the URL at ' + str(url)):
                web_page.go_to_page(url)  # open catalog page

            with allure.step('Build product links list for URL ' + str(url)):
                products_links_list = LinksListBuilder.create_products_list(
                    web_page.find_elements(
                        PageLocators.LOCATOR_PRODUCT_CARD))  # create a list of sku links
                check_if_variable_is_not_empty(products_links_list)

            for sku in products_links_list:
                with allure.step('Open the webpage for SKU ' + str(sku)):
                    web_page.go_to_page(sku)  # open each sku page

                with allure.step('Create the filename for SKU ' + str(sku)):
                    file_name = web_page.find_element(
                        PageLocators.LOCATOR_IMAGE).text  # get each sku name from image text
                    check_if_variable_is_not_empty(file_name)

                with allure.step('Create final description for SKU ' + str(sku)):
                    sku_desc = DescsBuilder.add_attrs(DescsBuilder.create_raw_descs(sku))
                    check_if_variable_is_not_empty(sku_desc)

                with allure.step('Create html file for SKU ' + str(sku)):
                    FileUtil.create_html_file(file_name=file_name, sku_desc=sku_desc)

                with allure.step('Go back'):
                    browser.execute_script("window.history.go(-1)")  # going back

                time.sleep(3)  # wait until the page loads

            with allure.step('Clear previous products links list for URL ' + str(url)):
                products_links_list.clear()  # prevent from adding elements from previous cycle
