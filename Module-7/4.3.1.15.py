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

    # Print the histogram in alphabetical order
    for letter in sorted(letter_counts):
        print(f"{letter} -> {letter_counts[letter]}")
