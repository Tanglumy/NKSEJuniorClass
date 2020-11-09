import StudentFile
import TeacherFile
import Course
import sys


def align(str1, distance, alignment='left'):
    length = len(str1.encode('gbk'))
    space_to_fill = distance - length if distance > length else 0
    if alignment == 'left':
        str1 = str1 + ' ' * space_to_fill
    return str1


def Show_Menu():
    print("############################################################")
    print('南开大学选课系统v0.01a'.center(50))
    print('学生界面请按[s]'.center(50))
    print('老师界面请按[t]'.center(50))
    print('查看课程请按[c]'.center(50))
    print("############################################################")
    x = 1
    while x == 1:
        x = choice()


def choice():
    request = input("请输入相应的命令(退出请按q)：")
    if request == 's':
        s_id = input('请输入您的学号：')
        flag = 1
        for i in s_list:
            if i.order == s_id:
                i.StudentView()
                flag = 0
        if flag == 1:
            print('学号不存在,请重新输入')
        return 1
    if request == 't':
        t_id = input('请输入您的教工号：')
        flag = 1
        for i in t_list:
            if i.order == t_id:
                i.TeacherView()
                flag = 0
        if flag == 1:
            print('教工号不存在，请重新输入')
        return 1
    if request == 'c':
        c_id = input('请输入课程号')
        flag = 1
        course = Course.Course.check_info_new(c_id)
        if course!=None:
            course.CourseView()
        else:
            print("不存在该课程，请重新输入")
        return 1
    if request == 'q':
        print("farewell,my friend!")
        sys.exit(0)


student_list = []
s_list = []
teacher_list = []
t_list = []
if __name__ == '__main__':
    with open('./data.txt', 'r', encoding='UTF-8') as lines:
        array = lines.readlines()  # 该列表每一个元素是txt文件的每一行
        for a in array:
            a = a.strip('\n')  # 去掉换行符\n
            items = a.split()  # 空格切分
            if items[0] == 's':
                student_list.append(items)
            elif items[0] == 't':
                teacher_list.append(items)
            elif items[0] == 'c':
                course = Course.Course(items[1], items[2], items[3], items[4], items[5])
                Course.Course.add(course)

        # 2. 添加学生课程关系
        for s in student_list:
            student = StudentFile.Student(s[1], s[2])
            ids = s[3].split(',')  # 所选课程
            for i in ids:
                c = Course.Course.check_info(i)
                student.c_list.append(c)  # 加入选课
            s_list.append(student)
            StudentFile.s_temp_list = s_list
            # 3. 添加老师课程关系
        for t in teacher_list:
            teacher = TeacherFile.Teacher(t[1], t[2])
            ids = t[3].split(',')  # 所教课程
            for i in ids:
                c = Course.Course.check_info(i)
                teacher.c_list.append(c)
            t_list.append(teacher)
            TeacherFile.t_temp_list=t_list
    while 1:
        Show_Menu()
