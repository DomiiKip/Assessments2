def find_largest_number(num_tuple):
    largest = num_tuple[0]  # Start by assuming the first number is the largest
    for num in num_tuple:  # Loop through each number in the tuple
        if num > largest:  # Check if the current number is larger than the current largest
            largest = num  # Update largest if the current number is greater
    return largest  # Return the largest number found

# Example usage
example_tuple = (10, 20, 30, 40, 50)
result = find_largest_number(example_tuple)
print(f"The largest number in the tuple is: {result}")