#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
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

        readfile['adview'] = readfile.adview.astype(float)
        readfile['views'] = readfile.views.astype(float)
        readfile['likes'] = readfile.likes.astype(float)
        readfile['dislikes'] = readfile.dislikes.astype(float)
        readfile['comment'] = readfile.comment.astype(float)

        # self.readFile_views = readfile[['views']]
        # self.readFile_adViews = readfile[['adview']]
        self.readFile = readfile.loc[:, :]

    def read_test(self):
        read_test = pd.read_csv(self.test_input)
        read_test['videoID'] = read_test['vidid'].str.extract('(\d+)').astype(int)

        read_test = read_test[read_test.views.str.contains('F') == False]
        read_test = read_test[read_test.likes.str.contains('F') == False]
        read_test = read_test[read_test.dislikes.str.contains('F') == False]
        read_test = read_test[read_test.comment.str.contains('F') == False]

        read_test['views'] = read_test.views.astype(float)
        read_test['likes'] = read_test.likes.astype(float)
        read_test['dislikes'] = read_test.dislikes.astype(float)
        read_test['comment'] = read_test.comment.astype(float)

        self.test_data = read_test.loc[:, :]

    def plot_data(self):
        plt.xlabel('Views')
        plt.ylabel('adView')
        # plt.scatter(self.readFile['views'], self.readFile['adview'], marker='+')

        plt.scatter(self.readFile_views, self.readFile_adViews, marker='+')

        plt.show()
        # plt.savefig('AdViews')

    # Preparing X and Y
    def train_split(self):
        # x_data = self.readFile[['views', 'likes', 'dislikes', 'comment']]
        x_data = self.readFile.iloc[:, 2]
        # y_data = self.readFile[['adview']]
        y_data = self.readFile.iloc[:, 1]

        # spliting the data set
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x_data, y_data, train_size=0.8,
                                                                                test_size=0.2)

    # Scalling up data
    def scale_data(self):
        sc = StandardScaler()
        self.x_train = sc.fit_transform(self.x_train)
        self.x_test = sc.transform(self.x_test)

    # linear Model
    def linear_model_prep(self):
        model_linear = LinearRegression()
        # model_linear.fit(self.x_train, self.y_train)
        model_linear.fit(self.readFile[['views']], self.readFile.adview)
        # model_linear_predict_train = model_linear.predict(self.x_test)
        model_linear_predict_test = model_linear.predict(self.test_data)
        # print(model_linear_predict_train)
        print (model_linear_predict_test)
        # print(model_linear.score(self.x_test, self.y_test))

        self.test_data['adViews'] = model_linear_predict_test
        print(self.test_data)

    # Regression  Model
    def random_forest_prep(self):
        model_random = RandomForestRegressor(n_estimators=20, random_state=0)
        model_random.fit(self.x_train, self.y_train)
        self.model_random_predict = model_random.predict(self.x_test)

        print(self.model_random_predict)
        print(model_random.score(self.x_test, self.y_test))

    def evaluate_random_forest(self):
        print('Mean Absolute Error:', metrics.mean_absolute_error(self.y_test, self.model_random_predict))
        print('Mean Squared Error:', metrics.mean_squared_error(self.y_test, self.model_random_predict))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(self.y_test, self.model_random_predict)))

        # KNeighborsClassifier
    def k_neighbour_prep(self):
        model_k_neighbour = KNeighborsClassifier(n_neighbors=50)
        model_k_neighbour.fit(self.x_train, self.y_train)
        model_k_neighbour_predict = model_k_neighbour.predict(self.x_test)
        print(model_k_neighbour_predict)
        print(model_k_neighbour.score(self.x_test, self.y_test))

    def main(self):
        self.read_train()
        self.read_test()
        self.plot_data()
        # self.train_split()
        # self.scale_data()
        self.linear_model_prep()
        # self.random_forest_prep()
        # self.evaluate_random_forest()
        # self.k_neighbour_prep()


if __name__ == "__main__":
    object_train = TestAdModel('ad_org_train.csv', 'ad_org_test.csv')
    object_train.main()



