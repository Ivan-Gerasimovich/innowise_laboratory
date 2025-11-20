def generate_profile(age: int) -> str: # strange name of func, but TS requiers this
    """
    Determines the life stage based on the age provided.
    
    Args:
        age (int): The user's age.
        
    Returns:
        str: 'Child', 'Teenager', or 'Adult'.
    """
    if age > 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        else:
            return "Adult"
    return "Havent u been born?"


print("Hey! What's up? Pleast, inter your full name: ")

user_name = input()

print('Well, now please tell me your birth date: ')

birth_year = int(input())

current_age = 2025 - birth_year # getting user's age
user_life_stage = generate_profile(current_age)

hobbies = []

while True:
    print("Tell me please, what hobbie do u have? ")
    user_input = input()
    if user_input.lower() == "stop":
        break
    hobbies.append(user_input)


user_profile = {
    "name": user_name,
    "age": current_age,
    "life_stage": user_life_stage,
    "hobbies": hobbies
} # create a dict with user profile data


print("Okay, look what we've got: ")

print(f"""
***
Profile summary:
Name: {user_profile["name"]}
Age: {user_profile["age"]}
Life Stage: {user_profile["life_stage"]}""") 
if user_profile["hobbies"]:
    print(f"Favorite hobbies: {len(user_profile["hobbies"])}")
    for hobbie in user_profile["hobbies"]:
        print("- " + hobbie) # printing hobbies in a list
else:
    print("You didn't mention any hobbies :(")
print("***")

