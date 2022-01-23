# 导入模块
import requests
import re
import csv


def request2():
  '''
  爬取老师姓名
  :return:
  '''
  url = 'https://xgxy.cug.edu.cn/yjspy/dsjj1.htm'
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
  }

  response = requests.get(url, headers=headers, verify=False)
  text = response.content.decode('utf-8')
  return text


def analysis2(text):
  """
  信息解析提取（正则）
  :param text: utf-8编码的html页面字符串
  :return: 所有教师姓名拼音缩写的数组
  """

  pattern = re.compile('<div class="media-caption">.*?href="(.*?)">(.*?)</a></h2>', re.S) # 一组url 二组姓名
  results = re.findall(pattern, text)

  teacherNames = []

  for i in results:
    name = i[0].split('/')[3]   # 利用split方法解析url，[3]即为拼音缩写
    print(name)
    teacherNames.append((i[0], i[1], name)) # append方法为数组添加元素

  return teacherNames

def save(content):
  '''
  本地存储信息
  :param content:
  :return:
  '''

  # 创建文件流
  f = open("Teachers.csv", 'w', encoding='GBK', newline='')   # 使用csv模块读写CSV文件时候，需要设置newline=''

  # 创建csv写入文件
  writer = csv.writer(f)

  # 先写一行，写入标题栏
  writer.writerow(('链接', '姓名拼写', '姓名'))

  # 再迭代writerow，逐行写入
  for row in content:
    writer.writerow(row)

  # 关闭文件
  f.close()
  print("写入完毕！！！")


text = request2();
results = analysis2(text)
save(results)
