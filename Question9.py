def has_pair_with_sum(input_list, target_sum):
    seen_numbers = set()  # Initialize an empty set to store seen numbers
    for number in input_list:  # Iterate through each number in the list
        complement = target_sum - number  # Calculate the complement
        if complement in seen_numbers:  # Check if the complement is in the set
            return True  # If found, return True
        seen_numbers.add(number)  # Add the current number to the set
    return False  # If no pair is found, return False

# Example usage
example_list = [1, 2, 3, 4, 5]
target = 9
result = has_pair_with_sum(example_list, target)
print(result)  # Output: False

target = 7
result = has_pair_with_sum(example_list, target)
print(result)  # Output: True