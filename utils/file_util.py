import wget
from pathlib import Path
from datas.download_datas import DownloadDatas


class FileUtil:

    @staticmethod
    def create_html_file(file_name, sku_desc):

        # create the empty html file
        full_desc_name = DownloadDatas.DESC_DIR + file_name + '.html'
        Path(full_desc_name).touch()

        # writing the descs to a new html file
        html_file = open(full_desc_name, 'wb')  # opening the created file in write mode
        html_file.write(sku_desc)
        html_file.close()

    @staticmethod
    def create_xls_file(xls_file_name):

        # create the empty xls file
        full_file_name = DownloadDatas.XLS_FILE_DIR + xls_file_name + '.xls'
        Path(full_file_name).touch()

    @staticmethod
    def download_image(img_name, img_url):
        wget.download(img_url,
                      DownloadDatas.PIC_DIR + img_name + ".png")  # download the pic
