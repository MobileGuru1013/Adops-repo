# coding=utf-8
# !/usr/bin/env python

from Advertiser_list import AdvertiserList
from JiraWrapper import Jira

if __name__ == "__main__":
    object_Advertiser = AdvertiserList("C://Adops-Git//Files//Account_&_Advertisers_List_data.xlsx")
    object_Advertiser.main()

    object_JiraWrapper = Jira(username='Dharmendra.mishra@neomediaworld.com', password='Password1')
    object_JiraWrapper.main()
