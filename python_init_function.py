#!/usr/bin/python

class Student:

	def __init__( self , first: object , last: object , courses: object = None ) -> object:
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

	def remove_course(self, course) -> object:
		if course in self.courses:
			self.courses.remove(course)
		else:
			print(f"{self.first_name} is not enrolled in {course} course")

	def remove(self, course):
		pass

	def __str__(self):
		return f"First name: {self.first_name.capitalize()}\n" \
			   f"Last name: {self.last_name.capitalize()}\n" \
			   f"Courses: {', '.join(self.courses)}"



courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
chris = Student("chris", "gaughan", courses_1)
john = Student("john", "doe", courses_2)

print(chris.first_name, chris.last_name, chris.courses)
print(john.first_name, john.last_name, john.courses)
# print("Courses added to students")
chris.add_course("java")
chris.add_course("rails")
john.remove_course("rails")
john.remove_course("python")
chris.remove_course("python")
# John.remove_course("python")
print(john.first_name, john.last_name, john.courses)
print(chris.first_name, chris.last_name, chris.courses)
# print("Courses removed from students")
# mashrur.remove_course('rails')

print(chris.first_name, chris.last_name, chris.courses)
print(john.first_name, john.last_name, john.courses)
