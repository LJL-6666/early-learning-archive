#!/usr/bin/env python
# coding: utf-8

# In[12]:


import re
a = 'Which chars do you want? small smell smll sm.ll sm?ll smsmll smsmllll sm3ll sm-ll'


# In[13]:


print(re.match('Which', a))
print(re.match('small', a))
print(re.search('small', a))
print(re.findall('small', a))
print(re.sub('small', 'big', a))

b = 'small smell smll smsmll sm3ll sm.ll sm-ll'
# 通配符号
print(re.findall('sm.ll', a))
print(re.findall('sm[asdfghjklpoiuytrewqzxcvbnm]ll', a))
print(re.findall('sm[a-zA-Z0-9]ll', a))
print(re.findall('sm\.ll', a),re.findall('sm[.\- ]ll', a))
print(re.findall('sm\\wll', a), re.findall('^sm.ll', a))
print(re.findall('sm.ll$', a), re.findall('sm[^a-z]ll', a))
# 量化符号
print(re.findall('sm.{2}ll', a))
print(re.findall('sm.{1,2}ll', a))
print(re.findall('sm.{,2}ll', a))
print(re.findall('sm.?ll', a)) # {0,1}
print(re.findall('sm.*ll', a))  # {0,}
print(re.findall('sm[a-z]*ll', a))  # {0,}
print(re.findall('sm[a-z]+ll', a))  # {1,}


# 练习

# In[15]:


rawdata = '555-1239Moe Szyslak(636) 555-0113Burns, C.Montgomery555-6542Rev. Timothy Lovejoy555 8904Ned Flanders636-555-3226Simpson,Homer5553642Dr. Julius Hibbert'
peo = re.findall('[A-Za-z., ]{2,}', rawdata)
# re.findall('[A-Z][A-Za-z., ]+', rawdata)
tel = re.findall('[0-9(][0-9)\- ]+', rawdata)
re.findall('[0-9(][^A-Z]+', rawdata)
re.findall('\(?[0-9]{0,3}\)?[ \-]?[0-9]{3}[\- ]?[0-9]{4}', rawdata)
import pandas as pd
data = pd.DataFrame({'telphone':tel, 'user': peo})
print(data)
data.to_csv('../tmp/temp.csv')


# 1、找出以下信息中的电话号码。

# In[6]:


rd = '李磊: 248-555-1234；韩梅梅: (313) 555-1234  迪丽热巴: (810)555-1234阿里巴巴: 734.555.9999'

print(re.findall('[^0-9 ；()\-:]{2,}', rd))
print(re.findall('[\u4E00-\u9FD5]+', rd))

print(re.findall('[0-9(][0-9\- ).]+', rd))


# 2、将句子中年份的大写数字改为阿拉伯数字

# In[4]:


import re
m0 = "在一九四九年新中国成立"
m1 = "比一九九零年低百分之五点二"
m2 = '人一九九六年击败俄军,取得实质独立'
data = [m0, m1, m2]
a = list('一二三四五六七八九零')
b = list('1234567890')
my_dict = dict(zip(a, b))
data2 = []
for m in data:
    tem = re.findall('(.{4})年', m)
    c = ''.join([my_dict[i] for i in list(tem[0])])
    data2.append(re.sub('(.{4})年', c + '年', m))
print(data2)


# In[30]:


text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""


# In[31]:


entries = re.split("\n+", text)
entries


# In[32]:


[re.split(":? ", entry, 3) for entry in entries]


# In[33]:


[re.split(":? ", entry, 4) for entry in entries]


# In[34]:


help(re.split)


# 3、豆瓣评论提取

# In[19]:


with open(r'C:\Users\45543\Desktop\NLP\data\豆瓣\明星大侦探 第四季的剧评 (321).html', 'r', encoding='utf-8') as f:
    txt = f.read()


# In[20]:


print(txt)


# In[48]:


import re
txt2 = txt.split('\n')
ind = [i for i, x in enumerate(txt2) if re.findall('review-content clearfix', x) !=[]]


# In[66]:


import pandas as pd
doc = pd.Series([txt2[i+1] for i in ind])
doc


# In[67]:


doc = doc.apply(lambda x: re.sub('<[^>]+>', '', x))


# In[73]:


nam = [re.findall('data-author="(.+)" data-url', txt2[i])[0] for i in ind]


# In[74]:


data = pd.DataFrame({'name': nam, 'message':doc})
data.to_csv('../tmp/dp.csv')


# In[75]:


data


# In[ ]:




