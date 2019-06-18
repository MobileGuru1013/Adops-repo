#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from LogFile import logger
import pandas as pd
import pandas.io.formats.excel
pandas.io.formats.excel.header_style = None


class AdvertiserList(object):

    def __init__(self, input_file):

        self.input_file = input_file
        self.file_csv = None
        self.writer = None
        self.path = None
        self.file_csv_unique_market = None

    def read_csv(self):
        file_csv = pd.read_excel(self.input_file)
        file_csv_br = file_csv[file_csv['Market'] == 'BR']
        file_csv = file_csv.drop(file_csv_br.index, axis=0)
        file_csv_unique_market = file_csv['Market'].nunique()
        self.file_csv = file_csv
        self.file_csv_unique_market = file_csv_unique_market

    def generate_multiple_file(self):
        df_by_market = self.file_csv.groupby('Market')
        self.path = "C://Adops-Git//Files//"
        for(market, market_df) in df_by_market:
            self.writer = pd.ExcelWriter(self.path + "{}.xlsx".format(market), engine="xlsxwriter")
            # file_name = self.writer
            market_df.to_excel(self.writer, index=False)
            workbook = self.writer.book
            worksheet = self.writer.sheets["Sheet1"]
            worksheet.hide_gridlines(2)
            worksheet.set_column("A:A", 43)
            worksheet.set_column("B:D", 10)
            worksheet.set_zoom(90)
            worksheet.freeze_panes(1, 0)
            format_campaign_info = workbook.add_format({"bold": True, "bg_color": '#00B0F0', "align": "left"})
            worksheet.conditional_format("A1:D1", {"type": "no_blanks", "format": format_campaign_info})
            start_row = 1
            start_col = 0
            end_col = market_df.shape[1]
            end_row = market_df.shape[0]
            border_format = workbook.add_format({'border': 1})
            worksheet.conditional_format(start_row, start_col, end_row, end_col-1,
                                         {"type": "no_blanks", "format": border_format})

            worksheet.conditional_format(start_row, start_col, end_row, end_col-1, {"type": "blanks",
                                                                                    "format": border_format})
            format_num = workbook.add_format({"num_format": "###0"})

            worksheet.conditional_format(start_row, start_col, end_row, end_col - 4,
                                         {"type": "no_blanks", "format": format_num})

            self.writer.save()
            self.writer.close()

    def main(self):
        self.read_csv()
        self.generate_multiple_file()
        logger.info(" {} Advertiser count files have been created. ".format(self.file_csv_unique_market) + " at " +
                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))


if __name__ == "__main__":
    object_advertiser = AdvertiserList('C://Adops-Git//Files//Account_&_Advertisers_List_data.xlsx')
    object_advertiser.main()