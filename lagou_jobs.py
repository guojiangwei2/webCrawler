#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_jobs(keyword):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
        (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

    keywordbyte = keyword.encode('utf-8')
    keywordindex = str(keywordbyte).replace(r'\x','%').replace(r"'","")
    keywordindex = re.sub('^b','',keywordindex)

    res_lst = []
    hasNextPage = 'true'
    i = 0
    isFirst = lambda x: 'true' if x == 1 else 'false'
    while hasNextPage:
        i += 1
        is_first = isFirst(i)
        url='http://www.lagou.com/jobs/positionAjax.json?px=default&first='\
            + is_first + '&kd=' + keywordindex + '&pn=' + str(i)
        res_dct = requests.get(url, headers = headers).json()
        hasNextPage = res_dct['content']['hasNextPage']
        res = res_dct['content']['result']
        res_lst.extend(res)
        time.sleep(2)

    print res_lst


if __name__ == '__main__':
    get_jobs('数据挖掘')
