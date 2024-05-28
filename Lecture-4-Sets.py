# Set Operations in Python

# 1. Creating a set
# Sets are created using curly braces {}
fruits = {"apple", "banana", "cherry"}
print("Initial set of fruits:")
print(fruits)
# Output: {'apple', 'banana', 'cherry'}

# 2. Adding elements
# Add an element using add()
fruits.add("date")
print("Set after adding 'date':")
print(fruits)
# Output: {'apple', 'banana', 'cherry', 'date'}

# Adding multiple elements using update()
fruits.update(["elderberry", "fig", "grape"])
print("Set after adding multiple elements:")
print(fruits)
# Output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'}

# 3. Removing elements
# Remove an element using remove()
fruits.remove("banana")
print("Set after removing 'banana':")
print(fruits)
# Output: {'apple', 'cherry', 'date', 'elderberry', 'fig', 'grape'}

# Remove an element using discard()
fruits.discard("fig")
print("Set after discarding 'fig':")
print(fruits)
# Output: {'apple', 'cherry', 'date', 'elderberry', 'grape'}

# Remove a random element using pop()
removed_element = fruits.pop()
print(f"Removed element: {removed_element}")
print("Set after popping an element:")
print(fruits)
# Output: (Removed element varies)
# Set after popping an element: {'cherry', 'date', 'elderberry', 'grape'}

# 4. Checking for membership
# Check if an element is in the set using 'in'
print("Checking for membership:")
print("apple" in fruits)  # Output: True
print("banana" in fruits)  # Output: False

# 5. Set operations
# Union of sets using union() or |
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "date", "elderberry"}
union_set = set1.union(set2)
print("Union of set1 and set2:")
print(union_set)
# Output: {'apple', 'banana', 'cherry', 'date', 'elderberry'}

# Intersection of sets using intersection() or &
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:")
print(intersection_set)
# Output: {'cherry'}

# Difference of sets using difference() or -
difference_set = set1.difference(set2)
print("Difference of set1 and set2 (set1 - set2):")
print(difference_set)
# Output: {'apple', 'banana'}

# Symmetric difference of sets using symmetric_difference() or ^
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:")
print(symmetric_difference_set)
# Output: {'apple', 'banana', 'date', 'elderberry'}

# 6. Iterating over a set
print("Iterating over the set of fruits:")
for fruit in fruits:
    print(fruit)
# Output: (Each element in the set will be printed, order may vary)

# 7. Copying a set
# Create a shallow copy of a set using copy()
fruits_copy = fruits.copy()
print("Shallow copy of the set:")
print(fruits_copy)
# Output: {'cherry', 'date', 'elderberry', 'grape'}

# 8. Clearing a set
# Remove all elements from the set using clear()
fruits.clear()
print("Set after clearing all elements:")
print(fruits)
# Output: set()
