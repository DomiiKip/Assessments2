def tuples_to_dict(tuples_list):
    result_dict = {}  # Initialize an empty dictionary
    for key, value in tuples_list:  # Iterate through each tuple in the list
        result_dict[key] = value  # Assign the key-value pair to the dictionary
    return result_dict  # Return the resulting dictionary

# Example usage
example_tuples = [("apple", 5), ("banana", 3), ("orange", 7)]
result = tuples_to_dict(example_tuples)
print(result)  # Output: {'apple': 5, 'banana': 3, 'orange': 7}