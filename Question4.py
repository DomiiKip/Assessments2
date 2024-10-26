def reverse_strings(string_list):
    reversed_list = []  # Initialize an empty list to hold the reversed strings
    for string in string_list:  # Loop through each string in the input list
        reversed_list.append(string[::-1])  # Reverse the string and add it to the new list
    return reversed_list  # Return the list of reversed strings

# Example usage
input_list = ["apple", "banana", "cherry"]
result = reverse_strings(input_list)
print(result)  # Output: ['elppa', 'ananab', 'yrrehc']