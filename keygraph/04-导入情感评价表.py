# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:04:26 2018

@author: Dell
"""

## 加载情感词表
feeling = pd.read_csv('C:\\Users\\45543\\Desktop\\BosonNLP_sentiment_score.txt', sep = ' ', header = None)
feeling.columns = ['word','score']
feeling.head()

feel = list(feeling['word'])
def classfi(list1):
    SumScore = 0
    for i in  list1:
        if i in feel:
            SumScore += feeling['score'][feel.index(i)]
    return SumScore

date7 = data6.apply(lambda x:classfi(x))  # 对评论情感打分

pos = data6[date7 >= 0]
neg = data6[date7 < 0]
data6[date7 == 0]
pos.to_csv('C:\\Users\\45543\\Desktop\\meidi_jd_pos_delStop.txt', encoding = 'utf-8', index = False, header = False)
neg.to_csv('C:\\Users\\45543\\Desktop\\meidi_jd_neg_delStop.txt', encoding = 'utf-8', index = False, header = False)

negfile = 'C:\\Users\\45543\\Desktop\\meidi_jd_neg_delStop.txt'
posfile = 'C:\\Users\\45543\\Desktop\\meidi_jd_pos_delStop.txt'

neg = pd.read_csv(negfile, encoding = 'utf-8', header = None) #读入数据
pos = pd.read_csv(posfile, encoding = 'utf-8', header = None) 

neg[1] = neg[0].apply(lambda s: s.split(' ')) #定义一个分割函数，然后用 apply 广播
pos[1] = pos[0].apply(lambda s: s.split(' '))