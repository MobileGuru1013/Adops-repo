# coding=utf-8

import pandas as pd
import numpy as np
from CsvReader import CsvReader


class PerformanceDataThirdParty(CsvReader):

    def __init__(self):
        super(PerformanceDataThirdParty, self).__init__()
        self.processing_data_new = None
        self.writer = pd.ExcelWriter('{}.xlsx'.format('Display'),
                                     engine="xlsxwriter", datetime_format="YYYY-MM-DD")

    def processing_csv(self):
        processing_data = pd.pivot_table(self.file_path, index=['Advertiser'],
                                         values=['Impressions', 'Clicks', 'Media Cost',
                                                 'Total Conversions'], aggfunc=np.sum)

        processing_data_new = processing_data.reset_index()

        self.processing_data_new = processing_data_new

    def csv_loader(self):

        load_excel = self.processing_data_new.to_excel(self.writer, index=False, header=True)

    def saveAndCloseWriter(self):
        self.writer.save()
        self.writer.close()

    def main(self):
        self.processing_csv()
        self.csv_loader()
        self.saveAndCloseWriter()


if __name__ == '__main__':
    Object_Performance = PerformanceDataThirdParty()
    Object_Performance.main()

