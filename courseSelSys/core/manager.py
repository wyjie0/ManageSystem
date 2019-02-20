from os import path
from courseSelSys.conf.config import *
from courseSelSys.core.school import *
from courseSelSys.core.teacher import Teacher
from courseSelSys.core.student import Student
from courseSelSys.core.my_pickle import MyPickle
#管理员类
# from conf.config import teacher_obj, course_obj, school_info, classes_obj


class Manager:

    #menu即为视图
    menu = [('创建讲师账号','createTeacher'),('创建学生账号','createStudent'),
            ('查看学校','showSchool'),('查看讲师','showTeacher'),
            ('查看课程','showCourse'),
            ('创建班级','createClasses'),('查看班级','showClasses'),
            ('为班级指定老师','boundClassTeacher'),('退出','exit')]

    def __init__(self,name):
        self.name = name
        self.teacher_pickle_obj = MyPickle(teacher_obj)
        self.course_pickle_obj = MyPickle(course_obj)
        self.school_pickle_obj = MyPickle(school_info)
        self.class_pickle_obj = MyPickle(classes_obj)

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
        self.showSchool()
        school = input("学校：")
        content = '%s|%s|Teacher'%teacher_name,teacher_passwd
        Manager.userinfo_handle(content)
        teacher = Teacher(teacher_name,school)
        self.teacher_pickle_obj.dump(teacher)
        print('创建成功!')

    def createStudent(self):
        #输入学生的姓名
        #输入学生的密码
        #将学生的信息写入userinfo文件
        print(' in createStudent function')
        student_name = input('请输入学生的姓名：')
        student_pwd = input('请输入学生的密码：')
        self.showSchool()
        student_school = input('请输入学生所在的学校：')
        self.showClasses()
        student_class = input('请输入学生所在的班级：')
        class_g = self.class_pickle_obj.loaditer()
        for clas in class_g:
            if clas.name == student_class:
                content = '%s|%s|Student' %(student_name, student_pwd)
                Manager.userinfo_handle(content)
                stu_obj = Student(student_name, student_school, clas)
                MyPickle(clas.student_path).dump(stu_obj)
                print('创建成功!')
            else:
                print('您输入的内容有误，创建学生失败')
    # def createCourse(self):
    #     #输入：学科名称，价格，周期
    #     #创建一个课程对象，dump进course文件
    #     print(' in createCourse function')

    def createClasses(self):
        # 输入：
        # 班级名称、学校
        # 绑定一个学科对象，要先调用查看学科方法获取学科对象，用户选择学科，再讲对象绑定到班级
        # 创建一个属于这个班级的文件用于存储学生信息，将文件的路径存储到班级对象中
        # 创建一个班级对象（名称、学校、学科对象、讲师空列表、学生信息所在文件的路径），dump进classes文件
        print(' in createClasses function')
        class_name = input('请输入班级的名称：')
        self.showSchool()
        school_name = input('请输入学校的名称：')
        self.showCourse()
        course = input('请输入学科的名称：')
        student_path = path.join(student_info,class_name)
        open(student_path,'w').close()
        class_obj = Classes(school_name,class_name,course,student_path)
        self.class_pickle_obj.dump(class_obj)

    def show(self,pickle_obj):
        pickle_obj = getattr(self,pickle_obj)
        load_g = pickle_obj.loaditer()
        for course_obj in load_g:
            for i in course_obj.__dict__.keys():
                print(i, course_obj.__dict__[i])
            print('-' * 50)


    def showCourse(self):
        self.show('course_pickle_obj')

    def showSchool(self):
        self.show('school_pickle_obj')

    def showClasses(self):
        self.show('class_pickle_obj')

    def showTeacher(self):
        self.show('teacher_pickle_obj')

    def boundClassTeacher(self):
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
        self.showClasses()
        class_name = input('请输入要指定的班级：')
        self.showTeacher()
        teacher_name = input('请输入要制定的讲师：')
        teach_g = self.teacher_pickle_obj.loaditer()
        for teacher_obj in teach_g:
            if teacher_obj.name == teacher_name:
                teacher_obj.classes.append(class_name)
                self.teacher_pickle_obj.edit(teacher_obj)
                print('创建成功!')
                return
#首先 以管理员的身份登录
#登录之后 就应该实例化一个对应身份的对象
#管理员对象可以调用所有的方法