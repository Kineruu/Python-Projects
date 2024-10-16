"""
- courseName: a string that represents the name of the course
- courseGrade: a float that represents the code of the course
Create a structure named Student that represents a student, and contains the following members:
- studentName: a string that represents the name of the student
- studentID: an integer that represents the ID of the student
- numC ( an integer for the number of courses)
- courses, an array of type Course
- function named readStudent that prints the name, ID, and grade of the student.
- function named printStudent that prints the name, ID, and grade of the student.
- function float calculateAverage, that calculates the average grade from all courses.
"""

#* I finally learnt how to use class in python I guess? I have to do more projects with class.

class Course:
    def __init__(self, courseName, courseGrade):
        self.courseName = courseName
        self.courseGrade = courseGrade

class Student:
    def __init__(self, studentName, studentID, numC):
        self.studentName = studentName
        self.studentID = studentID
        self.numC = numC
        self.courses = []
    
    def readStudent(self):
        for x in range(self.numC):
            courseName = str(input("Course name: "))
            courseGrade = float(input("Course grade: "))
            course = Course(courseName, courseGrade)
            self.courses.append(course)
 
    def printStudent(self):
        print(f"{self.studentName, self.studentID, self.numC}")
        for course in self.courses:
            print(f"{course.courseName}: {course.courseGrade}")
    
    def calculateAverage(self):
        if not self.courses:
            return 0.0
        
        totalGrades = sum(course.courseGrade for course in self.courses)
        return totalGrades / self.numC
    

StudentName = input(str("Name: "))
StudentID = input("ID: ")
StudentID = int(StudentID)
StudentCoursesNumber = input("Courses (Number): ")
StudentCoursesNumber = int(StudentCoursesNumber)
student1 = Student(StudentName, StudentID, StudentCoursesNumber)
student1.readStudent()
student1.printStudent()

averageGrade = student1.calculateAverage()
print(f"Average grade is {averageGrade:.2f}")
    