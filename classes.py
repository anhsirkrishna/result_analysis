class Subject(object):
	
	def __init__(self,cia,ext):
		self.cia = cia
		self.ext = ext
		self.subject_total = cia + ext 
		
class Student(object):
	
	def __init__(self,name,reg_no,subjects,total,percent,result):
		self.name = name
		self.reg_no = reg_no
		self.subjects = subjects
		self.total = total
		self.percent = percent
		self.result = result		

class Semester(object):

	def __init__(self):
		self.students = []
	
	def add_student(self,student):
		self.students.append(student)
	
	@property
	def total_students(self):
		