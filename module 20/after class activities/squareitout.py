def separate_square_odd_even(start, end):
    # Create a list of square values in the specified range
    squares = [i**2 for i in range(start, end + 1)]
    
    # Separate the squares into odd and even values
    even_squares = [square for square in squares if square % 2 == 0]
    odd_squares = [square for square in squares if square % 2 != 0]
    
    # Print the results
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

# Example usage
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))
separate_square_odd_even(start_range, end_range)
