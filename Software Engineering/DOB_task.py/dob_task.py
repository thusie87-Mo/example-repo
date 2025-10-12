
# dob_task.py

def read_dob_file(filename):
    names = []
    birthdates = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 4:
                    # Join name and birthdate parts with spaces
                    name = ' '.join(parts[:-3])
                    birthdate = ' '.join(parts[-3:])
                    names.append(name)
                    birthdates.append(birthdate)
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    # Print names
    print("Name")
    for name in names:
        print(name)

    print("\nBirthdate")
    for date in birthdates:
        print(date)

# Run the function only if this script is executed directly
if __name__ == "__main__":
    read_dob_file("DOB.txt")
