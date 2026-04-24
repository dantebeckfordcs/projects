# Career Advisor V2
# Created by Dante Beckford on 4/19/2026, after deciding that I want to be a Forward Deployed Software Engineer, this is my first project ever.
# A Career Advisor that takes in info and develops a personalized roadmap for the user.

print("=" * 50)
print("CAREER ADVISOR V2 - Personalized Career Guidance")
print("=" * 50)
print()

#Section 1: Collecting Basic User Information
print("Let's start by getting to know you better!")
print("Please answer the following questions honestly.")

name = input("What is your name?")
while True: 
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:        print("Please enter a valid number for your age.")    
location = input("Where do you currently live?")

#Section 2: Career Goals and Interests
print()
print("=" * 50)
print("PASSIONS AND CAREER INTERESTS")
print("=" * 50)
career_goal = input("What is your ultimate and ideal career goal? ")
education = input ("What is your current level of education? (e.g., High School, Bachelor's, etc.) ")
passion = input("What are you passionate about? What activity can you do for hours without getting bored that isn't obviously entertaining and may be boring to others? ")
experience = input("Do you have any relevant experience in your desired field? If so, please describe it briefly. ")
while True: 
    try:
        hours = int(input("How many hours per week can you realistically dedicate to pursuing your career goals? "))
        break 
    except ValueError: print() 
income = input("What is your desired income range for your career? ")

#Section 3: Personalized Roadmap
def display_roadmap(career_goal, education, passion, experience, hours, income):
    print()
    print("=" * 50)
    print("PERSONALIZED ROADMAP")
    print("=" * 50)
    print()
    print(f"Career Goal: {career_goal}")
    print(f"Education: {education}")
    print(f"Passion: {passion}")
    print(f"Experience: {experience}")
    print(f"Hours per Week: {hours}")
    print(f"Desired Income Range: {income}")

#Section 4: API Integration
#Confirmation
print("\nHere's what we have on you.")
print(f"name: {name}")
print(f"age: {age}")
print(f"location: {location}")
print(f"career goal: {career_goal}")
print(f"education: {education}")
print(f"passion: {passion}")
print(f"experience: {experience}")
print(f"hours per week: {hours}")
print(f"desired income: {income}")
confirm = input("Is this information correct? (yes/no) ")
if confirm.lower() != "yes":
    print("Let's start over and get the correct information.")
import ollama
message = f"""You are an encouraging and practical career advisor helping students discover their path.
You must always provide a helpful roadmap regardless of the student's current situation.
Never refuse to help. Always give actionable steps from where they are right now.

Here is the student's information:
Name: {name}
Age: {age}
Location: {location}
Career Goal: {career_goal}
Education: {education}
Passion: {passion}
Experience: {experience}
Hours per week available: {hours}
Desired income: {income}

Provide a friendly, detailed, step by step roadmap for this student.
Start from their current situation and build up realistically.
Include what to learn first, what to learn next, timeline estimates, and free resources to use, alongside this provide people and places they can contact to learn more about various things such as university majoring programs, FAFSA etc and how to do all that for those that may not have help.
Be encouraging but honest about the journey ahead, and make sure to provide a clear path forward, the overall tone should be very positive and uplifting, but also practical and realistic."""
response = ollama.chat(model="llama3.2", messages=[{"role":"user","content":message}])

print()
print("=" * 50)
print("YOUR PERSONALIZED CAREER ROADMAP")
print("=" * 50)
print()
print(response['message']['content'])
