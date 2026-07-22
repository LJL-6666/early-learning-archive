#!/usr/bin/env python
# coding: utf-8

# # TF-IDF

# 根据词频提取出《浅谈能源文化》文章的关键字

# In[ ]:


import jieba
import pandas as pd
# 1、读取文章《浅谈能源文化》
with open('../data/浅谈能源文化.txt', 'r') as f:
    txt = f.read()
# 2、分词
txt = txt.split()
words = [jieba.lcut(x) for x in txt]
# 3、去除停用词
with open('../data/stoplist.txt', 'r', encoding='utf-8') as f:
    stop = f.read()
stop = stop.split()
words2 = [[i for i in x if i not in stop] for x in words]
# 4、统计词频
a = [' '.join(x) for x in words2]
b = ' '.join(a)
cipin = pd.Series(b.split()).value_counts()
# 5、提取词频最多的5个词语作为文章的关键字
cipin.index[:5]
key_words = cipin.iloc[:5].index
print(key_words)


# 改进：根据词频-逆文档概率提取《浅谈能源文化》的关键字

# In[ ]:


with open('../data/字典.txt', 'r', encoding='utf-8') as f:
    dic = f.readlines()
print(dic[:4])
dic2 = [i.split()[:2] for i in dic]
print(dic2[:4])
dic3 = {i[0]:i[1] for i in dic2}


# In[ ]:


n = 100000
import math
word3 = []
tf_idf3 = []
tf3 = []
idf3 = []
for (k, w) in zip(cipin[:10], cipin[:10].index):
    tf = k
    idf = math.log(n/(int(dic3.get(w, 0))+1))
    tf_idf = tf*idf
    word3.append(w)
    tf_idf3.append(tf_idf)
    tf3.append(tf)
    idf3.append(idf)
    print(f'词语 {w} 在文章中的词频为{k}, 在语料库中出现的次数为{dic3.get(w, 0)}，tf-idf是{tf_idf}')


# In[ ]:


data = pd.DataFrame({'words':word3, 'tf':tf3, 'idf':idf3, 'tf-idf':tf_idf3})
data.sort_values(by='tf-idf', ascending=False)


# # 文本聚类

# 对手机评论数据进行聚类

# In[ ]:


import pandas as pd
f = open('../data/vivo数据.csv', encoding='utf-8')
data = pd.read_csv(f)
data.head()


# In[ ]:


content = data['content']
content.head()


# 分词

# In[ ]:


import jieba
content = content.apply(jieba.lcut)
content.head()


# 去除停用词

# In[ ]:


with open('../data/stoplist.txt', 'r', encoding='utf-8') as f:
    stop = f.read()
stop = stop.split()
content = content.apply(lambda x: [i for i in x if i not in stop])
content.head()


# 转换为文本-词条矩阵

# In[ ]:


x = content.apply(lambda x: ' '.join(x))
y = data['lab']
print(x.head(), y.head())


# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x_data = cv.fit_transform(x)
cv.vocabulary_  # 字典
cv.get_feature_names()  # 词条
x_data.toarray()


# 使用KMeans聚类

# In[ ]:


from sklearn.cluster import KMeans
model = KMeans(n_clusters=5).fit(x_data)
model.labels_


# In[ ]:


y_pre = model.labels_


# 评价聚类效果

# In[ ]:


from sklearn.metrics import silhouette_score
# help(silhouette_score)
silhouette_score(x_data, y_pre)


# In[ ]:


for i in range(3, 9):
    model = KMeans(n_clusters=i).fit(x_data)
    y_pre = model.labels_
    print(f'{i} {silhouette_score(x_data, y_pre)}')


# # 情感分析

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 文本分类

# In[22]:


import pandas as pd
f = open('../data/vivo数据.csv', encoding='utf-8')
data = pd.read_csv(f)
data.head()


# In[23]:


content = data['content']
content.head()


# In[24]:


import jieba
content = content.apply(jieba.lcut)
content.head()


# In[25]:


with open('../data/stoplist.txt', 'r', encoding='utf-8') as f:
    stop = f.read()
stop = stop.split()
stop = stop + ['\n', ' ']
content = content.apply(lambda x: [i for i in x if i not in stop])
content.head()


# In[26]:


x = content.apply(lambda x: ' '.join(x))
y = data['lab']
print(x.head(11), y.head())


# In[27]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x_data = cv.fit_transform(x)
cv.vocabulary_  # 字典
cv.get_feature_names()  # 词条
x_data.toarray()


# In[28]:


from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data.toarray(), y, test_size=0.2, random_state=123)
model = GaussianNB().fit(x_train, y_train)
y_pre = model.predict(x_test)


# In[29]:


from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test, y_pre))
print(classification_report(y_test, y_pre))


# # 使用FastText分类

# In[69]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=123)


# In[70]:


with open('../tmp/train.txt', 'w', encoding='utf-8') as f:
    for i in x_train.index:
        f.write(x_train[i]+ ' __label__' + str(y_train[i]) +'\n')


# In[71]:


import fastText
classifier = fastText.train_supervised(r'..\tmp\train.txt')


# In[72]:


classifier.get_words()[:12]


# In[73]:


classifier.get_labels()[:12]


# In[74]:


y_pre = classifier.predict(list(x_test))
y_pre = [int(x[-1]) for x in y_pre[0]]


# In[75]:


from sklearn.metrics import confusion_matrix, classification_report
y_test = list(y_test)
print(confusion_matrix(y_test, y_pre))
print(classification_report(y_test, y_pre))


# In[ ]:




