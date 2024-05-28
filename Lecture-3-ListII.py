
# 1. Creating a list
# Lists are created using square brackets []
fruits = ["apple","orange","grape", "banana", "cherry","apple","apple"]
print(f"Initial list of fruits: {fruits}")


# # 9. List methods
# Lists have several built-in methods for various operations

# Count occurrences of an element
apple_count = fruits.count("apple")
print(f"Number of times 'apple' appears in the list: {apple_count}")
#
# # Find the index of an element
banana_index = fruits.index("banana")
print(f'Index of "banana" in the list: {banana_index}')
#
# # Sort the list
fruits.sort()
print(f"List after sorting: {fruits}")

# # Reverse the list
fruits.reverse()
print(f"List after reversing: {fruits}")
#
# Clear the list
fruits.clear()
print(f"List after clearing all elements: {fruits}")

# 10. Copying a list
# Lists can be copied using the copy() method or slicing
original_list = ["a", "b", "c"]
shallow_copy = original_list.copy()
print(f"Original list: {original_list}")
print(f"Shallow copy of the list: {shallow_copy}")
print("===========")
original_list = original_list.pop()
print("my original list",original_list)
print(f"Shallow copy of the original list: {shallow_copy}")


# # Modify the original list and show that the copy is unaffected
original_list.append("d")
print(f"Original list after appending a new element: {original_list}")
print(f"Shallow copy remains unchanged: {shallow_copy}")



Java Script Object Notation (JSON)

{"Name":"William",
 "age":}
