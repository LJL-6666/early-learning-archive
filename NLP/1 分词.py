#!/usr/bin/env python
# coding: utf-8

# # 分词

# ## 1.1最大正向匹配法

# 1、读取字典文件

# In[1]:


with open('../data/字典.txt', encoding='utf-8') as f:
    txt = f.readlines()
    
print(txt[:4])
dictionary = [i.split()[0] for i in txt]
print(dictionary[:4])
print(len(dictionary))


# 2、最大正向匹配法

# In[2]:


sentence = '今天我来到北京清华大学。'
max_len = 5


# In[3]:


words = []
while len(sentence) != 0:
    tmp = sentence[:max_len]
    while tmp not in dictionary and len(tmp) != 1:
        tmp = tmp[: -1]
    words.append(tmp)
    sentence = sentence[len(tmp):]
    print(sentence)

print(words)


# 3、自定义函数

# In[4]:


def fenci(sentence, dic, max_len=5):
    words = []
    while len(sentence) != 0:
        tmp = sentence[:max_len]
        while tmp not in dic and len(tmp) != 1:  # 要注意添加len(tmp) != 1这个添加，不然会陷入死循环，最后一个符号出不来
            tmp = tmp[: -1]      
        words.append(tmp)
        sentence = sentence[len(tmp):]
    print(words)
    
    return words


# In[5]:


fenci(sentence='今天我们学习文本挖掘。', dic=dictionary, max_len=4)


# ## 1.2 最大逆向匹配法

# 读取字典

# In[6]:


with open('../data/字典.txt', encoding='utf-8') as f:
    txt = f.readlines()
dictionary = [i.split()[0] for i in txt]


# 自定义实现

# In[7]:


sentence = '今天我来到北京清华大学。'
max_len = 5

def fenci2(sentence, dic, max_len):
    words = []
    while(len(sentence) != 0):
        tmp = sentence[-max_len: ]
        while tmp not in dic and len(tmp) != 1:
            tmp = tmp[1:]
        words = [tmp] + words
        sentence = sentence[:-len(tmp)]
    
    return words

fenci2(sentence='今天我们学习文本挖掘。', dic=dictionary, max_len=4)


# ## 1.3 隐式马可夫模型HMM

# 数据导入

# In[1]:


p_start = {'good':0.63, 'normal':0.17, 'bad':0.2}
p_emit = {
    'good':{'working':0.05, 'traval':0.35, 'shopping':0.35, 'running':0.25},
    'normal':{'working':0.25, 'traval':0.25, 'shopping':0.25, 'running':0.25},
    'bad':{'working':0.6, 'traval':0.2, 'shopping':0.05, 'running':0.15}
}
p_trans = {
    'good':{'good':0.5, 'normal':0.375, 'bad':0.125},
    'normal':{'good':0.25, 'normal':0.125, 'bad':0.625},
    'bad':{'good':0.25, 'normal':0.375, 'bad':0.375}
}
# 不容易构建、保存，但是索引比较容易


# 假设观察到K连续3天的行为分布是：工作、购物、旅行。那么K三天的心情是什么样子的？

# -- 穷举法

# In[3]:


obs = ['working', 'shopping', 'traval']
states = ['good', 'normal', 'bad']

V = [{}]  # 记录条路径及相应的概率

# 初始化
for y in states:
    V[0][y] = p_start[y] * p_emit[y][obs[0]]
print(V)


for t in range(1, len(obs)): 
    V.append({})
    for y in states:  # t时刻的心情状态
        for i, j in V[-2].items():
            pa = i.split('-')[-1]  # t-1时刻的心情状态
            V[t][i+'-'+y] = j * p_emit[y][obs[t]] * p_trans[pa][y]

print(V[-1])
(prob, path) = max((j, i) for i, j in V[-1].items())
print(f'连续状态为{obs}后，心情可能是：{path}')


# In[10]:


print(tmp)
print(V)


# -- 维特比算法

# In[24]:


# obs = ['working', 'shopping', 'traval']
# states = ['good', 'normal', 'bad']

# V = [{}]
# path = {}

# # 初始化
# for y in states:
#     V[0][y] = p_start[y] * p_emit[y][obs[0]]
#     path[y] = [y]
# print(path)
# print(V)

# # 从第二天开始
# for t in range(1, 3):
#     V.append({})
#     newpath = {}
#     for y in states:
#         em_p = p_emit[y][obs[t]]
#         (prob, state) = max([(V[t - 1][y0] * p_trans[y0][y] * em_p, y0) for y0 in states])
#         V[t][y] = prob
#         newpath[y] = path[state] + [y]
#     print(newpath)
#     path = newpath

# (prob, state) = max((V[len(obs) - 1][y], y) for y in states)  # 确定三条路径的最优解

# print(f'最后一天的心情为：{state}, 概率为：{prob}')
# print(f'连续状态为{obs}后，心情可能是：{path[state]}')


# In[11]:


