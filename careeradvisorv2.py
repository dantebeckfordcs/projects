def run_advisor():
    print("=" * 50)
    print("  CAREER ADVISOR - Personalized Career Guidance")
    print("=" * 50)
    print()
    
    # All your input questions here
    name = input("What is your name? ")
    
    while True:
        try:
            age = int(input(f"Nice to meet you {name}. How old are you? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    location = input("Where are you currently located? ")
    career_goal = input("What is your career goal? ")
    education = input("What is your highest level of education? ")
    experience = input("Do you have any relevant experience? ")
    passion = input("What are you passionate about? ")
    
    while True:
        try:
            hours = int(input("How many hours per week can you study? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    income = input("What is your desired income range? ")
    
    # Confirmation
    print()
    print("=" * 50)
    print("Here is what we have on you:")
    print("=" * 50)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Location: {location}")
    print(f"Career Goal: {career_goal}")
    print(f"Education: {education}")
    print(f"Experience: {experience}")
    print(f"Passion: {passion}")
    print(f"Hours per week: {hours}")
    print(f"Desired Income: {income}")
    print()
    
    confirm = input("Is this correct? (yes/no) ")
    
    if confirm.lower() != "yes":
        print("\nLet's start over.\n")
        run_advisor()
        return
    
    # AI Generation
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

    print()
    print("=" * 50)
    print("  GENERATING YOUR PERSONALIZED ROADMAP...")
    print("=" * 50)
    print()
    
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": message}])
    print(response['message']['content'])
    
    print()
    print("=" * 50)
    print("  Good luck on your journey.")
    print("=" * 50)

# Run the program
run_advisor()