#Deep Copy Behaviour
import copy

# Original list with nested list
original_list = [1, 2, [3, 4]]

# Creating a deep copy
deep_copy = copy.deepcopy(original_list)

# Modifying the nested list in the original list
original_list[2][0] = '7'

print("Original List:", original_list)  # Output: [1, 2, ['7', 4]]
print("Deep Copy:", deep_copy)          # Output: [1, 2, [3, 4]]

