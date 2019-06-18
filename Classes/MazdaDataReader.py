#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from MazdaConfiguration import Properties
import glob
import datetime
import xlsxwriter
import pandas.io.formats.excel
pandas.io.formats.excel.header_style = None


class Mazda(Properties):

    def __init__(self):
        super(Mazda, self).__init__()
        self.frame = None
        self.site_name = None
        self.placement_name = None
        self.site_placement_product = None
        self.model_name = None
        self.cpm_value = None
        self.site_placement_product_cpm = None
        self.writer = None

    def output_report(self):
        previous_week = datetime.date(2018, 10, 01).isocalendar()[1]
        current_week = datetime.datetime.now().date().isocalendar()[1]

        final_week = previous_week - current_week

        report_name = 'PY153_P3_In Market Display_Week-{}.xlsx'.format(final_week)
        self.writer = pd.ExcelWriter(self.output_path + report_name, engine="xlsxwriter")

    def read_file(self):
        all_files = glob.glob(self.input_path + "*.csv")
        list_ = []
        for file_ in all_files:
            df = pd.read_csv(file_, index_col=None, header=0)
            list_.append(df)
        frame = pd.concat(list_, sort=True)
        self.frame = frame
        # print(self.frame.dtypes)

    def read_site(self):
        site_name = pd.read_csv(self.mapping_file + 'placementsitename.csv')
        placement_name = pd.read_csv(self.mapping_file + 'placementmappingname.csv')
        model_name = pd.read_csv(self.mapping_file + 'placementmodelname.csv')
        cpm_value = pd.read_csv(self.mapping_file + 'placementcpmname.csv')

        self.site_name = site_name
        self.placement_name = placement_name
        self.model_name = model_name
        self.cpm_value = cpm_value

    def merging_site_data(self):
        site_name_merge = [self.frame, self.site_name, self.placement_name, self.model_name]
        site_placement_product = reduce(lambda left, right: pd.merge(left, right, on='Placement'), site_name_merge)
        self.site_placement_product = site_placement_product

        product_cpm_merge = [self.site_placement_product, self.cpm_value]
        site_placement_product_cpm = reduce(lambda left, right: pd.merge(left, right, on='Product'), product_cpm_merge)
        self.site_placement_product_cpm = site_placement_product_cpm

        self.site_placement_product_cpm['Total Media Cost'] = self.site_placement_product_cpm['Impressions'] \
                                                              / 1000 * self.site_placement_product_cpm['CPM']

        self.site_placement_product_cpm['Date'] = pd.to_datetime(self.site_placement_product_cpm['Date'])

        self.site_placement_product_cpm.sort_values(by=['Date'], inplace=True)

        self.site_placement_product_cpm['Week'] = pd.factorize(self.site_placement_product_cpm['Date'].dt.
                                                               weekofyear)[0] + 1

        self.site_placement_product_cpm['Month'] = self.site_placement_product_cpm['Date'].dt.strftime("%B")

        self.site_placement_product_cpm['Period'] = 'P3'

        # self.site_placement_product_cpm.to_excel(self.writer, index=False)

    def file_save_close(self):
        self.writer.save()
        self.writer.close()

    def main(self):
        # self.output_report()
        self.read_file()
        self.read_site()
        self.merging_site_data()
        # self.file_save_close()


if __name__ == "__main__":
    Object_Mazda = Mazda()
    Object_Mazda.main()
