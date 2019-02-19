class Classes:
    def __init__(self,school, name, subject):
        self.school = school#学校,属于哪个学校（北京或者上海分校）
        self.name = name#班级名称
        self.subject = subject#班级科目
        self.student = []#所有学生的对象

class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

class Teacher:
    def __init__(self,name,classes,courses):
        self.name = name
        self.classes = []#一个老师带的所有班级的对象
        self.course = courses#一个老师上得科目的对象
