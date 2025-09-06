# AI-MLOps-python

Type casting in Python, also known as type conversion, refers to the process of converting a value from one data type to another. This can be either implicit (automatic by Python) or explicit (manual conversion using built-in functions).
Importance of Type Casting: Type casting is crucial for:
• Data manipulation:
Ensuring data is in the correct format for operations (e.g., performing arithmetic on numbers that were initially strings from user input).
• Preventing errors:
Avoiding TypeError exceptions when operations require specific data types.
• User input handling:
Converting user input, which is typically received as strings, into appropriate data types for processing.
• Flexibility:
Adapting to different data types within a program and integrating them seamlessly.

1. Implicit Type Conversion:
Python automatically converts one data type to another in certain situations to avoid data loss or to perform operations between different types. For example, when an integer is added to a float, Python implicitly converts the integer to a float before performing the addition, and the result will be a float.
num_int = 10
num_float = 5.5
result = num_int + num_float  # num_int is implicitly converted to float
print(result)
print(type(result))

2. Explicit Type Conversion (Type Casting):
Explicit type casting involves using built-in functions to manually convert a value to a specific data type. Common functions for explicit type casting include:
• int(): Converts a value to an integer. If converting a float, it truncates the decimal part. If converting a string, the string must represent a valid integer.
• float(): Converts a value to a floating-point number.
• str(): Converts a value to a string.
• bool(): Converts a value to a boolean. Non-zero numbers, non-empty strings, lists, tuples, and dictionaries evaluate to True. Zero, empty strings, lists, tuples, and dictionaries evaluate to False.

# Convert float to int
float_num = 10.7
int_num = int(float_num)
print(f"Float to int: {int_num}, type: {type(int_num)}")

# Convert string to int
str_num = "123"
converted_int = int(str_num)
print(f"String to int: {converted_int}, type: {type(converted_int)}")

# Convert int to float
int_val = 20
float_val = float(int_val)
print(f"Int to float: {float_val}, type: {type(float_val)}")

# Convert int to string
num_to_str = 456
str_val = str(num_to_str)
print(f"Int to string: {str_val}, type: {type(str_val)}")

# Convert to boolean
truthy_val = bool(1)
falsy_val = bool(0)
empty_string_bool = bool("")
non_empty_string_bool = bool("hello")
print(f"1 to bool: {truthy_val}")
print(f"0 to bool: {falsy_val}")
print(f"Empty string to bool: {empty_string_bool}")
print(f"Non-empty string to bool: {non_empty_string_bool}")

