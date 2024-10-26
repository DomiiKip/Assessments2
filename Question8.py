def keys_greater_than_n(input_dict, n):
    result_keys = []  # Initialize an empty list to store the keys
    for key, value in input_dict.items():  # Iterate through the dictionary items
        if value > n:  # Check if the value is greater than n
            result_keys.append(key)  # Add the key to the result list if the condition is met
    return result_keys  # Return the list of keys

# Example usage
example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
result = keys_greater_than_n(example_dict, n)
print(result)  # Output: ['a', 'b']