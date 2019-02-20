import sys
from courseSelSys.conf import config
from courseSelSys.core.manager import Manager

def login():
    '''
    登录函数，应该先到conf.config文件中读取userinfo的文件路径
    读取userinfo文件中的信息，对用户名和密码进行检查，
    登录成功之后，查看这个人的身份，来确定进入哪一个视图
    
    :return: 
    '''
    usr = input("请输入账号：")
    pwd = input("请输入密码：")
    userinfo_path = config.userinfo
    with open(userinfo_path, encoding = 'utf-8') as f:
        for line in f:
            username,passwd,role = line.strip().split('|')
            if username == usr and passwd == pwd:
                print('\033[1;32m登录成功!\033[0m')
                return {'username':usr, 'role':role}
            else:
                print('\033[1;31m登录失败！\033[0m')

def main():
    '''
    打印欢迎信息
    调用login:得到返回值：用户的姓名和身份(三次登录)
    打印用户身份对应的功能菜单
    如果用户想要调用任何方法应该通过角色对象调用，跳转到对应对象的方法里
    
    :return: 
    '''
    print("\033[1;42m欢迎进入选课系统！\033[0m")
    ret = login()
    if ret:
        role_class = getattr(sys.modules[__name__],ret['role'])#得到与role相同的类
        obj = role_class(ret['username'])#实例化对象
        while True:
            for i,j in enumerate(role_class.menu,1):
                print(i,j[0])
            try:
                ret = int(input("请输入操作序号："))
                getattr(obj,role_class.menu[ret-1][1])()
            except:
                print('对不起，您输入的内容有误！')