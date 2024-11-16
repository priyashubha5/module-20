# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:", test_dict)

# Ask the user to enter a value to check for frequency
value_to_check = int(input("Enter the value for which you want to check the frequency: "))

# Find and print the frequency of the specified value
frequency = list(test_dict.values()).count(value_to_check)
print(f"The frequency of value {value_to_check} is: {frequency}")
