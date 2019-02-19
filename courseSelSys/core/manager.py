from conf.config import *
from core.teacher import Teacher
from core.my_pickle import MyPickle
#管理员类
class Manager:

    #menu即为视图
    menu = [('创建讲师账号','createTeacher'),('创建学生账号','createStudent'),
            ('创建课程','createCourse'),('查看课程','showCourse'),
            ('创建班级','createClasses'),('查看班级','showClasses'),
            ('绑定班级','boundClass'),('退出','')]

    def __init__(self,name):
        self.name = name
        self.teacher_pickle_obj = MyPickle(teacher_obj)

    @staticmethod
    def userinfo_handle(content):
        with open(userinfo,'a') as f:
            f.write('\n%s' %content)

    def createTeacher(self):
        #输入讲师的姓名
        #输入讲师的密码
        #将讲师的信息写入userinfo文件
        #输入：
            #讲师所在的学校
        #实例化一个讲师对象，存储在讲师对应的文件中
        print(' in createTeacher function')
        teacher_name = input("请输入要创建的讲师姓名：")
        teacher_passwd = input("请输入要创建的讲师密码：")
        school = input("学校：")
        content = '%s|%s|Teacher'%teacher_name,teacher_passwd
        Manager.userinfo_handle(content)
        teacher = Teacher(teacher_name,school)
        self.teacher_pickle_obj.dump(teacher)

    def createStudent(self):
        #输入学生的姓名
        #输入学生的密码
        #将学生的信息写入userinfo文件
        print(' in createStudent function')
    def createCourse(self):
        #输入：学科名称，价格，周期
        #创建一个课程对象，dump进course文件
        print(' in createCourse function')
    def showCourse(self):
        #打开文件
        #将文件中的学科对象读出来并展示
        print(' in showCourse function')
    def createClasses(self):
        #输入：
            #班级名称、学校
            #绑定一个学科对象，要先调用查看学科方法获取学科对象，用户选择学科，再讲对象绑定到班级
            #创建一个属于这个班级的文件用于存储学生信息，将文件的路径存储到班级对象中
            #创建一个班级对象（名称、学校、学科对象、讲师空列表、学生信息所在文件的路径），dump进classes文件
        print(' in createClasses function')
    def showClasses(self):
        #打开文件
        #将文件中的班级对象读出来并展示
        print(' in showClasses function')
    def boundClass(self):
        #管理员选择为老师还是学生指定班级
        #如果是为老师绑定班级：
            #找到指定的老师和对应的班级（都是通过show方法查看后选择）
            #给讲师对象的班级属性的列表中加入一个新的项，值为班级的对象
            #给班级对象中的讲师属性列表加入一个新的项，值为讲师的对象
        #如果为学生绑定班级
            #找到指定的学生和对应的班级（都是通过show方法查看之后选择）
            #给学生创建新的班级属性，将属性的值设置为班级对象
            #将学生对象的信息根据班级对象中存储的学生信息存储路径 dump入对应文件
        print(' in boundClass function')

#首先 以管理员的身份登录
#登录之后 就应该实例化一个对应身份的对象
#管理员对象可以调用所有的方法