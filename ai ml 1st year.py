#Fixed Subjects for marks
Subjects = ["Physics", "Chemistry", "Math", "English", "Computer Science"]

# Some sample data for testing
students = [
    {"roll_no": 1, "name": "Alice", "class": 10, "marks": {"Physics": 85, "Chemistry": 90, "Math": 95, "English": 88, "Computer Science": 92}},
    {"roll_no": 2, "name": "Bob", "class": 10, "marks": {"Math": 70}},  
    {"roll_no": 3, "name": "Charlie", "class": 9, "marks": {"Physics": 60, "English": 75}},
    {"roll_no": 4, "name": "David", "class": 11, "marks": {"Chemistry": 55, "Computer Science": 65}},
    {"roll_no": 5, "name": "Eva", "class": 12, "marks": {"Physics": 95, "Chemistry": 85, "Math": 80, "English": 90, "Computer Science": 88}}
]
#Defining FUNCTIONS

def getClass(allowAll = False):
    while True:
        inp = input("Enter class (1-12" + (", or ALL" if allowAll else "") + "): ")
        if allowAll and inp.upper() == "ALL":
            return "ALL"
        if inp.isdigit():
            num = int(inp)
            if num >= 1 and num <= 12:
                return num
        print("Oops wrong input, try again plz")

def getMarks():
    while True:
        mark = input("Enter marks (0-100 or NO): ")
        if mark.upper() == "NO":
            return None
        if mark.isdigit():
            m2 = int(mark)
            if m2 >= 0 and m2 <= 100:
                return m2
        print("Invalid marks!! (must be 0 to 100)")

def findStudent(cls, r):
    for st in students:
        if st["class"] == cls and st["roll_no"] == r:
            return st
    return None

def rollExists(cls, roll):
    for x in students:
        if x["class"] == cls and x["roll_no"] == roll:
            return True
    return False

def addStudent():
    cls = getClass()
    while True:
        try:
            rn = int(input("Enter roll number: "))
        except:
            print("not a valid number!!")
            continue
        if rollExists(cls, rn) == True:
            print("This roll already exists... please choose another")
        else:
            break

    nm = input("Enter name of student: ")
    marks = {}
    atleastOne = False

    print("Now enter marks (or type NO):")
    for sb in Subjects:
        mk = getMarks()
        if mk is not None:
            marks[sb] = mk
            atleastOne = True
    
    if atleastOne == False:
        print("You must enter at least one subject")
        return

    newStu = {"roll_no": rn, "name": nm, "class": cls, "marks": marks}
    students.append(newStu)
    print("Student added!")

def deleteStudent():
    c = getClass()
    try:
        rr = int(input("Enter roll to delete: "))
    except:
        print("bad input")
        return
    stu = findStudent(c, rr)
    if stu != None:
        students.remove(stu)
        print("deleted!")
    else:
        print("Not found!!")

def editStudent():
    print("What do you want to edit??")
    print("1-Class")
    print("2-Roll No")
    print("3-Name")
    print("4-Marks")

    choice = input("Enter choice: ")

    cls = getClass()
    try:
        rn = int(input("Enter roll: "))
    except:
        print("bad roll")
        return
    
    stu = findStudent(cls, rn)
    if stu == None:
        print("Student does not exist")
        return

    if choice == "1":
        nc = getClass()
        if rollExists(nc, rn):
            print("Duplicate roll in new class!!")
        else:
            stu["class"] = nc
            print("Class changed")
    elif choice == "2":
        try:
            nr = int(input("Enter new roll: "))
        except:
            print("bad input again")
            return
        if rollExists(cls, nr):
            print("Already used roll in class")
        else:
            stu["roll_no"] = nr
            print("Updated roll")
    elif choice == "3":
        newName = input("Enter new name: ")
        stu["name"] = newName
        print("Name updated")
    elif choice == "4":
        print("Subjects list:")
        for i in range(len(Subjects)):
            print(i+1, Subjects[i])
        try:
            sc = int(input("Pick subject no: "))
        except:
            print("wrong input")
            return
        if sc < 1 or sc > len(Subjects):
            print("invalid subject")
            return
        subj = Subjects[sc-1]
        val = getMarks()
        if val == None:
            val = 0
        stu["marks"][subj] = val
        print("Marks updated for", subj)
    else:
        print("Invalid option")


def showAll():
    print("---- All STUDENTS ----")
    for s in students:
        print("Class=", s["class"], " Roll=", s["roll_no"], " Name=", s["name"], " Marks=", s["marks"])


def subjectStats():
    for i in range(len(Subjects)):
        print(i+1, Subjects[i])
    try:
        ch = int(input("Enter subject no: "))
    except:
        print("bad input")
        return
    if ch < 1 or ch > len(Subjects):
        print("invalid subject")
        return

    sub = Subjects[ch-1]
    c = getClass(True)
    nums = []
    for s in students:
        if sub in s["marks"]:
            if c == "ALL" or s["class"] == c:
                nums.append(s["marks"][sub])

    if len(nums) == 0:
        print("No data")
    else:
        avg = sum(nums)/len(nums)
        print("Max:", max(nums))
        print("Average:", avg)


def classStats():
    c = getClass()
    avgs = []
    for s in students:
        if s["class"] == c:
            t = 0
            for sb in Subjects:
                if sb in s["marks"]:
                    t += s["marks"][sb]
                else:
                    t += 0
            a = t / len(Subjects)
            avgs.append(a)
    if len(avgs) == 0:
        print("No students in class", c)
    else:
        print("Class max avg:", max(avgs))
        print("Class avg:", sum(avgs)/len(avgs))


#Main Menu

def menu():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add or Delete")
        print("2. Edit Student")
        print("3. Show Students")
        print("4. Subject Stats")
        print("5. Class Stats")
        print("6. Exit")

        c = input("Enter option: ")
        if c == "1":
            xx = input("1-Add  2-Delete: ")
            if xx == "1":
                addStudent()
            elif xx == "2":
                deleteStudent()
            else:
                print("invalid again")
        elif c == "2":
            editStudent()
        elif c == "3":
            showAll()
        elif c == "4":
            subjectStats()
        elif c == "5":
            classStats()
        elif c == "6":
            print("Goodbye")
            break
        else:
            print("Invalid menu choice!")


# run the program
menu()