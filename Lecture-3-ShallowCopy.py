original_list = [1, 2, [3, 4]]
shallow_copy = original_list.copy()  # Creating a shallow copy

# Modifying the nested list in the original list
original_list[2][0] = 'new value'

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)