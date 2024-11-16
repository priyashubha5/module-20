# Take a number from the user
num = int(input("Enter a number: "))

# List comprehension to get all odd numbers up to 'num'
odd_numbers = [i for i in range(1, num) if i % 2 != 0]

# Print the result
print("List of odd numbers under the input value:", odd_numbers)

# List of fruits
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# List comprehension to capitalize the first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# Print the result
print("List of fruits with capitalized first letters:", capitalized_fruits)
