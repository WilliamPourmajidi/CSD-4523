# Lists in Python

# 1. Creating a list
# Lists are created using square brackets []
fruits = ["apple", "banana", "cherry"]
print(f"Initial list of fruits: {fruits}")

# 2. Accessing elements
# List elements are accessed by their index, starting from 0
first_fruit = fruits[0]
print(f"First fruit: {first_fruit}")

# 3. Modifying elements
# List elements can be modified by assigning a new value to an index
fruits[1] = "blueberry"
print(f"Modified list of fruits: {fruits}")

# 4. Adding elements
# Elements can be added using the append() method
fruits.append("date")
print(f"List after appending a new fruit: {fruits}")

# Adding elements at a specific position using insert()
fruits.insert(1, "elderberry")
print(f"List after inserting a new fruit at index 1: {fruits}")

# 5. Removing elements
# Elements can be removed using the remove() method
fruits.remove("cherry")
print(f"List after removing 'cherry': {fruits}")

# Elements can be removed using the pop() method, which removes the last item by default
last_fruit = fruits.pop()
print(f"Removed the last fruit: {last_fruit}")
print(f"List after popping the last fruit: {fruits}")

# Elements can be removed using pop() with an index
second_fruit = fruits.pop(1)
print(f"Removed the second fruit: {second_fruit}")
print(f"List after popping the fruit at index 1: {fruits}")

# 6. Slicing a list
# Lists can be sliced to get a subset of elements
some_fruits = fruits[1:3]
print(f"Sliced list (from index 1 to 3): {some_fruits}")

# 7. Looping through a list
# Lists can be iterated over using a for loop
print("Looping through the list of fruits:")
for fruit in fruits:
    print(fruit)

# 8. List comprehension
# List comprehension provides a concise way to create lists
squares = [x**2 for x in range(5)]
print(f"List of squares using list comprehension: {squares}")

# 9. List methods
# Lists have several built-in methods for various operations

# Count occurrences of an element
apple_count = fruits.count("apple")
print(f"Number of times 'apple' appears in the list: {apple_count}")

# Find the index of an element
banana_index = fruits.index("banana")
print(f"Index of 'banana' in the list: {banana_index}")

# Sort the list
fruits.sort()
print(f"List after sorting: {fruits}")

# Reverse the list
fruits.reverse()
print(f"List after reversing: {fruits}")

# Clear the list
fruits.clear()
print(f"List after clearing all elements: {fruits}")

# 10. Copying a list
# Lists can be copied using the copy() method or slicing
original_list = ["a", "b", "c"]
shallow_copy = original_list.copy()
print(f"Original list: {original_list}")
print(f"Shallow copy of the list: {shallow_copy}")

# Modify the original list and show that the copy is unaffected
original_list.append("d")
print(f"Original list after appending a new element: {original_list}")
print(f"Shallow copy remains unchanged: {shallow_copy}")


