# 按间距中的绿色按钮以运行脚本。
from json_handle import show_students, append_student

if __name__ == '__main__':
    print("Hello World")
    file_path = "data/students.json"
    # show_students.show_students(file_path)
    while True:
        print("1: append students")
        print("2: show students")
        print("3: exit")
        tmp = int(input())
        if tmp == 1:
            append_student.append_student(file_path)
        if tmp == 2:
            show_students.show_students(file_path)
        if tmp == 3:
            break
