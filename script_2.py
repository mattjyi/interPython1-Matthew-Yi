# Return combined_dict with variables new dict 
def get_combined_dict(my_dict_1, my_dict_2): 
    new_dict = {} # Empty dictionalry to store values 

    # Iterate the pairs in my_dict_1
    for key, value in my_dict_1.items():
        # Check if the values exist in my_dict_2
        if (key in my_dict_2.keys()):
            # If the values match then store the value in new_dict
            new_dict[key] = value + my_dict_2[key]
        #Return new_dict with the results
        return new_dict
# Declare values to my_dict_1 and my_dict 2 
my_dict_1 = {'a' : 5, 'b' : 12, 'c' : 3, 'd' : 9}
my_dict_2 = {'b' : 4, 'c' : 9, 'd' : 10, 'e' : 16}
# Call get_combined_dict with my_dict_1 and my_dict_2 and store the result in comined_dict 
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
# Print the combined_dict
print(combined_dict)