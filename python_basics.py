# Python Basics Tutorial
# A comprehensive introduction to Python programming

def print_section_header(title):
    """Helper function to print formatted section headers"""
    print("\n" + "=" * 50)
    print(f" {title} ".center(50, "*"))
    print("=" * 50 + "\n")

# ===== INTRODUCTION TO PYTHON EXPRESSIONS =====
print_section_header("INTRODUCTION TO PYTHON EXPRESSIONS")

print("Basic arithmetic operations:")
print(f"Addition: 5 + 3 = {5 + 3}")
print(f"Subtraction: 10 - 4 = {10 - 4}")
print(f"Multiplication: 6 * 7 = {6 * 7}")
print(f"Division: 20 / 5 = {20 / 5}")
print(f"Integer Division: 20 // 3 = {20 // 3}")
print(f"Modulus (remainder): 20 % 3 = {20 % 3}")
print(f"Exponentiation: 2 ** 3 = {2 ** 3}")

print("\nVariable assignment and expressions:")
x = 10
y = 5
print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")
print(f"x * y = {x * y}")

print("\nString operations:")
first_name = "Python"
last_name = "Programming"
print(f"Concatenation: {first_name} + ' ' + {last_name} = {first_name + ' ' + last_name}")
print(f"Repetition: 'Python' * 3 = {'Python' * 3}")
print(f"String length: len('Python') = {len('Python')}")

# ===== LISTS AND STATEMENTS =====
print_section_header("LISTS AND STATEMENTS")

print("Creating and accessing lists:")
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slicing: fruits[1:3] = {fruits[1:3]}")

print("\nModifying lists:")
fruits.append("mango")
print(f"After append: {fruits}")
fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")
fruits.remove("cherry")
print(f"After remove: {fruits}")
popped_fruit = fruits.pop()
print(f"Popped fruit: {popped_fruit}")
print(f"After pop: {fruits}")

print("\nList operations:")
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
print(f"Concatenation: {numbers} + {more_numbers} = {numbers + more_numbers}")
print(f"Repetition: {numbers} * 2 = {numbers * 2}")
print(f"Length: len({numbers}) = {len(numbers)}")
print(f"Sum: sum({numbers}) = {sum(numbers)}")
print(f"Min: min({numbers}) = {min(numbers)}")
print(f"Max: max({numbers}) = {max(numbers)}")

print("\nList comprehensions:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers from 1-10: {even_numbers}")

# ===== DICTIONARIES =====
print_section_header("DICTIONARIES")

print("Creating and accessing dictionaries:")
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}
print(f"Person dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"First skill: {person['skills'][0]}")

print("\nModifying dictionaries:")
person["email"] = "john@example.com"
print(f"After adding email: {person}")
person["age"] = 31
print(f"After updating age: {person}")
del person["city"]
print(f"After deleting city: {person}")

print("\nDictionary methods:")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")
print(f"Get with default: {person.get('phone', 'Not available')}")

print("\nDictionary comprehensions:")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# ===== LOOPS AND CONTROL FLOW =====
print_section_header("LOOPS AND CONTROL FLOW")

print("If-elif-else statements:")
x = 15
if x < 10:
    result = "less than 10"
elif x < 20:
    result = "between 10 and 20"
else:
    result = "20 or greater"
print(f"x = {x}, result = '{result}'")

print("\nFor loops:")
print("Iterating through a list:")
for fruit in fruits[:3]:
    print(f"  - {fruit}")

print("\nIterating with range:")
for i in range(3):
    print(f"  - Index {i}")

print("\nWhile loops:")
count = 0
while count < 3:
    print(f"  - Count is {count}")
    count += 1

print("\nBreak and continue:")
for i in range(5):
    if i == 2:
        print(f"  - Skipping {i}")
        continue
    if i == 4:
        print(f"  - Breaking at {i}")
        break
    print(f"  - Processing {i}")

# ===== FUNCTIONS =====
print_section_header("FUNCTIONS")

print("Basic function definition:")
def greet(name):
    return f"Hello, {name}!"

print(f"greet('Alice') = {greet('Alice')}")

print("\nDefault parameters:")
def greet_with_time(name, time_of_day="morning"):
    return f"Good {time_of_day}, {name}!"

print(f"greet_with_time('Bob') = {greet_with_time('Bob')}")
print(f"greet_with_time('Charlie', 'evening') = {greet_with_time('Charlie', 'evening')}")

print("\nVariable number of arguments:")
def sum_all(*args):
    return sum(args)

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40) = {sum_all(10, 20, 30, 40)}")

print("\nKeyword arguments:")
def build_profile(first, last, **kwargs):
    profile = {"first_name": first, "last_name": last}
    profile.update(kwargs)
    return profile

profile = build_profile("John", "Doe", age=30, occupation="Developer")
print(f"Profile: {profile}")

print("\nLambda functions:")
double = lambda x: x * 2
print(f"double(5) = {double(5)}")

numbers = [1, 2, 3, 4, 5]
even_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers in {numbers}: {even_filter}")

doubled_map = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers in {numbers}: {doubled_map}")

# ===== INFORMATION FLOW =====
print_section_header("INFORMATION FLOW")

print("Function composition:")
def get_length(text):
    return len(text)

def is_long_text(length):
    return length > 10

text = "Hello, Python Programming!"
length = get_length(text)
is_long = is_long_text(length)

print(f"Text: '{text}'")
print(f"Length: {length}")
print(f"Is long text? {is_long}")

print("\nError handling with try-except:")
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"
    finally:
        print("  - Division operation attempted")

print(f"divide(10, 2) = {divide(10, 2)}")
print(f"divide(10, 0) = {divide(10, 0)}")

print("\nFile handling:")
# Writing to a file (this is just a demonstration)
print("Writing to a file (demonstration):")
print("  with open('example.txt', 'w') as file:")
print("      file.write('Hello, Python!')")

# Reading from a file (this is just a demonstration)
print("\nReading from a file (demonstration):")
print("  with open('example.txt', 'r') as file:")
print("      content = file.read()")
print("      print(content)")

print("\nModules and imports (demonstration):")
print("  import math")
print("  print(math.pi)")
print("  print(math.sqrt(16))")

print("\nThis concludes our Python basics tutorial!")