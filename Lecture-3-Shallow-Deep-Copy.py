original_list = [1, 2, [3, 4]]
shallow_copy_1 = original_list.copy()


original_list = [1, 2, [3, 4]]
shallow_copy_2 = original_list[:]


#Shallow Copy Behaviour

# Original list with nested list
original_list = [1, 2, [3, 4]]

# Creating a shallow copy
shallow_copy = original_list.copy()

# Modifying the nested list in the original list
original_list[2][0] = 'changed'

print("Original List:", original_list)  # Output: [1, 2, ['changed', 4]]
print("Shallow Copy:", shallow_copy)    # Output: [1, 2, ['changed', 4]]

#Deep Copy Behaviour
import copy

# Original list with nested list
original_list = [1, 2, [3, 4]]

# Creating a deep copy
deep_copy = copy.deepcopy(original_list)

# Modifying the nested list in the original list
original_list[2][0] = 'changed'

print("Original List:", original_list)  # Output: [1, 2, ['changed', 4]]
print("Deep Copy:", deep_copy)          # Output: [1, 2, [3, 4]]

