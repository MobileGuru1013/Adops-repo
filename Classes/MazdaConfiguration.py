#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Configuration of absolute paths"""
import configparser


class Properties(object):
    """
    read bi.ini file
    """
    def __init__(self):
        """
        Path
        :return:
        """
        config_file = configparser.ConfigParser()
        config_file.read('ConfigMazda.ini')
        self.input_path = config_file['Mazda_path']['Report_Path']
        self.output_path = config_file['Mazda_path']['output_file_path']
        self.mapping_file = config_file['Mazda_path']['mapping_file_path']


if __name__ == "__main__":
    obj_read = Properties()