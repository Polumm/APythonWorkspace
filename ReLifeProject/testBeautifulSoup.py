import requests
from bs4 import BeautifulSoup
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
