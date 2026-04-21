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
age = int(input("How old are you? "))
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
hours = int(input("How many hours per week can you dedicate to working towards your career goal? "))   
income = input("What is your desired income range for your career? ")

#Section 3: Personalized Roadmap
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
Include what to learn first, what to learn next, timeline estimates, and free resources.
Be encouraging but honest about the journey ahead."""
response = ollama.chat(model="llama3.2", messages=[{"role":"user","content":message}])

print()
print("=" * 50)
print("YOUR PERSONALIZED CAREER ROADMAP")
print("=" * 50)
print()
print(response['message']['content'])