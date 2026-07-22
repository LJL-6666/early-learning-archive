#!/usr/bin/env python
# coding: utf-8

# 文本挖掘是一个以半结构（如 WEB 网页）或者无结构（如纯文本）的自然语言文本为对象的数据挖掘，是从大规模文本数据集中发现隐藏的、重要的、新颖的、潜在的有用的规律的过程。，直观的说，当数据挖掘的对象完全由文本这种数据类型组成时，这个过程就称为文本挖掘。文本挖掘也称为文本数据挖掘。
# <img src=a.png height=50% width=60%>

# # 文本预处理技术

# ## 正则表达式

# In[6]:


import re
string = 'The small cake smell good. But it is too small.'
re.match('small', string)  # 从第一个字符开始查看
re.match('The small', string)

re.search('small', string)  # 找一个就好

re.findall('small', string)  # 找出全部

re.sub(pattern='small', repl='big', string=string)  # 替换
re.sub('small', '', string)  # 删除


# In[29]:


string = 'small smell sm.ll smll smaall sm3ll smAll smaaaall sm\nll sm ll'

re.findall('small', string)
re.findall('small|smell', string)
re.findall('sm.ll', string)  # 任意字符，除了\n
re.findall('sm[abcde]ll', string)
re.findall('sm[a-zA-Z0-9]ll', string)
re.findall('sm\.ll', string)  # 转义

re.findall('sm..ll', string)
# 量化符
re.findall('sm.{2}ll', string)
re.findall('sm[a-z]{2,4}ll', string)
re.findall('sm[a-z]?ll', string)  # {0,1}
re.findall('sm[a-z]+ll', string)  # {1,}
re.findall('sm[a-z]*ll', string)  # {0,}
re.findall('sm.*ll', string)  # 贪婪特性


# In[28]:


string = 'My name is YangHui.'
s = re.findall('My name is (.+)\.', string)
s
print('Hi! ' + s[0])
# print('\nHi!'+ 'YangHui')


# 练习：

# In[32]:


rawdata = '555-1239Moe Szyslak(636) 555-0113Burns, C.Montgomery555-6542Rev. Timothy Lovejoy555 8904Ned Flanders636-555-3226Simpson,Homer5553642Dr. Julius Hibbert'
tel = re.findall('\(?[0-9]{0,3}\)?[ -]?[0-9]{3}[ -]?[0-9]{4}', rawdata)
name = re.findall('[A-Z][a-zA-Z ,.]+', rawdata)
import pandas as pd
pd.DataFrame({'name': name, 'Tel': tel})


# In[34]:


re.findall('sm[^a]ll', 'small smell sm\nll')


# ## 分词

# In[35]:


sentence = '今天我来到北京清华大学'


# ### 最大正向匹配法

# In[40]:


sentence = '今天我来到北京清华大学'
words = []
max_len = 5

with open('../data/字典.txt', 'r', encoding='utf-8') as f:
    txt = f.readlines()
my_dict = [i.split()[0] for i in txt]
my_dict[:3]

while len(sentence) != 0:
    tmp = sentence[:max_len]
    while tmp not in my_dict and len(tmp) > 1:
        tmp = tmp[:-1]
    words.append(tmp)
    sentence = sentence[len(tmp):]
print(words)


# ### 最大逆向匹配法（练习）

# In[ ]:


sentence = '今天我来到北京清华大学'
max_len = 5

words = []
while len(sentence) != 0:
    tmp = sentence[-max_len:]
    while tmp not in my_dict and len(tmp) > 1:
        tmp = tmp[1:]
    words = [tmp] + words
    sentence = sentence[:-len(tmp)]
print(words)


# ### HMM

# In[41]:


p_start = {'good':0.63, 'normal':0.17, 'bad':0.2}  # 初始概率矩阵
p_emit = {
    'good':{'working':0.05, 'travel':0.35, 'shopping':0.35, 'running':0.25},
    'normal':{'working':0.25, 'travel':0.25, 'shopping':0.25, 'running':0.25},
    'bad':{'working':0.6, 'travel':0.2, 'shopping':0.05, 'running':0.15}
}  # 发射概率矩阵
p_trans = {
    'good':{'good':0.5, 'normal':0.375, 'bad':0.125},
    'normal':{'good':0.25, 'normal':0.125, 'bad':0.625},
    'bad':{'good':0.25, 'normal':0.375, 'bad':0.375} }  # 转移概率矩阵


# 1、穷举法

# In[ ]:


obs = ['working', 'shopping', 'travel']
states = ['good', 'normal', 'bad']
V = [{}]

# 初始化
for y in states:
    V[0][y] = p_start[y] * p_emit[y][obs[0]]
print(V)

for t in range(1, len(obs)):
    V.append({})
    for y in states:
        for i, j in V[t-1].items():
            pre_state = i.split('-')[-1]
            V[t][i+'-'+y] = j * p_trans[pre_state][y] * p_emit[y][obs[t]]
print(sum([len(i) for i in V]))

(prob, path) = max((j, i) for i,j in V[-1].items())
print(f'观察状态连续为{obs}, 心情可能是{path}, 概率为{prob}')


# 2、维特比算法

# In[46]:


obs = ['working', 'shopping', 'travel']
states = ['good', 'normal', 'bad']

V = [{}]  # 储存节点和对应概率
path = [{}]

# 初始化
for y in states:
    V[0][y] = p_start[y] * p_emit[y][obs[0]]
    path[0][y] = [y]
print(path)
print(V)

for t in range(1, len(obs)):
    V.append({})
    path.append({})
    for y in states:
        em_p = p_emit[y][obs[t]]
        (prob, state) = max((V[t-1][y0]*p_trans[y0][y]*em_p, y0) for y0 in states)
        V[t][y] = prob
        path[t][y] = path[t-1][state] + [y]
print(V[-1])
(prob, last_state) = max((j, i) for i, j in V[-1].items())
path[-1][last_state]
prob


# 3、HMM应用：分词

# In[ ]:





# ### jieba分词

# In[ ]:





# ## 去除停用词

# ## 绘制词云

# # 文本向量表示

# ## 词频

# ## TF-IDF值

# # 常用文本分类器

# ## kNN

# ## Naive Bayes

# ## SVM

# # 模型评估

# In[ ]:




