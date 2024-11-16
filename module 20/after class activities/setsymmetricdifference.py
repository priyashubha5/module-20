def find_symmetric_difference(set1, set2):
    # Calculate the symmetric difference
    symmetric_diff = set1.symmetric_difference(set2)
    return symmetric_diff

# Given sets
set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}

set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}

# Find and print symmetric differences
print("Symmetric Difference of Set1_a and Set2_a:", find_symmetric_difference(set1_a, set2_a))
print("Symmetric Difference of Set1_b and Set2_b:", find_symmetric_difference(set1_b, set2_b))
