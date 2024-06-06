# nested_list = [1, 2, "String", 3.14, ["a", "b", "c", "d"]]
#
# for element in nested_list:
#     print(f"element in the list is {element}, and its type is {type(element)}")
# ------------------------------
# Nested Loops
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i*j)
# --------------------
# Number of rows and columns in the multiplication table
n = 10

# Using nested loops to print a multiplication table
for i in range(1, n + 1):
    # print("-------Outer Loop-------")
    for j in range(1, n + 1):
        # print("-------Inner Loop-------")
        print(f"{i * j}\t", end='')  # Multiplying and formatting the output
    print()  # New line after each row
