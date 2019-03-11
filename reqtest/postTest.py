# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 16:45
# @Author  : zhouzz
# @FileName: postTest.py

import requests
import json
payload={'yoyo':'Hello World!',
		 'pythonQQ群':'226296743'
		 }
# r=requests.post('http://httpbin.org/post',data=payload)
# print r.text

data_json=json.dumps(payload)
r=requests.post('http://httpbin.org/post',json=payload)
print r.text