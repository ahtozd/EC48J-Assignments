# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:42:09 2019

@author: USER
"""



first_student = {"name": "Ahmet",
                 "student_id": '2015300000',
                 "password": '1234',
                 "gpa": 3.55,
                 "semester": 7,
                 "department": "Economics",
                 "courses": {}}

second_student = {"name": "Buse",
                 "student_id":'2015300001',
                 "password": '4321',
                 "gpa": 2.72,
                 "semester": 5,
                 "department": "Economics",
                 "courses": {}}

third_student = {"name": "Can",
                 "student_id": '2015300002',
                 "password": '3412',
                 "gpa": 3.14,
                 "semester": 6,
                 "department": "Management",
                 "courses": {}}

fourth_student = {"name": "Deniz",
                 "student_id": '2015300003',
                 "password": '1122',
                 "gpa": 2.56,
                 "semester": 6,
                 "department": "Political Science",
                 "courses": {}}

fifth_student = {"name": "Emre",
                 "student_id": '2015300004',
                 "password": '1313',
                 "gpa": 3.70,
                 "semester": 8,
                 "department": "Economics",
                 "courses": {}}


students={'2015300000':first_student,
          '2015300001':second_student,
          '2015300002':third_student,
          '2015300003':fourth_student,
          '2015300004':fifth_student}


for student in students:
    students[student]["schedule"] = {"M":[],
            "T": [],
            "W": [],
            "Th": [],
            "F": []}


courses = {"EC206": {"days":["M","M"],"slots":[3,4],"quota":3,"current":0},
           "EC48T": {"days":["M","M","M"],"slots":[5,6,7],"quota":3,"current":0},
           "EC48J": {"days":["T","T","T"],"slots":[1,2,3],"quota":3,"current":0},
           "EC331": {"days":["W","W","W"],"slots":[5,6,7],"quota":3,"current":0},
           "EC481": {"days":["Th","Th"],"slots":[1,2],"quota":2,"current":0},
           "EC406": {"days":["Th","Th"],"slots":[3,4],"quota":2,"current":0},
           "EC48Z": {"days":["Th","Th","Th"],"slots":[5,6,7],"quota":2,"current":0},
           "EC381": {"days":["T","T"],"slots":[3,4],"quota":1,"current":0},
           "EC411": {"days":["W","W"],"slots":[4,5],"quota":1,"current":0},
           "EC350": {"days":["T","T","T"],"slots":[3,4,5],"quota":3,"current":0}}

                

def start():
    while True:
        welcome = input("""
--- Welcome to BOUN REGISTRATION--- 

1. Login
2. Exit 

> """)
        
        if welcome == "1":
            return login()
        elif welcome == "2":
            print("See you later!")
            break
        
        
def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if username in students.keys():
            if password==students[username]['password']:
                print(f"""

Welcome {students[username]['name']}!""")
                return main_menu(username)
            else:
                print("Wrong username or password!")
                return start()
        else:
            print("Wrong username or password!")
            return start()
        
        
def main_menu(username):    
    while True:
        options = input("""
Please enter the number of service:
        
1. Course List Preparation
2. Courses and Quotas
3. My Schedule
4. My Account Information
5. Logout
        
> """)       
        if options == "1":
            return course_list_prep(username)
        elif options == "2":
            return courses_quotas(username)
        elif options == "3":
            print(students[username]["schedule"])
            print("Going back to main menu!")
        elif options == "4":
            return account_info(username)
        elif options == "5":
            return start()
    

def course_list_prep(username):
    while True:
        add_drop = input("""
1. Add Course
2. Drop Course

> """)
        if add_drop == "1":
            return add_course(username)
        elif add_drop == "2":
            return drop_course(username)
        

def add_course(username):
    while True:
        course = input("""
Please enter the course code you want to add.
> """)
        if course in courses.keys():
            if course in students[username]["courses"].keys():
                print("The course is already in your schedule!")
                return main_menu(username)
            elif len(conflict(username, course)) != 0:
                print("Conflict with", conflict(username, course))
                return main_menu(username)
            else:
                if courses[course]["current"] < courses[course]["quota"]:
                    courses[course]["current"] += 1
                    students[username]["courses"][course] = courses[course]
                    print(course,"added to your schedule!")
                    return add_schedule(username, course)
                else:
                    print("""
There is no quota!
                      
Going back to main menu!""")
                    return main_menu(username)
             
        
def drop_course(username):
    while True:
        course = input("""
Please enter the course code you want to drop.
> """)
        if course in students[username]["courses"].keys():
            courses[course]["current"] += -1
            del students[username]["courses"][course]
            print(f"{course} is successfully dropped!")
            return drop_schedule(username,course)
        else:
            print("""
The course is NOT in your schedule!
            
Going back to main menu!""")
            return main_menu(username)
            
        
def courses_quotas(username):
    while True:
        course = input("""
Please enter the course code.
> """)
        if course in courses.keys():
            print(f"""
{course}
Total Quota: {courses[course]["quota"]}
Registered: {courses[course]["current"]}
Days: {courses[course]["days"]}
Hours: {courses[course]["slots"]}
            
Going back to main menu!""")
            return main_menu(username)
        else:
            print("Please enter a valid course code!")
            
            
def account_info(username):
    print(f"""
Student ID: {username}
Name: {students[username]['name']}
GPA: {students[username]['gpa']}
Semester: {students[username]['semester']}
Department: {students[username]['department']}""")
    return main_menu(username)
            

        
def conflict(username,course):
    conflict_with = []
    for c in students[username]["courses"]:
        if courses[course]["days"][0] in students[username]["courses"][c]['days']:
            for slot in courses[course]["slots"]:
                if slot in students[username]["courses"][c]["slots"]:
                    conflict_with.append(c)
    return conflict_with
                

def add_schedule(username, course):
    day = courses[course]["days"][0]
    students[username]["schedule"][day].append([course,courses[course]["slots"]])
    return main_menu(username)
    

def drop_schedule(username, course):
    day = courses[course]["days"][0]
    students[username]["schedule"][day].remove([course,courses[course]["slots"]])
    return main_menu(username)
        


#start()  # uncomment this line to start the program
        


        

    

            
        













