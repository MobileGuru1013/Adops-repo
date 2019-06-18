# coding=utf-8

"""
This file is used for csv reader
"""
import pandas as pd
from Config import Config


class CsvReader(Config):

    def __init__(self):
        super(CsvReader, self).__init__()
        self.file_path = None
        self.csv_path()

    def csv_path(self):
        file_path = pd.read_csv(self.section_value[2] + 'Performacebymarket.csv', skiprows=9, low_memory=False)
        file_path = file_path[:-1]
        self.file_path = file_path[['Advertiser', 'Advertiser ID', 'Impressions', 'Clicks', 'Media Cost',
                                    'Total Conversions']]

    def main(self):
        self.csv_path()


if __name__ == "__main__":
    object_csv = CsvReader()
    object_csv.main()

