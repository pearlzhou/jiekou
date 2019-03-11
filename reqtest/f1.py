# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 16:17
# @Author  : zhouzz
# @FileName: f1.py

import requests

# r=requests.get('http://www.cnblogs.com/yoyoketang')
# print r.status_code
# print r.text

"""http://zzk.cnblogs.com/s/blogpost?Keywords=yoyoketang"""

#params
# para = {'Keywords':'yoyoketang'}
# r=requests.get('http://zzk.cnblogs.com/s/blogpost',params=para)
# print r.text
# print r.headers
# print r.content


r=requests.get('https://www.baidu.com')
print r.status_code
print r.text
print r.headers
print r.content #自动解码headers的内容格式:gzip的数据格式
print r.encoding