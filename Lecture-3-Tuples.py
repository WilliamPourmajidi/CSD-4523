# Tuples in Python

# 1. Creating a tuple
# Tuples are created using parentheses ()
fruits = ("apple", "cherry", "banana")
print(f"Initial tuple of fruits: {fruits}")

# 2. Accessing elements
# Tuple elements are accessed by their index, starting from 0
first_fruit = fruits[0]
print(f"First fruit: {first_fruit}")

last_fruit = fruits[-1]
print(f"Last fruit: {last_fruit}")

# 3. Slicing a tuple
# Tuples can be sliced to get a subset of elements
some_fruits = fruits[1:3]
print(f"Sliced tuple (from index 1 to 3 -- note that it gives us index 1 and 2, so 3 is not included! ): {some_fruits}")

# 4. Iterating through a tuple
# Tuples can be iterated over using a for loop
print("Looping through the tuple of fruits:")
for fruit in fruits:
    print(fruit)



# 5. Unpacking a tuple
# Tuples can be unpacked into individual variables
print(type(fruits))
(a, b, c) = fruits


print(f"Unpacked tuple: a = {a}, b = {b}, c = {c}")

# 6. Nested tuples
# Tuples can contain other tuples as elements
nested_tuple = (fruits, ("orange", "blueberry"))
print(f"Nested tuple: {nested_tuple}")

# 7. Immutable nature of tuples
# Tuples are immutable, meaning their elements cannot be changed after creation
# The following line would raise an error:
# fruits[0] = "watermelon"  # Uncommenting this line will cause a TypeError


# 8. Tuple methods
# Tuples have only two built-in methods: count() and index()

# Count occurrences of an element
apple_count = fruits.count("apple")
print(f"Number of times 'apple' appears in the tuple: {apple_count}")

# Find the index of an element
banana_index = fruits.index("banana")
print(f"Index of 'banana' in the tuple: {banana_index}")

# 9. Using tuples as dictionary keys
# Tuples can be used as keys in dictionaries because they are immutable
locations = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128, -74.0060): "New York",
    (48.8566, 2.3522): "Paris"
}
print(f"Dictionary with tuple keys: {locations}")

# Accessing value using tuple key
tokyo_location = locations[(35.6895, 139.6917)]
print(f"Location for (35.6895, 139.6917): {tokyo_location}")

# 10. Converting between lists and tuples
# Lists can be converted to tuples and vice versa
fruit_list = ["apple", "banana", "cherry"]
fruit_tuple = tuple(fruit_list)
print(f"Converted list to tuple: {fruit_tuple}")

# Convert a tuple back to a list
converted_list = list(fruit_tuple)
print(f"Converted tuple back to list: {converted_list}")
