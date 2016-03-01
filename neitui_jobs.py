#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup


def get_info():

    url = 'http://www.neitui.me/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
               (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    r = requests.get(url, headers=headers).content

    soup = BeautifulSoup(r)

    # top jobs
    #jobs = soup.find(class_='topjobs')
    #for x in jobs.find_all('li'):
    #    print x.find(class_="padding-r10")

    # job list
    for x in soup.find_all(class_='jobnote-l'):
        print x.find(class_='padding-r10').string


if __name__ == '__main__':
    get_info()
