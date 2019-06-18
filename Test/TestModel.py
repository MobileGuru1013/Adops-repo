#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class TrainModel(object):

    def __init__(self):
        self.read_file = None

    def read_csv(self):
        read_file = pd.read_csv('ad_org_train.csv')
        self.read_file = read_file[['vidid', 'adview']]
        print(self.read_file)

    def plot_data(self):
        plot = plt.scatter(self.read_file['vidid'], self.read_file['adview'])
        plot.show()

    def train_data(self):
        X = self.read_file['vidid']
        Y = self.read_file['adview']


    def main(self):
        self.read_csv()
        self.plot_data()


if __name__ == "__main__":
    obj_train = TrainModel()
    obj_train.main()