def sum_of_numbers(nums):
    total = 0  # Initialize a variable to hold the sum
    for num in nums:  # Loop through each number in the list
        total += num  # Add the current number to the total
    return total  # Return the final sum

# Given list
nums = [1, 2, 3, 4, 5]

# Call the function and print the result
result = sum_of_numbers(nums)
print(f"The sum of the numbers in the list is: {result}")