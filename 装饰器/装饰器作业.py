#1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
#要求登录成功一次，后续的函数都无需再输入用户名和密码
# FLAG = False
# def login(func):
#     def inner(*args, **kwargs):
#         global FLAG
#         '''登录程序'''
#         if FLAG == False:
#             username = input('账号：')
#             password = input('密码：')
#             if username == 'boss_gold' and password == '22222':
#                 FLAG = True
#                 ret = func(*args, **kwargs)     #func是被装饰的函数
#                 return ret
#             else:
#                 print('登录失败')
#         else:
#             ret = func(*args, **kwargs)  # func是被装饰的函数
#             return ret
#     return inner
#
# @login
# def shoplist_add():
#     print('增加一件物品')
# @login
# def shoplist_del():
#     print('删除一件物品')
#
# shoplist_add()
# shoplist_del()

#2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数
#都将被调用的函数名称写入文件
# def log(func):
#     def inner(*args, **kwargs):
#         with open('log', 'a', encoding='utf-8') as f:
#             f.write(func.__name__ + '\n')
#         ret = func(*args, **kwargs)
#         return ret
#     return inner
#
# @log
# def shoplist_add():
#     print('增加一件物品')
# @log
# def shoplist_del():
#     print('删除一件物品')
# shoplist_add()
# shoplist_del()

#3.编写下载网页内容的作业，要求功能是：用户传入一个url，函数返回下载页面的结果


#4.为题目1编写装饰器，实现缓存网页内容的功能：
#具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），
#就优先从文件中读取网页内容，否则，就去下载
import os
from urllib.request import urlopen
def cache(func):
    def inner(*args, **kwargs):
        '''判断文件是否有内容'''
        if os.path.getsize('web_cache'):
            with open('web_cache', 'rb') as f:
                return f.read()
        ret = func(*args, **kwargs)#请求网页的函数
        #将请求的结果写到文件里
        with open('web_cache', 'wb') as f:
            f.write(b'*********'+ret)
        return ret
    return inner

@cache
def get(url):
    code = urlopen(url).read()
    return code

ret = get('http://www.baidu.com')
print(ret)
ret = get('http://www.baidu.com')
print(ret)
ret = get('http://www.baidu.com')
print(ret)