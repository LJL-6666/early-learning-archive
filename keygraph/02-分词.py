# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:02:22 2018

@author: Dell
"""

import jieba
## 分词
list(jieba.cut('我爱北京天安门，天安门前国旗升'))
data5 = data4.apply(lambda x: list(jieba.cut(x)))  
data5.head()