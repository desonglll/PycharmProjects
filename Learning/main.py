# 按间距中的绿色按钮以运行脚本。
import append_student
import show_students

if __name__ == '__main__':
    print("Hello World")
    file_path="students.json"
    append_student.append_student(file_path)
    show_students.show_students(file_path)

