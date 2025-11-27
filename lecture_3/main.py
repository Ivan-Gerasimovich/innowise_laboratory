students = []

def add_student(students: list[dict[str, list[int]]]) -> list[dict[str, list[int]]]:
    """
    Creates a new student profile. 
    Checks for duplicates before adding to the list.
    """
    new_student_list = students.copy()
    new_name = input("Okay, type student's name: ").strip()

    # Let's check if we already have this student in our DB
    if any(student["name"] == new_name for student in new_student_list):
        print("This student already exists!")
    else:
        # Fresh start: empty list of grades
        new_student = {"name": new_name, "grades": []}
        new_student_list.append(new_student)
        print(f"Student {new_name} was added to database!")

        # Maybe the user wants to add grades right away?
        user_answer = input("Do you want to type grades right now? (Y/n) ").lower()
        match user_answer:
            case "y":
                # Pass the updated list so the new student can get grades
                new_student_list = add_grades(new_student_list, new_name)
            case _:
                print("Okay, I've got this")

    return new_student_list


def add_grades(students: list[dict[str, list[int]]], student_name: str) -> list[dict[str, list[int]]]:
    """
    Finds the student and starts a loop to add grades one by one.
    Handles invalid inputs (like text instead of numbers).
    """
    new_student_list = students.copy()
    
    # First, we need to find where this student is in our list
    student_index = -1
    for i, student in enumerate(new_student_list):
        if student["name"] == student_name:
            student_index = i
            break
    
    # If we found the guy, let's ask for grades
    if student_index != -1:
        print(f"Okay, input grades for {student_name}. Type 'done' when finished.")
        
        while True:
            user_input = input("Enter a grade (0-100): ").strip()
            
            # Stop the loop if user is tired
            if user_input.lower() == 'done':
                break
            
            # Try to convert input to int, otherwise catch the error
            try:
                grade = int(user_input)
                if 0 <= grade <= 100:
                    new_student_list[student_index]["grades"].append(grade)
                else:
                    print("Hey, grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    else:
        print("I dont know this student!")

    return new_student_list


def make_report(students: list[dict[str, list[int]]]) -> None:
    """
    Calculates averages for everyone and prints a nice summary at the end.
    """
    if not students:
        print("No students found.")
        return

    all_averages = [] 

    print("\n--- Student Report ---")
    for student in students:
        grades = student["grades"]
        
        # Avoid dividing by zero if the student has no grades yet
        if len(grades) > 0:
            avg = sum(grades) / len(grades)
            all_averages.append(avg)
            print(f"{student['name']}'s average grade is {avg:.2f}.")
        else:
            print(f"{student['name']}'s average grade is N/A.")

    # If we have any data, show the big picture stats
    if all_averages:
        max_result = max(all_averages)
        min_result = min(all_averages)
        overall_avg = sum(all_averages) / len(all_averages)
        
        print("\n--- Summary ---")
        print(f"Max Average: {max_result:.2f}")
        print(f"Min Average: {min_result:.2f}")
        print(f"Overall Average: {overall_avg:.2f}")
    else:
        print("\nNothing to summarize yet.")


def find_top_performer(students: list[dict[str, list[int]]]) -> None:
    """
    Finds the student with the highest average score.
    """
    # Filter out students who have empty grade lists
    valid_students = [s for s in students if len(s["grades"]) > 0]

    if not valid_students:
        print("No students with grades found.")
        return

    # Use max() with a lambda to compare them by their calculated average
    top_student = max(valid_students, key=lambda s: sum(s["grades"]) / len(s["grades"]))
    
    # Calculate the score again just for printing
    top_avg = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"The top performer is {top_student['name']} with an average of {top_avg:.2f}.")


while True:
    print("""
Hello! Tell me, what u wanna do?
If u want to:
1. Add a new student - type AddS (or 1)
2. Add a new grades for a student - type AddG (or 2)
3. Show report - type R (or 3)
4. Find top reporter - type F (or 4)
5. Exit - type Exit
    """)
    
    # Using try/except here just in case input blows up
    try:
        user_input = input("Your choice: ").lower().strip()
        
        match user_input:
            case "exit" | "5":
                print("Bye!")
                break
            case "adds" | "1":
                students = add_student(students)
            case "addg" | "2":
                name_to_find = input("Type student name: ")
                students = add_grades(students, name_to_find)
            case "r" | "3":
                make_report(students)
            case "f" | "4":
                find_top_performer(students)
            case _:
                print("Unknown command, try again.")
                
    except Exception as error:
        print(f"Something went wrong: {error}")
