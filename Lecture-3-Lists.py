# # Lists in Python
#
# # 1. Creating a list
# # Lists are created using square brackets []
# fruits = ["apple", "banana", "cherry"]
# print(f"Initial list of fruits: {fruits}")
#
# # 2. Accessing elements
# # List elements are accessed by their index, starting from 0
# first_fruit = fruits[0]
# print(f"First fruit: {first_fruit}")
#
# # 3. Modifying elements
# # List elements can be modified by assigning a new value to an index
# fruits[1] = "grapefruit"
# print(f"Modified list of fruits: {fruits}")
#
# # 4. Adding elements
# # Elements can be added using the append() method
# fruits.append("orange")
# print(f"List after appending a new fruit: {fruits}")
#
# # Adding elements at a specific position using insert()
# fruits.insert(1, "elderberry")
# print(f"List after inserting a new fruit at index 1: {fruits}")
#
# # 5. Removing elements
# # Elements can be removed using the remove() method
# fruits.remove("cherry")
# print(f"List after removing 'cherry': {fruits}")
#
# # Elements can be removed using the pop() method, which removes the last item by default
# last_fruit = fruits.pop()
# print(f"Removed the last fruit: {last_fruit}")
# print(f"List after popping the last fruit: {fruits}")
#
# # Elements can be removed using pop() with an index
# second_fruit = fruits.pop(1)
# print(f"Removed the second fruit: {second_fruit}")
# print(f"List after popping the fruit at index 1: {fruits}")
#
# # 6. Slicing a list
# # Lists can be sliced to get a subset of elements
# some_fruits = fruits[0:4]
# print(f"Sliced list (from index 0 to 4): {some_fruits}")
# print("-----------")
#
# # 7. Looping through a list
# # Lists can be iterated over using a for loop
# print("Looping through the list of fruits:")
# for item in fruits:
#     print(item)
# # Lists in Python
#
# # 1. Creating a list
# # Lists are created using square brackets []
# fruits = ["apple", "banana", "cherry"]
# print(f"Initial list of fruits: {fruits}")
#
# # 2. Accessing elements
# # List elements are accessed by their index, starting from 0
# first_fruit = fruits[0]
# print(f"First fruit: {first_fruit}")
#
# # 3. Modifying elements
# # List elements can be modified by assigning a new value to an index
# fruits[1] = "grapefruit"
# print(f"Modified list of fruits: {fruits}")
#
# # 4. Adding elements
# # Elements can be added using the append() method
# fruits.append("orange")
# print(f"List after appending a new fruit: {fruits}")
#
# # Adding elements at a specific position using insert()
# fruits.insert(1, "elderberry")
# print(f"List after inserting a new fruit at index 1: {fruits}")
#
# # 5. Removing elements
# # Elements can be removed using the remove() method
# fruits.remove("cherry")
# print(f"List after removing 'cherry': {fruits}")
#
# # Elements can be removed using the pop() method, which removes the last item by default
# last_fruit = fruits.pop()
# print(f"Removed the last fruit: {last_fruit}")
# print(f"List after popping the last fruit: {fruits}")
#
# # Elements can be removed using pop() with an index
# second_fruit = fruits.pop(1)
# print(f"Removed the second fruit: {second_fruit}")
# print(f"List after popping the fruit at index 1: {fruits}")
#
# # 6. Slicing a list
# # Lists can be sliced to get a subset of elements
# some_fruits = fruits[0:4]
# print(f"Sliced list (from index 0 to 4): {some_fruits}")
# print("-----------")
#
# # 7. Looping through a list
# # Lists can be iterated over using a for loop
# print("Looping through the list of fruits:")
# for item in fruits:
#     print(item)

# 8. List comprehension
# List comprehension provides a concise way to create lists
squares = [x**2 for x in range(5)]
print(f"List of squares using list comprehension: {squares}")


