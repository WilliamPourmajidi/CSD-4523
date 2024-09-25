# Lists in Python

# 1. Creating a list
# Lists are created using square brackets []
fruit = "apple"
fruits = ["apple", "banana", "cherry"]
print(type(fruits))
print(f"Initial list of fruits: {fruits}")

# # 2. Accessing elements
# # List elements are accessed by their index, starting from 0

first_fruit = fruits[0]
second_fruit = fruits[1]
third_fruit = fruits[2]

print(f"First fruit: {first_fruit}")
print(f"Second fruit: {second_fruit}")
print(f"Third fruit: {third_fruit}")

# 3. Modifying elements
# List elements can be modified by assigning a new value to an index
fruits[1] = "grapefruit"
print(f"Modified list of fruits: {fruits}")

# 4. Adding elements
#  Elements can be added using the append() method
fruits.append("orange")
print(f"List after appending a new fruit: {fruits}")

# Adding elements at a specific position using insert()
fruits.insert(1, "elderberry")
print(f"List after inserting a new fruit at index 1: {fruits}")

# 5. Removing elements
# Elements can be removed using the remove() method
fruits.remove("cherry")
print(f"List after removing 'cherry': {fruits}")
print(f'List after removing "cherry": {fruits}')
#
# Elements can be removed using the pop() method, which removes the last item by default
last_fruit = fruits.pop()
print(f"Removed the last fruit: {last_fruit}")
print(f"List after popping the last fruit: {fruits}")
#
# Elements can be removed using pop() with an index
second_fruit = fruits.pop(1)
print(f"Removed the second fruit: {second_fruit}")
print(f"List after popping the fruit at index 1: {fruits}")

# 6. Slicing a list
# Lists can be sliced to get a subset of elements
my_new_fruits = ["apple", "banana", "cherry", "orange", "grapefruit", "strawberry", "blueberry", "kiwi"]
# important note: the starting index is inclusive and the ending index is exclusive
some_fruits = my_new_fruits[1:3]
print(f"Sliced list {some_fruits}")

# 7. Looping through a list
# Lists can be iterated over using a for loop
print("Looping through the list of fruits:")
for fruit in my_new_fruits:
    print(fruit)


interesting_list = ["William", "Pourmajidi", 42, 3.14]
for item in interesting_list:
    print(f"Here is our item {item} and is of type {type(item)}")
