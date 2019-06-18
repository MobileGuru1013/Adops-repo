#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


class TestAdModel(object):

    def __init__(self, training_input, test_input):
        self.readFile = None
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.model_random_predict = None
        self.test_data = None
        self.readFile_views = None
        self.readFile_adViews = None
        self.training_input = training_input
        self.test_input = test_input

    def read_train(self):
        readfile = pd.read_csv(self.training_input)
        readfile['videoID'] = readfile['vidid'].str.extract('(\d+)').astype(int)

        # Filtering the Strings from Int
        readfile = readfile[readfile.views.str.contains('F') == False]
        readfile = readfile[readfile.likes.str.contains('F') == False]
        readfile = readfile[readfile.dislikes.str.contains('F') == False]
        readfile = readfile[readfile.comment.str.contains('F') == False]

        readfile['adview'] = readfile.adview.astype(int)
        readfile['views'] = readfile.views.astype(int)
        readfile['likes'] = readfile.likes.astype(int)
        readfile['dislikes'] = readfile.dislikes.astype(int)
        readfile['comment'] = readfile.comment.astype(int)

        self.readFile = readfile.loc[:, :]

    def read_test(self):
        read_test = pd.read_csv(self.test_input)
        read_test['videoID'] = read_test['vidid'].str.extract('(\d+)').astype(int)

        read_test = read_test[read_test.views.str.contains('F') == False]
        read_test = read_test[read_test.likes.str.contains('F') == False]
        read_test = read_test[read_test.dislikes.str.contains('F') == False]
        read_test = read_test[read_test.comment.str.contains('F') == False]

        read_test['views'] = read_test.views.astype(int)
        read_test['likes'] = read_test.likes.astype(int)
        read_test['dislikes'] = read_test.dislikes.astype(int)
        read_test['comment'] = read_test.comment.astype(int)

        self.test_data = read_test.loc[:, :]

    # linear Model
    def linear_model_prep(self):
        # Creating object of linear model
        model_linear = LinearRegression()

        # Training the model
        model_linear.fit(self.readFile[['views']], self.readFile.adview)

        # predicting the test data adviews
        model_linear_predict_test = model_linear.predict(self.test_data[['views']])
        self.test_data['adViews'] = model_linear_predict_test
        self.test_data.to_csv('test.csv', columns=['vidid',  'adViews'], index=False)

    def plot_data(self):
        plt.xlabel('Views', fontsize=20)
        plt.ylabel('adView', fontsize=20)
        plt.plot(self.test_data.views, self.test_data[['adViews']])
        plt.show()
        plt.savefig('AdViews')

    def main(self):
        self.read_train()
        self.read_test()
        self.linear_model_prep()
        self.plot_data()


if __name__ == "__main__":
    object_train = TestAdModel('ad_org_train.csv', 'ad_org_test.csv')
    object_train.main()



