# coding=utf-8
# !/usr/bin/python

"""
This class in for config file
"""
import configparser


class Config(object):

    def __init__(self):

        config_file = configparser.ConfigParser()
        config_file.read('config.ini')
        section_key = []
        section_value = []
        for each_section in config_file.sections():
            for (each_key, each_val) in config_file.items(each_section):
                section_key.append(str(each_key))
                section_value.append(str(each_val))

        self.section_key = section_key
        # print(self.section_key[2])
        self.section_value = section_value
        # print(self.section_value[2])


if __name__ == '__main__':
    obj = Config()


