import os
os.chdir('/course/文本挖掘实战')
with open('./data/字典.txt', 'r', encoding='utf-8') as f:
    my_dict = f.readlines()
my_dict = [i.split()[0] for i in my_dict]
my_dict[:5]

sentence = '今天我来到北京清华大学'
max_len = 5

words = []
while len(sentence) != 0:
    tmp = sentence[:max_len]
    while tmp not in my_dict and len(tmp) > 1:
        tmp = tmp[:-1]
    words.append(tmp)
    sentence = sentence[len(tmp):]
    
print(words)



import os
os.chdir('/course/文本挖掘实战')
with open('../data/字典.txt', 'r', encoding='utf-8') as f:
    my_dict = f.readlines()
my_dict = [i.split()[0] for i in my_dict]
my_dict[:5]

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