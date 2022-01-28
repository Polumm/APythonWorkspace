import requests
from bs4 import BeautifulSoup
import csv
url = 'http://grzy.cug.edu.cn/taomh/zh_CN'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
response = requests.get(url, headers)
text = response.content.decode('utf-8')
soup = BeautifulSoup(text, 'lxml')
a = soup.find_all('div', attrs={'class': 'jbqk'}) # 找到“jbqk”标签下的内容，email从这里就抓不到了，怎么回事
# print(a)  # 监视a
b = []  # 存放'jbqk'标签下的p标签
info = [] # 存放个人详细信息
for i in a: # 找p标签
  b = i.find_all("p")
for j in range(len(b)): # 标签内的内容转文本
  # print(b[j].text)
  info.append(b[j].text)
print(info)

info2 = []
column = []
content = []
for i in range(len(info)):
  if i == 0:
    continue
  content.append(info[i].split('：')[1])
info2.append((content))  # append方法为数组添加元素
tuple(info2[0])
print(info2)

def save(content):
  '''
  本地存储信息
  :param content:
  :return:
  '''

  # 创建文件流
  f = open("TeachersInfo.csv", 'w', encoding='GBK', newline='')   # 使用csv模块读写CSV文件时候，需要设置newline=''

  # 创建csv写入文件
  writer = csv.writer(f)

  # 先写一行，写入标题栏
  writer.writerow(('曾获荣誉', '性别', '毕业院校', '学历', '学位', '在职信息', '所在单位', '学科', '联系方式'))

  # 再迭代writerow，逐行写入
  for row in content:
    writer.writerow(row)

  # 关闭文件
  f.close()
  print("写入完毕！！！")


save(info2)
# print(soup.prettify())
# print(soup.find('head'))  # 使用xml解析方法select, find同样可以解析html
# print(soup.find_all(class_ = 'con_bload'))
# a = soup.find_all(class_ = 'con_bload')
# for j in a:
#   b = j.find(class_ = '联系方式')
#   print(b)
# print(type(a))

# print(soup.a.attrs)  # 获取a标签属性字典
# print(soup.a['href'])  # 获取a标签url

# 待：可遍历字符串与注释的区分
