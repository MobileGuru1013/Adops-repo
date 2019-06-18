# coding=utf-8
# !/usr/bin/env python


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


class PredictHousePrice(object):

    def __init__(self, input_file):

        self.input_file = input_file
        self.house_price = None
        self.X_one = None
        self.y_one = None

    def read_file(self):

        house_price = pd.read_csv(self.input_file)
        self.house_price = house_price[house_price.columns[::-1]]

    # Bonus Exercise: Predict housing prices based on median_income and plot the regression chart.
    def median_income_predict_house_price(self):

        # Seprate the data with features and label
        X_one = self.house_price.iloc[:, 1:8]
        y_one = self.house_price.iloc[:, :1]
        self.X_one = X_one
        self.y_one = y_one
    # Deal with missing values

    def handling_missing_values(self):
        self.X_one['total_bedrooms'].fillna(self.X_one['total_bedrooms'].mean(), inplace=True)
        # missing_value_imputer = SimpleImputer(missing_values='nan', strategy='mean', verbose=0)
        # missing_value_imputer.fit(self.X_one['total_bedrooms'].values.reshape(-1, 1))
        # self.X_one['total_bedrooms'] = missing_value_imputer.transform(self.X_one['total_bedrooms'].values.reshape
        #                                                                (-1, 1))

        # self.X_one['total_bedrooms'] = missing_value_imputer.fit_transform(self.X_one['total_bedrooms'])

    def main(self):
        self.read_file()
        self.median_income_predict_house_price()
        self.handling_missing_values()


if __name__ == "__main__":
    obj = PredictHousePrice('housing.csv')
    obj.main()