#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jira import JIRA
# import requests
import urllib3
# requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class JiraException(Exception):
    pass


class Jira(object):
    __options = {
        'server': 'https://neomediaworld.atlassian.net',
        'verify': False
    }
    __client = None

    def __init__(self, **kwargs):
        if len(kwargs) != 2:
            raise JiraException(
                'In order to use this class you need to specify a user and a password as keyword arguments!')
        else:
            if 'username' in kwargs.keys():
                self.__username = kwargs['username']
            else:
                raise JiraException('You need to specify a username as keyword argument!')
            if 'password' in kwargs.keys():
                self.__password = kwargs['password']
            else:
                raise JiraException('You need to specify a password as keyword argument!')

            try:
                self.__client = JIRA(self.__options, basic_auth=(self.__username, self.__password))
            except:
                raise JiraException('Could not connect to the API, invalid username or password!')

    def __str__(self):
        return 'Jira(username = {}, password = {}, endpoint = {}'.format(self.__username, self.__password,
                                                                         self.__options['server'])

    def __repr__(self):
        return 'Jira(username = {}, password = {}, endpoint = {}'.format(self.__username, self.__password,
                                                                         self.__options['server'])

    def __format__(self, r):
        return 'Jira(username = {}, password = {}, endpoint = {}'.format(self.__username, self.__password,
                                                                         self.__options['server'])

    def get_projects(self, raw=False):
        projects = []
        for project in self.__client.projects():
            if raw:
                projects.append(project)
            else:
                projects.append({'Name': project.key, 'Description': project.name})
        return projects

    def get_issues(self, max_results=10, raw=False, **kwargs):
        issues = []
        if len(kwargs) < 1:
            raise JiraException('You need to specify a search criteria!')
        else:
            search_string = ' '.join([(_ + "=" + kwargs[_]) if _ != 'condition' else kwargs[_] for _ in kwargs])
            for item in self.__client.search_issues(search_string, maxResults=max_results):
                if raw:
                    issues.append(item)
                else:
                    issues.append({'Assignee': item.fields.assignee, 'TimeSpent': item.fields.timespent,
                                   'CreateDate': item.fields.created, 'DueDate': item.fields.duedate,
                                   'ResolutionDate': item.fields.resolutiondate, 'Status': item.fields.status,
                                   'Peer Reviewer': item.fields.customfield_13307, 'Reporter': item.fields.reporter,
                                   'Name': str(item), 'Summary': item.fields.summary,
                                   'Description': item.fields.description})
        return issues

    def transition(self, issue, transition):
        pass

    def new_issue(self, **kwargs):
        pass

    def comment_issue(self, issue, comment):
        pass


if __name__ == '__main__':
    MyJira = Jira(username='Dharmendra.mishra@neomediaworld.com', password='Password1')
    print(MyJira.get_projects())
    # print(MyJira.get_issues(project='Media Ops Sage', condition='AND', status='Closed'))