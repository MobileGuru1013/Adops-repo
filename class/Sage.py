# coding=utf-8
"""
Combining Xlsx File
"""
import pandas as pd
import glob
import xlsxwriter


class SageData(object):

    def __init__(self):
        self.all_data = None
        self.writer = pd.ExcelWriter('C:/Users/dharmendra.mishra/Desktop/Reports/Sage UKI - 3rd Party/output.xlsx',
                                     engine="xlsxwriter", datetime_format="YYYY-MM-DD")

    def read_sage(self):
        all_data = pd.DataFrame()
        for f in glob.glob("C:/Users/dharmendra.mishra/Desktop/Reports/Sage UKI - 3rd Party/*.xlsx"):
            df = pd.read_excel(f, sheet_name='Sheet1')
            all_data = all_data.append(df, ignore_index=True)

        self.all_data = all_data

    def dump_sage(self):

        df = self.all_data.to_excel(self.writer,
                                    index=False, header=True)

    def saveAndCloseWriter(self):
        self.writer.save()
        self.writer.close()

    def main(self):
        self.read_sage()
        self.dump_sage()
        self.saveAndCloseWriter()


if __name__ == "__main__":
    obj = SageData()
    obj.main()

















