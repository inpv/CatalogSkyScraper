from dataclasses import dataclass


@dataclass
class DownloadDatas:
    PIC_DIR = ""  # fill your pic dir here
    DESC_DIR = ""  # fill your desc dir here
    XLS_FILE = ""  # fill your xls file's absolute link here
    XLS_FILE_DIR = ""  # fill your xls file's directory here
    XLS_FILE_NAME = ""  # fill the new xls file's name, if it's not yet created
    XLS_WORKSHEET = ""  # fill your Excel worksheet name here
