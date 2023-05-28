import string

filename = input("Enter the input filename: ")

try:
    with open(filename, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    # Create a dictionary to store the letter counts
    letter_counts = {}
    # Iterate over each character in the text
    for char in text:
        # Convert the character to lowercase
        char = char.lower()
        # Check if the character is a Latin letter
        if char in string.ascii_lowercase:
            # Increment the count for the letter
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Sort the letter counts by frequency in descending order
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # Create the output filename by adding the suffix '.hist'
    output_filename = filename + ".hist"

    # Write the histogram to the output file
    with open(output_filename, "w") as file:
        for letter, count in sorted_counts:
            file.write(f"{letter} -> {count}\n")

    # Print the histogram to the console
    for letter, count in sorted_counts:
        print(f"{letter} -> {count}")
