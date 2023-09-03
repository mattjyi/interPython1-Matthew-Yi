# Define a function that uses the argument my_list
def get_unique_list(my_list):
    # Initialize empty list to store variables
    unique_list = []

    # Repeat throught each variable in the input list
    for i in my_list:
        # See if element 'i' is in unique list
        if i not in unique_list:
            # If not, append to uniq.list
            unique_list.append(i)
    # Return the unique list with the elements
    return unique_list

my_list = [1,2,3,2,1,4]
unique_list = get_unique_list(my_list)
print(unique_list)