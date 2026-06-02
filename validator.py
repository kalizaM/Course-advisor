import requests

name = input("Please enter your name:")
# print("Please enter your name")

school_name = input("Please enter your school name:")

major = input("Please enter your Major")

total_credit = input("Please enter your total number of credits completed")

courses_taken = []
courses_taken = input(
    "Please enter the courses youve takevn by course id and seperate each course by a comma")

print(name, school_name, major, total_credit, courses_taken)
