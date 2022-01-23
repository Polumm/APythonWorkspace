""""
Author : Polumm
Version: 0.1
"""

# 变量及输出
print("hello world!")
a = 100
b = 12.345
print(a + b)
# a = input("a = ")
print(a)

# 条件循环语句
results = 59
if results >= 60:
    print("及格")
else:   # 注意Python严格缩进
    print("不及格")

test = 0
if test:
    print("1")
    # test = 1
test = 1    # 注意：这里没有花括号，严格按照缩进体现代码块
if test:    # 非零非空可以像C++一样，直接代表true，但是没有(！变量)这样的写法
    print("1")

# 多分支条件
results = 89
if results > 90:
    print("优秀")
elif results > 80:
    print("良好")
elif results > 60:
    print("及格")
else:
    print("不及格")


