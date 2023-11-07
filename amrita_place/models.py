from sqlalchemy import Column, Integer, String, Text, ForeignKey, Double, Boolean
# from sqlalchemy.orm  import relationship, Mapped, mapped_column
from amrita_place.database import Base
# from sqlalchemy.sql import func

# Example Classes for creating tables, and PK, FK relations

# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True)
#     firstname = Column(String(100), nullable=False)
#     lastname = Column(String(100), nullable=False)
#     email = Column(String(80), unique=True, nullable=False)
#     age = Column(Integer)
#     created_at = Column(DateTime(timezone=True),
#                            server_default=func.now())
#     bio = Column(Text)
#     course_id = mapped_column(ForeignKey("courses.course_id")) # Child table 

#     def __init__(self, firstname, lastname): # constructor. Defines what to do when you do stu = Student("Bob", "Morly", ...)
#         self.firstname = firstname


#     def __repr__(self): # this tells python what to print if you do print(student) where student is a Student object.
#         return f'<Student {self.firstname}>'
    
# class Courses(Base):
#     __tablename__ = "courses"
#     course_id = Column(Integer, primary_key=True)
#     course_name = Column(String(100), nullable=False)
#     children = relationship() # Parent table

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(Text, nullable=False, unique=True)
#     password_hash = Column(Text)

#     def __init__(self, username, password_hash):
#         self.username = username
#         self.password_hash = password_hash
    
#     def __repr__(self):
#         return f"<User {self.username}>"

class Student(Base):
    __tablename__ = 'student'
    roll_no = Column(String(50), primary_key=True)
    email_id = Column(String(100))
    name = Column(String(100))
    linkedIN_profile = Column(String(500))
    salary = Column(Integer)
    CGPA = Column(Double())
    companyID = Column(Integer, ForeignKey('company.CompanyID'))
    adminID = Column(Integer, ForeignKey('administrator.AdminID'))

    def __init__(self, roll_no, email_id, name, linkedIN_profile, salary, CGPA, companyID, adminID):
        self.roll_no = roll_no
        self.email_id = email_id
        self.name = name
        self.linkedIN_profile = linkedIN_profile
        self.salary = salary
        self.CGPA = CGPA
        self.companyID = companyID
        self.adminID = adminID

class PhoneNumber(Base):
    __tablename__ = 'phone_number'
    rollNumber = Column(String(50), ForeignKey('student.roll_no'), primary_key=True)
    phoneNumber = Column(String(15))

    def __init__(self, rollNumber, phoneNumber):
        self.rollNumber = rollNumber
        self.phoneNumber = phoneNumber

class Company(Base):
    __tablename__ = 'company'
    logo = Column(String(500))
    name = Column(String(100))
    CompanyID = Column(Integer, primary_key=True)

    def __init__(self, logo, name):
        self.logo = logo
        self.name = name

class Degree(Base):
    __tablename__ = 'degree'
    programID = Column(String(50), primary_key=True)
    name = Column(String(100))
    branch = Column(String(3))

    def __init__(self, programID, name, branch):
        self.programID = programID
        self.name = name
        self.branch = branch

class InterviewExperience(Base):
    __tablename__ = 'interview_experience'
    interviewID = Column(Integer, primary_key=True)
    positivePoints = Column(Text)
    isJobSecured = Column(Boolean)
    improvements = Column(Text)
    rollNumber = Column(String(50), ForeignKey('student.roll_no'))
    companyID = Column(Integer, ForeignKey('company.CompanyID'))

    def __init__(self, interviewID, positivePoints, isJobSecured, improvements, rollNumber, companyID):
        self.interviewID = interviewID
        self.positivePoints = positivePoints
        self.isJobSecured = isJobSecured
        self.improvements = improvements
        self.rollNumber = rollNumber
        self.companyID = companyID

class Administrator(Base):
    __tablename__ = 'administrator'
    username = Column(String(50))
    AdminID = Column(Integer, primary_key=True)
    PasswordHash = Column(String(256))
    Name = Column(String(100))

    def __init__(self, username, PasswordHash, Name):
        self.username = username
        self.PasswordHash = PasswordHash
        self.Name = Name

class StudentDegreeHolder(Base):
    __tablename__ = 'student_degree_holder'
    rollNumber = Column(String(50), ForeignKey('student.roll_no'), primary_key=True)
    ProgrammeID=Column(String(50), ForeignKey('degree.programID'))

    def __init__(self, rollNumber, ProgrammeID):
        self.rollNumber = rollNumber
        self.ProgrammeID = ProgrammeID





    
