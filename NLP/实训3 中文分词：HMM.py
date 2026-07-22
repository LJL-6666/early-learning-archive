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




obs = ['working', 'shopping', 'travel']
states = ['good', 'normal', 'bad']
V = [{}]
path = [{}]

# 初始化
for y in states:
    V[0][y] = p_start[y] * p_emit[y][obs[0]]
    path[0][y] = [y]

for t in range(1, len(obs)):
    V.append({})
    path.append({})
    for y in states:
        em_p = p_emit[y][obs[t]]
        (prob, state) = max((V[t-1][y0]*p_trans[y0][y]*em_p, y0) for y0 in states)
        V[t][y] = prob
        path[t][y] = path[t-1][state] + [y]
(prob, last_state) = max(((j, i) for i, j in V[-1].items()))

print(f'观察状态连续为{obs}, 心情可能是{path[-1][last_state]}, 概率为{prob}')