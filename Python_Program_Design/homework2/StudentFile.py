import main
import Course
import TeacherFile

'''
学生
属性：      学生本人序号、姓名、已选课程列表（实例属性）
功能：      可以查看学生本人选课内容（实例方法）
	选课（实例方法）
	退课（实例方法）
'''

s_temp_list=[]
class Student:
    order = ""
    name = ""
    c_list = []

    def __init__(self, order, name):
        self.name = name
        self.order = order
        self.c_list = []

    # def InspectCourse(self):

    def StudentView(self):
        print("############################################################")
        print('学生界面'.center(50))
        print('查看选课内容请按[c]'.center(50))
        print('选课请按[a]'.center(50))
        print('退课请按[d]'.center(50))
        print('查看课程请按[1]'.center(50))
        print('返回菜单请按[b]'.center(50))
        print("############################################################")
        flag = 0
        while flag == 0:

            request = input("请输入相应的命令(返回菜单请按b)：")
            if request == 'c':
                self.s_viewcourse()
            if request == 'a':
                self.TakeCourse()
            if request == 'd':
                re = input('请输入你要退课的序号：')
                self.DropCourse(re)
            if request == '1':
                self.ViewCourse()
            if request == 'b':
                flag = 1
    def TakeCourse(self):
        course_id = input('请输入你要选课的序号')
        if Course.Course.check_order(course_id):
            for course in self.c_list:
                if course.order == course_id:
                    print('已经选过了,请勿重复选择')
                    return
            course = Course.Course.check_info(course_id)
            if course.number < course.max_number:
                course.number = str(int(course.number) + 1)
                self.c_list.append(course)
                print('选课成功')
            else:
                print('人数已经达到上线')

    def s_viewcourse(self):

        print(main.align('序号', 20), main.align('课程序号', 20), main.align('课程名', 20), main.align('课程老师', 20),
              main.align('当前人数', 20), main.align('最大选课人数', 20))
        flag = 0
        for course in self.c_list:
            flag = flag + 1
            print(main.align(str(flag), 20), main.align(str(course.order), 20), main.align(str(course.name), 20),
                  main.align(str(course.teacher), 20), main.align(str(course.number), 20),
                  main.align(str(course.max_number), 20))

    # def TakeCourse(self):

    def DropCourse(self, ids):
        for course in self.c_list:
            if course.order == ids:
                self.c_list.remove(course)
                course.number = str(int(course.number)-1)
                print('退课成功')
                return

        print('没有该课程')

    def ViewCourse(self):
        re = input('请输入您要查询的课程序号：')
        course = Course.Course.check_info_new(re)
        if course != None:
            print(main.align('课程序号', 20), main.align('课程名', 20), main.align('课程老师', 20), main.align('当前人数', 20),
                  main.align('最大选课人数', 20))
            print(main.align(str(course.order), 20), main.align(str(course.name), 20), main.align(str(course.teacher), 20),
              main.align(str(course.number), 20), main.align(str(course.max_number), 20))
        else:
            print('找不到该课程，请重新输入')
