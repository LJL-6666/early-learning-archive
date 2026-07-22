# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:05:03 2018

@author: Dell
"""

## 负面主题分析
neg_dict = corpora.Dictionary(neg[1]) #建立词典
neg_corpus = [neg_dict.doc2bow(i) for i in neg[1]] #建立语料库
neg_lda = models.LdaModel(neg_corpus, num_topics = 3, id2word = neg_dict) #LDA 模型训练
print("\n负面评价")
for i in range(3):
	print("主题%d : " %i)
	print(neg_lda.print_topic(i) ) #输出每个主题

## 正面主题分析
pos_dict = corpora.Dictionary(pos[1])
pos_corpus = [pos_dict.doc2bow(i) for i in pos[1]]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
print("\n正面评价")
for i in range(3):
	print("主题%d : " %i)
	print(pos_lda.print_topic(i) ) #输出每个主题