obs = ['working', 'shopping', 'traval']
states = ['good', 'normal', 'bad']
V = [{}]
path = [{}]

# 初始化
for y in states:
    V[0][y] = p_start[y] * p_emit[y][obs[0]]
    path[0][y] = [y]
    
print('\n', V)
print('\n', path)

for t in range(1, len(obs)):
    V.append({})
    newpath = {}
    for y in states:
        em_p = p_emit[y][obs[t]]
        (prob, state) = max((V[-2][y0]*p_trans[y0][y]*em_p, y0) for y0 in states)
        V[-1][y] = prob
        newpath[y] = path[-1][state] + [y]
    path.append(newpath)
    
print('\n', V)
print('\n', path)

(prob, state) = max((V[-1][y], y) for y in states)  # 确定三条路径的最优解

print(f'\n最后一天的心情为：{state}, 概率为：{prob}')
print(f'\n连续状态为{obs}后，心情可能是：{path[-1][state]}')


# In[12]:


V


# In[13]:


print(path)


# 2、 HMM应用--分词  
# jieba程序的路径：C:\Users\45543\AppData\Local\Continuum\Anaconda3\Lib\site-packages\jieba  
# 中文字符集合：[\u4E00-\u9FD5]

# In[14]:


# 导入父级目录下的Python文件
import sys
sys.path.append(r'C:\Users\45543\Desktop\NLP\data')  # 这种方法属于一次性的，只对当前的python解释器进程有效，关掉python重启后就失效了
from hmm.prob_start import P as start_P
from hmm.prob_trans import P as trans_P
from hmm.prob_emit import P as emit_P


# In[15]:


print(start_P)
print('\n', trans_P)


# In[16]:


obs = sentence = '今天我来到北京清华大学'
states = 'BEMS'

V = [{}]
path = {}

PrevStatus = {
    'B': 'ES',
    'M': 'MB',
    'S': 'SE',
    'E': 'BM'   # t时刻状态:t-1时刻状态
}

for y in states:
    V[0][y] = start_P[y] + emit_P[y][obs[0]]
    path[y] = [y]
print(V, path)

for t in range(1, len(obs)):
    V.append({})
    newpath = {}
    for y in states:
        em_p = emit_P[y][obs[t]]
        
        (prob, state) = max((em_p + V[t-1][y0] + trans_P[y0][y], y0) for y0 in PrevStatus[y])  # y0是上一个状态
        V[t][y] = prob
        newpath[y] = path[state] + [y]
    path = newpath

(prob, state) = max((V[len(obs) - 1][y], y) for y in 'ES')  # 注意'ES'，句子最后一个状态只能是这两种
print(prob, state)
print(path)
pos_list = path[state]

res = []
for i, char in enumerate(obs):    
    sign = pos_list[i]
    if sign == 'B':
        begin = i
    elif sign == 'E':
        res.append(obs[begin: i+1])
    elif sign == 'S':
        res.append(obs[i])
    
print(f'''
{obs}  
标注结果为：
  {path[state]}  
分词结果为：
  {res}
''')


# In[ ]:


pat = path[state]
res = []
for i, (word, char) in enumerate(zip(obs, pat)):
    if char == 'S':
        res.append(word)
    elif char == 'B':
        begin = i
    elif char == 'E':
        res.append(obs[begin:(i+1)])
print(res)


# In[17]:


def viterbi(obs, states, start_P, trans_P, emit_P):
    V = [{}]
    path = {}

    PrevStatus = {
        'B': 'ES',
        'M': 'MB',
        'S': 'SE',
        'E': 'BM'   # t时刻状态:t-1时刻状态
    }

    for y in states:
        V[0][y] = start_P[y] + emit_P[y][obs[0]]
        path[y] = [y]
    print(V, path)

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
        for y in states:
            em_p = emit_P[y][obs[t]]

            (prob, state) = max((em_p + V[t-1][y0] + trans_P[y0][y], y0) for y0 in PrevStatus[y])  # y0是上一个状态
            V[t][y] = prob
            newpath[y] = path[state] + [y]
        path = newpath
    (prob, state) = max((V[len(obs) - 1][y], y) for y in 'ES')
    
    return (prob, path[state])


# In[18]:


viterbi(sentence, 'BMES', start_P, trans_P, emit_P)  # 调用自定义函数


# In[19]:


print(f'step{2:>6}')
print(f'step{200:>6}')


# ## 1.4 jieba分词

# In[20]:


import jieba
print(jieba.lcut('今天我来到北京清华大学'))
print(jieba.lcut_for_search('今天我来到北京清华大学'))


# 对《鹿鼎记》进行分词

# In[21]:


with open('../data/鹿鼎记.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    
txt = txt.split()
print(txt[:7])


# In[22]:


import jieba

# 导入自定义字典
jieba.load_userdict('../data/coal_dict.txt')

words = [jieba.lcut(t) for t in txt]

from tkinter import _flatten
words = list(_flatten(words))


# In[23]:


words[:23]


# In[ ]:




