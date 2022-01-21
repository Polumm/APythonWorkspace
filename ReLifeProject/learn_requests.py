# 导入模块
import requests
# 定义请求地址
url = 'http://grzy.cug.edu.cn/'
# 定义自定义请求头
headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
# url + 请求头 发送get请求
response = requests.get(url,headers=headers)
# 获取响应的 html 内容
html = response.content.decode('utf-8')
print(html)