import time
import allure
from pages.web_page import NavHelper
from utils.file_util import FileUtil
from datas.builders.link_list_builder import LinksListBuilder
from datas.webpage_datas import PageLocators
from datas.connection_datas import ConnectionDatas


@allure.suite('Test Images Parsing')
class TestImagesParse:

    web_page = None
    products_links_list = None

    @staticmethod
    def test_descs_parse(browser):
        TestImagesParse.web_page = NavHelper(browser)  # initialize page object

        for url in ConnectionDatas.URLS_TO_PARSE:
            TestImagesParse.web_page.go_to_page(url)  # open catalog page

            TestImagesParse.products_links_list = LinksListBuilder.create_products_list(
                TestImagesParse.web_page.find_elements(
                    PageLocators.LOCATOR_PRODUCT_CARD))  # create a list of sku links

            for sku in TestImagesParse.products_links_list:
                TestImagesParse.web_page.go_to_page(sku)  # open each sku page

                img_name = TestImagesParse.web_page.find_element(
                    PageLocators.LOCATOR_IMAGE).text  # get each sku name from image text

                img_url = \
                    TestImagesParse.web_page.find_element(
                        PageLocators.LOCATOR_IMAGE).get_attribute(
                        'src')  # link to pic

                FileUtil.download_image(img_name, img_url)

                browser.execute_script("window.history.go(-1)")  # going back
                time.sleep(3)  # wait until the page loads

            TestImagesParse.products_links_list.clear()  # prevent from adding elements from previous cycle
