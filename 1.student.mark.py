def input_student():
    student_num = int(input("enter number of students"))
    students = []

    for i in range(student_num):
        student_id = input("Student ID: ")
        student_name = input("Student name: ")
        student_dob = input("Student DoB: ")
        student_info = {'name': student_name, 'id': student_id, 'dob': student_dob, 'marks': {}}
        students.append(student_info)

    return students

def input_course():
    course_num = int(input('enter number of course(s): '))
    courses = []

    for i in range(course_num):
        course_id = input("Course ID: ")
        course_name = input("course name: ")
        course_info = {'name': course_name, 'id': course_id}
        courses.append(course_info)

        return courses 
    
student_list = input_student()
course_list = input_course()