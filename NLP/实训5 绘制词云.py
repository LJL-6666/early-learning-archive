import os
os.chdir('/course/文本挖掘实战')

    
# 读取文本文件
with open('./data/鹿鼎记.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
txt = txt.replace('&#39;', '')
txt = txt.replace('\ufeff', '')
txt = txt.split()
txt[:7]


# 查看自定义词典
with open('./data/self_dict.txt', 'r', encoding='utf-8') as f:
    my_dict = f.read()
my_dict = my_dict.split()
my_dict[:5]

# 分词
import jieba
jieba.load_userdict('./data/self_dict.txt')
data_cut = [jieba.lcut(i) for i in txt]
data_cut[:6]


# 导入停用词表
with open('./data/stoplist.txt', 'r', encoding='utf-8') as f:
    stop = f.read()
stop = stop.split()
stop = [' '] + stop
stop[:6]


data_after = [[j for j in i if j not in stop] for i in data_cut]
print(data_cut[:5])
print(data_after[:5])



all_words = []
for i in data_after:
    all_words.extend(i)
print(data_after[:6])
print(all_words[:6])

import pandas as pd
tmp = pd.Series(all_words)
num = tmp.value_counts()
num.head()




import matplotlib.pyplot as plt
from wordcloud import WordCloud

pic = plt.imread('./data/aixin.jpg')
wc = WordCloud(background_color='white', max_words=300,
               font_path='./data/simkai.ttf', 
               mask=pic)
wc2 = wc.fit_words(num)
plt.figure(figsize=(5, 5))
plt.imshow(wc2)
plt.axis('off')
plt.show()

