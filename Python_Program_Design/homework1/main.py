
import start
if __name__ == "__main__":
    start.Show_Menu()
    f = open("Label.txt", mode='w+')
    f.write('{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
    f.write('\n')
    f.close()
    while 1:
        start1=start.start()
