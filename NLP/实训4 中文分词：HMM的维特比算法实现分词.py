import sys
import os
os.chdir('/course/文本挖掘实战')
sys.path.append(r'..\data')
from hmm.prob_start import P as p_start
from hmm.prob_trans import P as p_trans
from hmm.prob_emit import P as p_emit



obs = '今天我来到北京清华大学'
states = list('BMES')

V = [{}]
path = [{}]

# t时刻状态：t-1时刻可能的状态
prevStates = {'M': list('MB'),
              'B': list('ES'),
              'S': list('SE'),
              'E': list('BM')}


# 初始化
for y in states:
    V[0][y] = p_start[y] + p_emit[y][obs[0]]
    path[0][y] = [y]
print(V, '\n', path)    

for t in range(1, len(obs)):
    V.append({})
    path.append({})
    for y in states:
        emit_p = p_emit[y][obs[t]]
        (prob, state) = max((V[t-1][y0] + p_trans[y0][y] + emit_p, y0) for y0 in prevStates[y])
        V[t][y] = prob
        path[t][y] = path[t-1][state] + [y]
(prob, last_state) = max((V[-1][y], y) for y in list('ES'))
sentence_label = path[-1][last_state]

words = []
for i, char in enumerate(obs):
    sign = sentence_label[i]
    if sign == 'B':
        begin = i
    elif sign == 'E':
        words.append(obs[begin: i+1])
    elif sign == 'S':
        words.append(obs[i])

print(f'\n"{obs}"的标注为：\n{sentence_label}\n分词结果为：\n{words}')




import jieba
obs = '今天我来到北京清华大学'
print(jieba.lcut(obs))
print(jieba.lcut_for_search(obs))

sentence = '广州泰迪智能科技有限公司欢迎您！'
print(jieba.lcut(sentence))
jieba.add_word('广州泰迪智能科技有限公司')
print(jieba.lcut(sentence))