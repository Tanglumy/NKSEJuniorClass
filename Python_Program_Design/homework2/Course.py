"""
课程
属性：      课程序号、课程名、课程当前人数、开课老师、课程最大选课人数（实例属性），维护一个所有课程的列表（类属性且不能被外部访问）
功能：      查看当前课程人数与最大选课人数（实例方法）
                查看当前课程开课老师（实例方法）
无论老师还是学生都可以查看指定序号的课程的所有信息（课程序号、课程当前人数、开课老师、课程最大选课人数）（类方法）
"""
import StudentFile
import main


class Course(object):
    __c_list = []
    order = ""
    name = ""
    number = ""
    teacher = ""
    max_number = ""

    def __init__(self, order, name, number, max_number, teacher):
        self.order = order
        self.name = name
        self.number = number
        self.teacher = teacher
        self.max_number = max_number

    def check_number(self):
        print(main.align('课程序号', 20), main.align('当前人数', 20))
        print(main.align(self.order, 20), main.align(self.number, 20))

    def check_max_number(self):
        print(main.align('课程序号', 20), main.align('最大选课人数', 20))
        print(main.align(self.order, 20), main.align(self.max_number, 20))

    def check_teacher(self):
        print(main.align('课程序号', 20), main.align('开课老师', 20))
        print(main.align(self.order, 20), main.align(self.teacher, 20))

    @classmethod
    def add(cls, course):
        Course.__c_list.append(course)

    @classmethod
    def check_info(cls, ids):
        x = int(ids) - 1
        return Course.__c_list[x]

    @classmethod
    def check_order(cls, ids):
        for course in Course.__c_list:
            if course.order == ids:
                return 1
        print('不存在该课程')
        return 0

    @classmethod
    def check_order_t(cls, ids):
        for course in Course.__c_list:
            if course.order == ids:
                return 0
        return 1
    @classmethod
    def check_info_new(cls,ids):
        for course in cls.__c_list:
            if course.order == ids:
                return course
        return
    @classmethod
    def close_course(cls, ids):
        for student in StudentFile.s_temp_list:
            for course in student.c_list:
                if course.order == ids:
                    student.c_list.remove(course)
        for course in cls.__c_list:
            if course.order == ids:
                cls.__c_list.remove(course)

    def CourseView(self):
        print("############################################################")
        print('课程界面'.center(50))
        print('\n')
        print('查看当前课程人数请按[n]'.center(50))
        print('查看最大选课人数请按[m]'.center(50))
        print('查看当前课程开课老师请按[t]'.center(50))
        print('返回菜单请按[b]'.center(50))
        print("############################################################")
        flag = 0
        while flag == 0:
            request = input("请输入相应的命令(返回菜单请按b)：")
            if request == 'n':
                self.check_number()
            if request == 'm':
                self.check_max_number()
            if request == 't':
                self.check_teacher()
            if request == 'b':
                flag = 1
