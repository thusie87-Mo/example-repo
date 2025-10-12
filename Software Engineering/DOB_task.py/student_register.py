# student_register.py

def register_students():
    try:
        num_students = int(input("How many students are registering? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    with open("reg_form.txt", "w") as file:
        for i in range(num_students):
            student_id = input(f"Enter student ID for student {i + 1}: ")
            file.write(f"{student_id}\n{'-' * 30}\n")

    print(f"\nRegistration complete. {num_students} student(s) added to reg_form.txt.")

if __name__ == "__main__":
    register_students()
