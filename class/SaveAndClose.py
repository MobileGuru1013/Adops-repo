# coding=utf-8
"""
Save and Close the file
"""
import pandas as pd


class SaveAndClose(object):

    def __init__(self):
        self.writer = pd.ExcelWriter('{}.xlsx'.format('DisplayNDP'),
                                     engine="xlsxwriter", datetime_format="YYYY-MM-DD")

        self.writer.save()
        self.writer.close()


if __name__ == "__main__":
    obj_save = SaveAndClose()







