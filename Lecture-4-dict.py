### Dictionary
my_dict = {'name': 'Alice', 'age': 25}
# Accessing Values:
age = my_dict['age']  # Outputs: 25
# Modifying Dictionaries:
my_dict['age'] = 26  # Updates age to 26

# Dictionary Operations in Python
# 1. Creating a dictionary
# Create a dictionary with initial key-value pairs


student = {
    "id": 1,
    "name": "Alice Johnson",
    "age": 20,
    "grades": {
        "math": 90,
        "science": 85,
        "literature": 88
    },
    "attendance": ["2023-01-10", "2023-01-11", "2023-01-12"]
}
print("Initial dictionary:")
print(student)
# Output:
# {'id': 1, 'name': 'Alice Johnson', 'age': 20, 'grades': {'math': 90, 'science': 85, 'literature': 88},
# 'attendance': ['2023-01-10', '2023-01-11', '2023-01-12']}

# 2. Accessing elements
# Access values using keys
name = student["name"]
print(f"Student's name: {name}")
# Output: Student's name: Alice Johnson


math_grade = student["grades"]["math"]
print(f"Math grade: {math_grade}")
# Output: Math grade: 90

# 3. Modifying elements
# Modify values using keys
student["age"] = 21
print("Updated age:")
print(student["age"])
# Output: 21

student["grades"]["science"] = 87
print("Updated science grade:")
print(student["grades"]["science"])
# Output: 87

# 4. Adding elements
# Add new key-value pairs
student["email"] = "alice.johnson@mycollege.com"
print("Added email:")
print(student["email"])
# Output: alice.johnson@mycollege.com

student["grades"]["history"] = 92
print("Added history grade:")
print(student["grades"]["history"])
# Output: 92

# 5. Removing elements
# Remove key-value pairs using pop()
# Let's print our dictionary so we see what we have so far

print("--before------------")
print(student)
print("-------------------")

removed_age = student.pop("age")
print("Removed age")
print(f"Removed age {removed_age}")


removed_email = student.pop("email")
print("Removed email:")
print(removed_email)
print("--after-------------")
print(student)
print("-------------------")


# Remove key-value pairs using del
del student["grades"]["literature"]
print("Removed literature grade:")
print(student["grades"])
# Output: {'math': 90, 'science': 87, 'history': 92}

# 6. Iterating over a dictionary
# Iterate over keys
print("Keys in the dictionary:")
for key in student:
    print(key)
# Output:
# id
# name
# grades
# attendance

# Iterate over values
print("Values in the dictionary:")
for value in student.values():
    print(value)
# Output:
# 1
# Alice Johnson
# {'math': 90, 'science': 87, 'history': 92}
# ['2023-01-10', '2023-01-11', '2023-01-12']

# Iterate over key-value pairs
print("Key-value pairs in the dictionary:")
for key, value in student.items():
    print(f"Here is the key: {key} and its value is {value}")
# Output:
# id: 1
# name: Alice Johnson
# grades: {'math': 90, 'science': 87, 'history': 92}
# attendance: ['2023-01-10', '2023-01-11', '2023-01-12']

# 7. Checking for existence of keys
# Check if a key exists using 'in'
print("Checking for keys:")
print("name" in student)  # Output: True
print("age" in student)   # Output: False

# 8. Dictionary methods
# Get value with default using get()
email = student.get("email", "No email provided")
print("Email using get():")
print(email)
# Output: No email provided

# Update dictionary with another dictionary
additional_info = {"phone": "123-456-7890", "address": "123 Main St"}
student.update(additional_info)
print("Updated dictionary with additional info:")
print(student)
# Output:
# {'id': 1, 'name': 'Alice Johnson', 'grades': {'math': 90, 'science': 87, 'history': 92}, 'attendance': ['2023-01-10', '2023-01-11', '2023-01-12'], 'phone': '123-456-7890', 'address': '123 Main St'}

# Clear all elements from the dictionary
student.clear()
print("Cleared dictionary:")
print(student)
# Output: {}



