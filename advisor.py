# advisor.py

class Student:
    # The blueprint for a student object.
    # __init__ runs automatically when you create
    # a new student and sets up all their info.
    def __init__(self, name, school_name, major, total_credit, courses_taken):
        self.name = name
        self.school_name = school_name
        self.major = major
        self.total = total_credit
        self.courses = courses_taken


def build_prompt(student):
    # Packages the student's info into a message
    # that DeepSeek can read and respond to.
    message = f"""
    My name is {student.name}.
    I am studying {student.major} at {student.school_name}.
    I have completed {student.total} credits so far.
    The courses I have already taken are: {student.courses}.
    Based on my major requirements, please recommend 
    what courses I should take next to complete my 
    degree as efficiently as possible.
    Return your response as a JSON list of course codes.
    """
    return message


# Prompting the user and creating a real student object
user_person = Student(
    input("Enter your name: "),
    input("Enter your school name: "),
    input("Enter your major: "),
    int(input("Enter total credits completed: ")),
    input("Enter courses taken (example: CMSC131, CMSC132): ")
)

# Test print to confirm the object was created correctly
print(user_person.name, user_person.major, user_person.school_name,
      user_person.courses, user_person.total)
