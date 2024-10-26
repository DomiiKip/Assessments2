def remove_duplicates(input_list):
    unique_list = []  # Initialize an empty list to hold unique elements
    for item in input_list:  # Loop through each item in the input list
        if item not in unique_list:  # Check if the item is not already in the unique list
            unique_list.append(item)  # Add the item to the unique list if it's not a duplicate
    return unique_list  # Return the list of unique elements

# Example usage
example_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(example_list)
print(result)  # Output: [1, 2, 3, 4, 5]