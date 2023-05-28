class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


filename = input("Enter the input filename: ")

try:
    with open(filename, "r") as file:
        text = file.read()
except FileNotFoundError:
    raise StudentsDataException("File not found.")
except IOError:
    raise StudentsDataException("Error reading file.")
else:
    if not text:
        raise FileEmpty("File is empty.")

    # Create a dictionary to store the student data
    student_data = {}
    # Iterate over each line in the text
    for line in text.splitlines():
        # Split the line into first name, last name, and points
        try:
            first_name, last_name, points = line.split()
            points = float(points)
        except ValueError:
            raise BadLine(f"Bad line: {line}")
        # Combine the first name and last name into a single key
        name = f"{first_name} {last_name}"
        # Increment the total points for the student
        student_data[name] = student_data.get(name, 0) + points

    # Sort the student data by name
    sorted_data = sorted(student_data.items())

    # Print the report
    for name, total_points in sorted_data:
        print(f"{name}\t{total_points}")
