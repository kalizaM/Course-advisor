# advisor.py
import groq
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")


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


def get_recommendations(student):
    # Build the prompt (the message we send to Groq)
    # using the student's info
    prompt = build_prompt(student)

    # Create a client (open a connection to Groq)
    # using our secret API key as identification
    client = groq.Groq(api_key=api_key)

    # Send the prompt to Groq as a message and
    # store the response it sends back
    # model is which AI we're using on Groq
    # messages is a list with one item — our prompt
    # role "user" means this is coming from the user
    # content is the actual text we're sending
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Pull just the text out of the response object
    # (the response comes back with a lot of extra
    # info we don't need — this grabs just the message)
    return response.choices[0].message.content


# Prompting the user and creating a real student object
user_person = Student(
    input("Enter your name: "),
    input("Enter your school name: "),
    input("Enter your major: "),
    int(input("Enter total credits completed: ")),
    input("Enter courses taken (example: CMSC131, CMSC132): ")
)
recommendations = get_recommendations(user_person)
print("\nYour recommended courses:")
print(recommendations)
