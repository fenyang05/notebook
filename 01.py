'''
定义一个学生类，用来描述学生
'''
# 定义一个空类
class Student():
    pass
# 定义一个对象
mingyue = Student()

class PythonStudent():
    # 用None给不确定的变量赋值
    name = "yueyue"
    age = 18
    course = "python"

    def DoHomework(self):
        '''
        这是文件说明
        :return: none
        '''
        print("I working")
        return None

s = PythonStudent()
print("I am {:m<15},I am {} yearold".format(s.name,s.age))
print(s.__dict__)
print(PythonStudent.__dict__)
help(s)
help(PythonStudent)
print("hello word")