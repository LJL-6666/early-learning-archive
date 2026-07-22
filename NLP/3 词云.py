#!/usr/bin/env python
# coding: utf-8

# 1、练习：《Walden》小说词云绘制

# In[4]:


with open(r'..\data\Walden.txt', 'r') as f:
    txt = f.read()
print(txt[:55])


# In[7]:


txt = txt.lower()
print(txt[:55])

import re
txt = re.sub('[.,?!:;]', '', txt)
print(txt[:55])

all_words = txt.split()


# In[10]:


import pandas as pd
cipin = pd.Series(all_words).value_counts()
print(cipin.head(20))


# In[15]:


from imageio import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud

pic = imread('../data/aixin.jpg')
wc = WordCloud(background_color='white', font_path=r'C:\Windows\Fonts\JOKERMAN.ttf', mask=pic)
wc.fit_words(cipin)

plt.figure(figsize=(9, 9))
plt.imshow(wc)
plt.axis('off')
plt.show()


# 2、练习：绘制《鹿鼎记》的词云

# In[18]:


with open('../data/鹿鼎记.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

print(txt[:25])


# In[20]:


import re
txt = re.sub(' |\ufeff', '', txt)


# In[23]:


import jieba
jieba.load_userdict('../data/coal_dict.txt')
all_words = jieba.lcut(txt)
print(all_words[:25])


# In[40]:


with open('../data/stoplist.txt', 'r', encoding = 'utf-8') as f:
    stop = f.read()
stop = stop.split()
stop = stop + ['\n', '道', '说', '说道', '听', '笑', '做']
print(stop)


# In[41]:


new_words = [i for i in all_words if i not in stop]


# In[42]:


print(new_words[:5])


# In[43]:


import pandas as pd
cipin = pd.Series(new_words).value_counts()
cipin.head(23)


# In[44]:


from imageio import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud

pic = imread('../data/aixin.jpg')
wc = WordCloud(background_color='white', font_path=r'C:\Windows\Fonts\SIMYOU.ttf', mask=pic)
wc.fit_words(cipin)

plt.figure(figsize=(9, 9))
plt.imshow(wc)
plt.axis('off')
plt.show()


# In[ ]:




