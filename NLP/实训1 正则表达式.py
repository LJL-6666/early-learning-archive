import re
string = 'The small cake smell good. But it is too small.'
print(re.match(pattern='small', string=string))  # 从第一个字母开始
print(re.match(pattern='The small', string=string))  # 从第一个字母开始
print(re.search(pattern='small', string=string))  # 查找一个
print(re.findall(pattern='small', string=string))  # 查找所有


import re
string = 'The small cake smell good. But it is too small.'
print(re.sub(pattern='small', repl='big', string=string))  # 替换


string = 'small smell sm.ll smll smaall sm3ll smAll smaaaall'
print(re.findall('small', string))  # 匹配small
print(re.findall('small|smell', string))  # 匹配small或者smell
print(re.findall('sm.ll', string))  # .表示任意一个字符
print(re.findall('sm[aesd]ll', string))  # []里的字符可以被匹配一次
print(re.findall('sm[a-z]ll', string))  # [a-z]所有小写字母可以被匹配一次
print(re.findall('sm[a-zA-Z0-9]ll', string))  # [a-zA-Z0-9]所有大小写字母和数字可以被匹配一次
print(re.findall('sm\.ll', string))  # 匹配.本身需要转义



# 量化符号
string = 'small smell sm.ll smll smaall sm3ll smAll smaaaall'
print(re.findall('sm[a-z]{1,2}ll', string))  # {1,2}表示前面的元素匹配一次或者两次
print(re.findall('sm[a-z]{2}ll', string))  # {2}表示前面的元素匹配两次
print(re.findall('sm[a-z]{2,}ll', string))  # {2}表示前面的元素匹配两次以上(贪婪)
print(re.findall('sm[a-z]?ll', string))  # 前面的内容匹配0次或1次，同{0,1}
print(re.findall('sm[a-z]+ll', string))  # 前面的内容匹配1次或以上，同{1,}
print(re.findall('sm[a-z]*ll', string))  # 前面的内容匹配0次或以上，同{0,}




rawdata = '555-1239Moe Szyslak(636) 555-0113Burns, C.Montgomery555-6542Rev. Timothy Lovejoy555 8904Ned Flanders636-555-3226Simpson,Homer5553642Dr. Julius Hibbert'
tel = re.findall('\(?[0-9]{0,3}\)?[ -]?[0-9]{3}[ -]?[0-9]{4}', rawdata)
name = re.findall('[A-Z][a-zA-Z ,.]+', rawdata)
import pandas as pd
pd.DataFrame({'name': name, 'Tel': tel})


