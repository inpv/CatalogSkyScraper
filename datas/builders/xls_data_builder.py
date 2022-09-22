import codecs
from datas.download_datas import DownloadDatas


class XlsDataBuilder:
    min_row = None  # beginning row in xls file
    max_col = None  # column border in xls file
    max_row = None  # row border in xls file

    slice_value_min = 0  # starting point to split the name values from full names with extensions
    desc_slice_value_max = None  # endpoint to split name values for descs
    pic_slice_value_max = None  # endpoint to split name values for pics

    descs_column = None  # column name (int), to which the descs will be saved
    pics_column = None  # column name (int), to which the pics' links will be saved

    inner_dict = {}  # dict for mapping pic names with desc names

    @staticmethod
    def fill_rows_with_descs(desc_file, ws):
        f = codecs.open(DownloadDatas.DESC_DIR + desc_file, 'r', 'utf-8')
        f_contents = f.read()

        # searching for file name occurrence in cells

        for row in ws.iter_rows(min_row=XlsDataBuilder.min_row,
                                max_col=XlsDataBuilder.max_col,
                                max_row=XlsDataBuilder.max_row):
            for cell in row:
                if str(desc_file[XlsDataBuilder.slice_value_min:XlsDataBuilder.desc_slice_value_max]).upper() in str(
                        cell.value).upper():

                    # writing to each cell that has an occurrence
                    ws.cell(
                        column=XlsDataBuilder.descs_column,
                        row=cell.row).value = f_contents  # filling the appropriate column with descs

                    f.close()
                else:
                    pass

    @staticmethod
    def create_inner_dict(pic_file, ws):
        # searching for pic name occurrence in cells

        for row in ws.iter_rows(min_row=XlsDataBuilder.min_row,
                                max_col=XlsDataBuilder.max_col,
                                max_row=XlsDataBuilder.max_row):  # each row in column
            for cell in row:  # each cell in row
                if str(pic_file[XlsDataBuilder.slice_value_min:XlsDataBuilder.pic_slice_value_max]).upper() in str(
                        cell.value).upper():
                    XlsDataBuilder.inner_dict[str(cell.value)] = pic_file
                else:
                    pass

    @staticmethod
    def fill_rows_with_pics_links(ws):
        for row in ws.iter_rows(min_row=XlsDataBuilder.min_row,
                                max_col=XlsDataBuilder.max_col,
                                max_row=XlsDataBuilder.max_row):
            for cell in row:
                for key, value in XlsDataBuilder.inner_dict.items():
                    if key == cell.value:
                        ws.cell(column=XlsDataBuilder.pics_column, row=cell.row).value = (
                                str(DownloadDatas.PIC_DIR) + value)  # filling the column with pic links
                    else:
                        pass
