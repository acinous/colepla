class Course:
    def __init__(self, courseID, courseName, creditHrs, dept, prerequisites=None):
        self.courseID = courseID
        self.courseName = courseName
        self.creditHrs = creditHrs
        self.dept = dept
        self.prerequisites = prerequisites if prerequisites is not None else []