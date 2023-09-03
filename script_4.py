# Initialize variable to store integers
total = 0
# Iterate from 1 to 5 in the loop
for i in range(1,6):
    # Repeadetly prompts the user for an imput
    while True:
        try:
            # Prompt the user to enter an integer and store it
            user_int = int(input("Enter int #{}: " .format(i)))
            # Add the integer to the total variable
            total += user_int
            # Exit the loop if a valid integer was entered
            break
        except ValueError:
            # If the user enters a non-integer value, display an Error message
            print("Invalid input. Pease enter an int.")
            # Continue to ask the prompt until integer is inputted
            continue

# Display the total 
print("Your sum is ", total)