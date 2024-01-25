import re


class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.course_taken = 0


class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password


class University:
    courses = []
    student_courses = {}
    professors = []
    students = []
    current_menu = "log in/sign up menu"
    last_student_id = None

    def __init__(self):
        pass

    def current_menu_method(self):
        print(self.current_menu)

    def signup(self, sign_type, user_id, name, password):
        if University.current_menu == "log in/sign up menu":
            if sign_type == "S" or sign_type == "P":
                if not re.findall(r"\D", user_id):
                    user_id = int(user_id)
                    if not re.findall(r"\s", name):
                        if len(password) >= 4 and not re.findall(r"\s", password) and re.findall("[*.!@$%^&()]", password):
                            if sign_type == "S":
                                for student in University.students:
                                    if student.user_id == user_id:
                                        print("id already exists")
                                        return
                                for professor in University.professors:
                                    if professor.user_id == user_id:
                                        print("id already exists")
                                        return
                                University.students.append(User(user_id, name, password))
                                print("signed up successfully!")
                            elif sign_type == "P":
                                for professor in University.professors:
                                    if professor.user_id == user_id:
                                        print("id already exists")
                                        return
                                for student in University.students:
                                    if student.user_id == user_id:
                                        print("id already exists")
                                        return
                                University.professors.append(User(user_id, name, password))
                                print("signed up successfully!")
                        else:
                            print("invalid password")
                    else:
                        print("invalid name")
                else:
                    print("invalid id")
            else:
                print("invalid type")
        else:
            print("invalid command")

    def log_in(self, user_id, password):
        sth = False
        if not re.findall(r"\D", user_id):
            user_id = int(user_id)
            for user in University.students:
                if user.user_id == user_id:
                    sth = True
                    if user.password != password:
                        print("incorrect password")
                        return
                    print("logged in successfully!\nentered student menu")
                    University.current_menu = "student menu"
                    University.last_student_id = user_id
                    break
            if not sth:
                for user in University.professors:
                    if user.user_id == user_id:
                        sth = True
                        if user.password != password:
                            print("incorrect password")
                            return
                        print("logged in successfully!\nentered professor menu")
                        University.current_menu = "professor menu"
                        break
            if not sth:
                print("incorrect id")
        else:
            print("incorrect id")

    def add_course(self, course_name, course_id, capacity):
        if University.current_menu == "professor menu":
            if not re.findall(r"\s", course_name):
                if not re.findall(r"\D", course_id):
                    course_id = int(course_id)
                    if not re.findall(r"\D", capacity):
                        capacity = int(capacity)
                        for course in University.courses:
                            if course.course_id == course_id:
                                print("course id already exists")
                                return
                        University.courses.append(Course(course_id, course_name, capacity))
                        print("course added successfully!")
                        return
                    else:
                        print("invalid course capacity")
                else:
                    print("invalid course id")
            else:
                print("invalid course name")
        else:
            print("invalid command")

    def get_course(self, course_id, student_id):
        if student_id != None:
            if not re.findall(r"\D", course_id):
                course_id = int(course_id)
                student_id = int(student_id)
                if University.current_menu == "student menu":
                    for course in University.courses:
                        if course.course_id == course_id:
                            for idss in University.student_courses:
                                if student_id == idss:
                                    for taken_course_id in University.student_courses[student_id]:
                                        if taken_course_id == course_id:
                                            print("you already have this course")
                                            return
                                    if course.capacity == course.course_taken:
                                        print("course is full")
                                        return
                                    else:
                                        University.student_courses[student_id].append(course_id)
                                        course.course_id += 1
                                        print("course added successfully!")
                                        return
                            if course.capacity == course.course_taken:
                                print("course is full")
                                return
                            else:
                                University.student_courses[student_id] = []
                                University.student_courses[student_id].append(course_id)
                                course.course_taken += 1
                                print("course added successfully!")
                                return
                    print("incorrect course id")
                else:
                    print("invalid command")
            else:
                print("incorrect course id")
        else:
            print("invalid command")
    def show_course_list(self):
        if University.current_menu == "student menu" or University.current_menu == "professor menu":
            print("course list:")
            for course in University.courses:
                print(course.course_id, course.name, course.course_taken, end="/")
                print(course.capacity)
        else:
            print("invalid command")

    def log_out(self):
        if University.current_menu != "log in/sign up menu":
            University.current_menu = "log in/sign up menu"
            print("logged out successfully!")
            print("entered log in/sign up menu")
        else:
            print("invalid command")


while True:
    x = input().strip()
    daneshgah_daryai = University()
    if re.match(r"^edu exit edu$", x):
        break
    elif x == "edu current menu edu":
        daneshgah_daryai.current_menu_method()
    elif re.match(r'^edu sign up -(.+) -i (.+) -n (.+) -p (.+) edu$', x):
        match = re.match(r'^edu sign up -(.+) -i (.+) -n (.+) -p (.+) edu$', x)
        daneshgah_daryai.signup(match.group(1), match.group(2), match.group(3), match.group(4))
    elif re.match(r"^edu log in -i (.+) -p (.+) edu$", x):
        match = re.match(r"^edu log in -i (.+) -p (.+) edu$", x)
        daneshgah_daryai.log_in(match.group(1), match.group(2))
    elif x == "edu show course list edu":
        daneshgah_daryai.show_course_list()
    elif x == "edu log out edu":
        daneshgah_daryai.log_out()
    elif re.match(r"^edu add course -c (.+) -i (.+) -n (.+) edu$", x):
        match = re.match(r"^edu add course -c (.+) -i (.+) -n (.+) edu$", x)
        daneshgah_daryai.add_course(match.group(1), match.group(2), match.group(3))
    elif re.match(r"^edu get course -i (.+) edu$", x):
        match = re.match(r"^edu get course -i (.+) edu$", x)
        daneshgah_daryai.get_course(match.group(1), daneshgah_daryai.last_student_id)
    else:
        print("invalid command")
