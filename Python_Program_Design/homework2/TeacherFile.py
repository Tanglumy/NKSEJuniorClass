"""
导师
属性：      教师序号、姓名、开课列表（实例属性）
功能：      开课（实例方法）
	关闭课程（实例方法）
"""
import StudentFile
import main
import Course

t_temp_list = []
class Teacher:
    c_list = []
    name = ""
    order = ""

    def __init__(self, order, name):
        self.c_list = []
        self.order = order
        self.name = name

    def TeacherView(self):
        print("############################################################")
        print('教师界面'.center(50))
        print('\n')
        print('开课请按[o]'.center(50))
        print('关闭课程请按[a]'.center(50))
        print('查看课程请按[1]'.center(50))
        print('返回菜单请按[b]'.center(50))
        print('查看自己的所有课程请按[v]'.center(50))
        print("############################################################")
        flag = 0
        while flag == 0:
            request = input("请输入相应的命令(返回菜单请按b)：")
            if request == 'o':
                self.OpenCourse()
            if request == 'a':
                re = input('请输入你要关闭课程的序号：')
                self.CloseCourse(re)
            if request == '1':
                self.ViewCourse()
            if request == 'b':
                flag = 1
            if request == 'v':
                self.t_viewcourse()

    def t_viewcourse(self):
        print(main.align('序号', 20), main.align('课程序号', 20), main.align('课程名', 20), main.align('课程老师', 20),
              main.align('当前人数', 20), main.align('最大选课人数', 20))
        flag = 0
        for course in self.c_list:
            flag = flag + 1
            print(main.align(str(flag), 20), main.align(str(course.order), 20), main.align(str(course.name), 20),
                  main.align(str(course.teacher), 20), main.align(str(course.number), 20),
                  main.align(str(course.max_number), 20))

    def OpenCourse(self):
        course_id = input("请输入课程序号")
        if Course.Course.check_order_t(course_id):
            for course in self.c_list:
                if course.order == course_id:
                    print('该课程已经存在！')
                    return
            course_name = input("请输入课程名：")
            course_max_number = input("请输入课程最大数量")
            course = Course.Course(course_id, course_name, "0", course_max_number, self.name)
            Course.Course.add(course)
            self.c_list.append(course)
            print("开课成功")

    def CloseCourse(self, ids):
        for course in self.c_list:
            if course.order == ids:
                if course.teacher == self.name:
                    self.c_list.remove(course)
                    Course.Course.close_course(ids)
                    print('关闭课程成功!')
                    break
                else:
                    print('这是其他老师的课程，您无法关闭')
                    break
                print('没有该课程')

    def ViewCourse(self):
        re = input('请输入您要查询的课程序号：')
        course = Course.Course.check_info_new(re)
        if course != None:
            print(main.align('课程序号', 20), main.align('课程名', 20), main.align('课程老师', 20), main.align('当前人数', 20),
                  main.align('最大选课人数', 20))
            print(main.align(str(course.order), 20), main.align(str(course.name), 20),
                  main.align(str(course.teacher), 20),
                  main.align(str(course.number), 20), main.align(str(course.max_number), 20))
        else:
            print('找不到该课程，请重新输入')