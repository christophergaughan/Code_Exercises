#!/usr/bin/python

class Student:

	def __init__(self, first, last, courses=None):
		self.course = None
		self.first_name = first
		self.last_name = last
		if courses == None:
			self.courses = []
		else:
			self.courses = courses

	def add_course(self, course):
		if course not in self.courses:
			self.append(course)
		else:
			print(f"{self.first_name} is already enrolled in {course} Dammit!")

	def append(self, course):
		pass

	def remove_course(self, course):
		if course in self.courses:
			self.courses.remove(course)
		else:
			print(f"{self.first_name} is not enrolled in the {course} course")

	def remove(self, course):
		pass




courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
Chris = Student("Chris", "Gaughan", courses_1)
John = Student("John", "Doe", courses_2)

print(Chris.first_name, Chris.last_name, Chris.courses)
print(John.first_name, John.last_name, John.courses)
#print("Courses added to students")
Chris.add_course("java")
Chris.add_course("rails")
John.remove_course("rails")
John.remove_course("python")
Chris.remove_course("python")
#John.remove_course("python")
print(John.first_name, John.last_name, John.courses)
print(Chris.first_name, Chris.last_name, Chris.courses)
#print("Courses removed from students")
#mashrur.remove_course('rails')

#print(mashrur.first_name, mashrur.last_name, mashrur.courses)
#print(john.first_name, john.last_name, john.courses)