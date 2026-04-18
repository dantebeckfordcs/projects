# My first Python project
name = input("What is your name? ")
age = int(input("How old are you? "))
goal = input("What is your career goal? ")

years_to_goal = 4

print(f"\n--- Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Goal: {goal}")  
print(f"You'll be {age + years_to_goal} when you achieve it.")
print(f"Let's get to work.")

hours = int(input("How many hours did you work on your goal today? "))

if hours >= 2:
    print("Great job! Keep it up!")
else: 
    print("If you don't do it today, you won't do it tomorrow. Let's get to work!")
if hours >= 3:
    print ("This is what you need to be doing to achieve your goal. Keep it up!")
days_to_graduation = 4 * 365
print(f"You have {days_to_graduation} days until you graduate. Let's make the most of them!")
print(f"That's {days_to_graduation * 24} hours!")

print("\nYour top 3 skills to build are:")
skills = ["Python", "Mathematics", "Communication"]
for skill in skills:
    print(f"- {skill}")

print(f"\nName 3 things you would like to learn!")
my_skills = []
for I in range(3):
    skill = input(f"Skill {I + 1}: ")
    my_skills.append(skill)

print("\nYour skills to learn are:")
for skill in my_skills:
    print(f"- {skill}")
cd C:/Users/imCJs/Projects
git init 
git add hello.py
git commit -m "Day one complete, come back tomorrow for day two!"
git remote add origin https://github.com/dantebeckfordcs/projects.git
git push -u origin master