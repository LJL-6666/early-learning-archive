import requests
import re
import pandas as pd
import time
import os
import random

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

r1 = '<img alt="(.*?)" src='
re1 = re.compile(r1)
def get_data(url_):
    titles = []
    data = requests.get(url_,headers = headers).text
    df1 = re1.findall(data)
    titles.extend(df1)
    results = pd.DataFrame()
    results['标题'] = titles
    return results


# 创建存储路径，需要保证有底盘，可以改为其他的目录
try:
    os.mkdir('D:/bilibili/')
except BaseException as be:
    print(be)

url = 'https://www.bilibili.com/ranking/all/3/0/3'

urls = ['https://www.bilibili.com/ranking/all/0/0/3',
        'https://www.bilibili.com/ranking/all/1/0/3',
        'https://www.bilibili.com/ranking/all/168/0/3',
        'https://www.bilibili.com/ranking/all/3/0/3',
        'https://www.bilibili.com/ranking/all/129/0/3',
        'https://www.bilibili.com/ranking/all/4/0/3',
        'https://www.bilibili.com/ranking/all/36/0/3',
        'https://www.bilibili.com/ranking/all/188/0/3',
        'https://www.bilibili.com/ranking/all/160/0/3',
        'https://www.bilibili.com/ranking/all/119/0/3',
        'https://www.bilibili.com/ranking/all/155/0/3',
        'https://www.bilibili.com/ranking/all/5/0/3',
        'https://www.bilibili.com/ranking/all/181/0/3'
        ]

labels = ['全站','动画','国创相关','音乐','舞蹈','游戏',
        '科技','数码','生活','鬼畜','时尚','娱乐','影视']

datass = pd.DataFrame()
for url,label in zip(urls,labels):
    print(label+'--类别开始爬取')
    resultss = get_data(url)
    resultss['所属'] = label
    resultss['排名'] = list(range(1,len(resultss)+1))
    datass = pd.concat([datass,resultss])
    time.sleep(random.uniform(2,4))
# 将数据保存在excel中        
datass.to_excel('D:/bilibili/数据.xlsx',index = None)

