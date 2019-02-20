from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))

class Classes:
    def __init__(self,school, name, course, student_path):
        self.school = school#学校,属于哪个学校（北京或者上海分校）
        self.name = name#班级名称
        self.course = course#班级科目
        self.student_path = student_path#学生信息文件的路径

class Course:
    def __init__(self, name, period, price,school):
        self.name = name
        self.period = period
        self.price = price
        self.school = school
    def __repr__(self):
        return self.name

class School:
    def __init__(self,name,course):
        self.name = name
        self.course = course

if __name__ == '__main__':
    from courseSelSys.conf.config import school_info
    from courseSelSys.core.my_pickle import MyPickle
    school_pickle = MyPickle(school_info)
    python = Course('python','6 months',19800,'北京校区')
    linux = Course('linux','5 months',12800,'北京校区')
    go = Course('go','4 months',9800,'上海校区')
    beijing = School('北京校区',[linux,python])
    shanghai = School('上海校区',[go])
    school_pickle.dump(beijing)
    school_pickle.dump(shanghai)

    from courseSelSys.conf.config import course_obj
    course_pickle = MyPickle(course_obj)
    course_pickle.dump(python)
    course_pickle.dump(linux)
    course_pickle.dump(go)