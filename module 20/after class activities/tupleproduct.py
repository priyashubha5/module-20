from functools import reduce

def calculate_product(tup):
    # Use reduce to multiply all elements in the tuple
    product = reduce(lambda x, y: x * y, tup)
    return product

# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate and print the products
print("Product of tup1:", calculate_product(tup1))
print("Product of tup2:", calculate_product(tup2))
