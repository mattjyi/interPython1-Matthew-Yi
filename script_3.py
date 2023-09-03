# Define the function which takes a string
def count_letter(string):
    # Convers the string to lowercase
    string = string.lower()

    # Replace occurences of an empty string with another empty string
    # Removes all spaces from the inputted string
    string = string.replace("","")

    # Initialize an empty dictionary to store the frequency of each letter
    keep_count = {}

    # Repeat through each character in the string
    for i in string:
        # See if 'i' is used in keep_count
        if i in keep_count:
           # If it does exist, increase count by i
            keep_count[i] += 1
        else:
            # If it doesn't exist, initialize the count to 1
            keep_count[i] = 1
    # Return the keep_count
    return keep_count

# Define string with "hello world"
string = "hello world"

# Print the result
print(count_letter(string))