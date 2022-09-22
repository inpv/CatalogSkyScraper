import allure
import openpyxl
from utils.common_check import *
from utils.file_util import FileUtil
from datas.download_datas import DownloadDatas
from datas.builders.xls_data_builder import XlsDataBuilder


@allure.suite('Test Xls Fill')
class TestXlsFill:
    wb = None  # xls workbook object
    ws = None  # xls workbook's worksheet object

    @staticmethod
    def test_xls_fill():
        desc_files = os.listdir(DownloadDatas.DESC_DIR)
        pic_files = os.listdir(DownloadDatas.PIC_DIR)

        # create xls if not yet created
        if not check_file_creation(DownloadDatas.XLS_FILE) and not check_if_file_not_empty(DownloadDatas.XLS_FILE):
            FileUtil.create_xls_file(DownloadDatas.XLS_FILE_NAME)

        TestXlsFill.wb = openpyxl.load_workbook(DownloadDatas.XLS_FILE)  # opening xls file as an object
        TestXlsFill.ws = TestXlsFill.wb[DownloadDatas.XLS_WORKSHEET]

        for desc_file in desc_files:  # looping through all files in html directory
            XlsDataBuilder.fill_rows_with_descs(desc_file=desc_file, ws=TestXlsFill.ws)  # fill rows for each file

        for pic_file in pic_files:  # looping through all files in pic directory
            XlsDataBuilder.create_inner_dict(pic_file=pic_file, ws=TestXlsFill.ws)  # create a dict with pic links

        XlsDataBuilder.fill_rows_with_pics_links(ws=TestXlsFill.ws)  # match the dict with pic names

        TestXlsFill.wb.save(DownloadDatas.XLS_FILE)  # saving the values
        TestXlsFill.wb.close()
