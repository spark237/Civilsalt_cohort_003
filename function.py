# 1. Function to greet a user
def greet_user(name):
    print(f"Welcome, {name}!")

# 2. Function to calculate area
def calculate_area(length, width):
    return length * width

# 3. Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# --- Test Calls (Optional for practice) ---
name = input("Enter your name: ")
greet_user(name)
# -- area
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
print("Area:", calculate_area(length, width))

number = int(input("Enter a number: "))
print(f"Is {number} even?", is_even(number))
