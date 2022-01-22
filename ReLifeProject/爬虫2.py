# -*- coding:utf-8 -*-
"""
@文件名:爬虫
@Author: 宗闯
@Time: 2022/1/11 20:04
感谢学长的帮助！
"""
import requests as rq
import re


def request(name, headers):
    """
    请求函数
    :param name: 姓名（拼音）
    :param headers: 请求头
    :return:
    """

    url = 'http://grzy.cug.edu.cn/{0}/'.format(name)
    response = rq.get(url, headers=headers)
    text = response.content.decode('utf-8')
    return text


def analysis(text):
    """
    信息解析提取（正则）
    :param text: 返回的文本信息
    :return:
    """

    pattern = re.compile('"jbqk".*?<p>(.*?)</p>.*?主要任职：(.*?)</p>.*?性别：(.*?)</p>.*?毕业院校：(.*?)</p>', re.S)
    results = re.findall(pattern, text)
    return results


if __name__ == "__main__":
    name = 'wanglunche'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    text = request('wanglunche', headers=headers)
    results = analysis(text)

    print(results)