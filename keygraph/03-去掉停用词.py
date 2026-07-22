# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:03:47 2018

@author: Dell
"""


## 加载停止词
stop = pd.read_csv('C:\\Users\\45543\\Desktop\\stoplist1.txt', sep='yang', encoding = 'utf-8', header = None)
# sep设置为文档内不包含的内容，否则出错
stop = [' ', ''] + list(stop[0]) 	#Pandas自动过滤了空格符，这里手动添加
data6 = data5.apply(lambda x: [i for i in x if i not in stop])
# 去除停止词前后对比
data6.apply(lambda x: len(x)).sum()
data5.apply(lambda x: len(x)).sum()