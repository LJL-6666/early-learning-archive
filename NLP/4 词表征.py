#!/usr/bin/env python
# coding: utf-8

# # Word2Vec

# In[1]:


corpus = ["and the cute kitten purred and then",
          "the cute furry cat purred and miaowed",
          "that the small kitten miaowed and she",
          "the loud furry dog bowwowed and bit"]


# In[2]:


cor = {'cat':['cute', 'furry', 'purred', 'miaowed'],
       'kitten':['cute', 'purred', 'small', 'miaowed'],
       'dog':['bowwowed', 'furry', 'loud', 'ran', 'bit']}


# ## word-count Word2vec

# In[3]:


words = ['cute', 'furry', 'purred', 'miaowed', 'cute', 'purred', 'small', 'miaowed', 'bowwowed', 'furry', 'loud', 'ran', 'bit']
dic = {word:i for i, word in enumerate(words)}


# In[4]:


import pandas as pd
data = pd.DataFrame([], index=cor.keys(), columns=words)
data = data.fillna(0)
data


# In[5]:


for i in cor.keys():
    data.loc[i, cor[i]] = 1


# In[6]:


data


# In[7]:


import numpy as np
def similar(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.sum(x*y)/ (np.sqrt(sum((x**2))) * np.sqrt(sum((y**2))))


# In[8]:


print(f'{data.index[0]}和{data.index[1]}的相似度为：{similar(data.iloc[0,:], data.iloc[1, :])}')
print(f'{data.index[0]}和{data.index[2]}的相似度为：{similar(data.iloc[0,:], data.iloc[2, :])}')
print(f'{data.index[2]}和{data.index[1]}的相似度为：{similar(data.iloc[2,:], data.iloc[1, :])}')


# ## word2vec: CBOW

# In[9]:


words = ['cute', 'furry', 'purred', 'miaowed', 'cute', 'purred', 'small', 'bowwowed', 'furry', 'loud', 'ran', 'bit', 'cat',
         'kitten', 'dog']
dic = {word:i for i, word in enumerate(words)}


# In[10]:


onehot = np.diag([1]*len(words))
mat = pd.DataFrame(onehot, columns=words, index=words)
mat


# In[11]:


x = mat.loc[['dog', 'cat', 'kitten'], :]
x


# In[12]:


y = pd.DataFrame(index=mat.index)
for w in ['dog', 'cat', 'kitten']:
    a = mat.loc[cor[w], :].sum(axis=0)
    y = pd.concat([y, a], axis=1)
y = y.T
print(y)


# In[13]:


import numpy as np
x_data = np.array(x, dtype=np.float32)
y_data = np.array(y, dtype=np.float32)
print(x_data, '\n', y_data)


# In[14]:


import tensorflow as tf

input_size = len(mat)
output_size = len(mat)
hidden_size = 5
learning_rate = 0.001

x = tf.placeholder(tf.float32, [None, input_size])
y = tf.placeholder(tf.float32, [None, output_size])

w = tf.Variable(tf.zeros([input_size, hidden_size]))
v = tf.Variable(tf.zeros([hidden_size, output_size]))

b1 = tf.Variable(tf.zeros([hidden_size]))
b2 = tf.Variable(tf.zeros([output_size]))

hidden_output = tf.sigmoid(tf.matmul(x, w) + b1)
out = tf.nn.softmax(tf.matmul(hidden_output, v) + b2)

cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(out), axis=1))

train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    
    for i in range(2000):
        sess.run(train_op, feed_dict={x:x_data, y:y_data})
    wc = sess.run(w)


# In[15]:


wc


# In[16]:


wc2 = {}
wc2['cat'] = wc[12]
wc2['kitten'] = wc[13]
wc2['dog'] = wc[14]
wc2


# In[17]:


similar(wc2['cat'], wc2['kitten'])


# In[18]:


print(f"cat和kitten的相似度为：{similar(wc2['cat'], wc2['kitten'])}")
print(f"cat和dog的相似度为：{similar(wc2['cat'], wc2['dog'])}")
print(f"dog和kitten的相似度为：{similar(wc2['dog'], wc2['kitten'])}")


# 相比上面用word-count的方法，CBOW方法得到的结果能够挖掘出dog和kitten之间的关系

# ## FastText

# In[19]:


import fastText
classifier = fastText.train_supervised(r'..\data\train.txt')


# In[20]:


classifier.get_words()


# In[21]:


classifier.get_labels()
classifier.predict(['i hate it', 'i like the baby smell', 'oh, how could it look sooo beautiful.'])


# In[22]:


help(fastText.train_supervised)


# In[ ]:




