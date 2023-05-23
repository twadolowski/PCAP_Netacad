# Define the LED patterns for each digit (0-9)
digits = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]


def display_number(number):
    # Convert the number to a string
    number_str = str(number)

    # Initialize an empty list to store the LED representation of the number
    display = [[] for _ in range(5)]

    # Generate the LED representation for each digit
    for digit in number_str:
        digit_int = int(digit)
        digit_led = digits[digit_int]

        # Add each row of the digit to the display
        for i in range(5):
            display[i].append(digit_led[i])

    # Display the LED representation of the number
    for row in display:
        print(" ".join(row))


# Prompt the user for a number
number = int(input("Enter a non-negative integer: "))

# Display the number using LED representation
display_number(number)
