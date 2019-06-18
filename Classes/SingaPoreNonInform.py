# coding=utf-8
# !/usr/bin/env python

import datetime
import pandas as pd
from LogFile import logger
import glob


class NonInform(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.writer = None
        self.summary_data = None
        self.new_leads_data = None
        self.all_leads_data = None

    def output_report(self):

        report_name = 'NonInformReportTracker.xlsx'
        self.writer = pd.ExcelWriter(self.file_path + report_name, engine="xlsxwriter")

    def read_files(self):
        summary_data = pd.DataFrame()
        new_leads_data = pd.DataFrame()
        all_leads_data = pd.DataFrame()
        for f in glob.glob(self.file_path + "*.xlsx"):
            df_summary = pd.read_excel(f, sheet_name=0)
            df_new_leads = pd.read_excel(f, sheet_name=1)
            df_all_leads = pd.read_excel(f, sheet_name=2)
            summary_data = summary_data.append(df_summary, ignore_index=True)
            new_leads_data = new_leads_data.append(df_new_leads, ignore_index=True)
            all_leads_data = all_leads_data.append(df_all_leads, ignore_index=True)

        self.summary_data = summary_data
        self.new_leads_data = new_leads_data
        self.all_leads_data = all_leads_data


        filter_leads = self.summary_data.loc[self.summary_data['CAMPAIGN SUMMARY'].isin(['This report', 'This Report'])]

        # print(filter_leads)

        # print(self.all_data.loc[:, ~self.all_data.columns.str.contains('^Unnamed')])

    def main(self):
        self.output_report()
        self.read_files()


if __name__ == "__main__":
    obj_NonInform = NonInform('C://Users//dharmendra.mishra//Desktop//Reports//'
                              'Thursday-Monday//IBM_Singapore_Report//Non_inform Reports//test//')
    obj_NonInform.main()