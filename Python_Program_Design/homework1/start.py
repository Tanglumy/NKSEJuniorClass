import os
import fileinput
def Show_Menu():
    print("############################################################")
    print('南开大学软件学院通讯录管理系统v0.01a'.center(50))
    print('添加数据请按[a]'.center(50))
    print('查看数据请按[s]'.center(50))
    print('删除数据请按[d]'.center(50))
    print('修改睡请按[m]'.center(50))
    print('返回菜单请按[q]'.rjust(50))
    print("############################################################")
def start():

    request = input("请输入相应的命令(返回菜单请按q)：")
    if request == 'a':
        add_Data()
    if request == 's':
        inspect_Data()
    if request == 'm':
        modify_Data()
    if request == 'd':
        temp = input('请输入序列：')
        delete_Data(temp)
    if request == 'q':
        Show_Menu()
def add_Data():
    a = input('请输入您的姓名：')
    b = input('请输入您的QQ号码：')
    c = input('请输入您的电话号码：')
    d = input('请输入您的邮箱：')
    print('添加成功!')
    print('修改/添加数据'.center(37, '～'))
    f=open("Label.txt",mode='r')
    lines = len(f.readlines())
    f.close()
    f=open("Label.txt",mode='a')
    f.write('{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}'.format(lines,a,b,c,d))
    f.write('\n')
    f.close()
    f=open("Label.txt",mode='r')
    data=f.read()
    print(data)
    # mylist.append(temp)



def inspect_Data():
    print('通讯录数据列表'.center(37, '～'))
    f = open("Label.txt", mode='r')
    data = f.read()
    print(data)




def delete_Data(temp):
    with open('Label.txt', 'r') as r:
        lines = r.readlines()
    with open('Label.txt', 'w+') as w:
        for l in lines:
            if temp not in l:
                w.write(l)



def modify_Data():
    a=input('请输入你需要修改的序号')
    b=input('请输入你需要修改的原内容')
    c=input('请输入你需要修改的内容')
    lines = open('Label.txt').readlines()
    fp = open('Label.txt','w')
    for s in lines:
        if a in s:
            fp.write(s.replace(b, c,1).replace('yes', 'no'))
        else:
            fp.write(s)
    fp.close()  # 关闭文件
    print('修改成功')