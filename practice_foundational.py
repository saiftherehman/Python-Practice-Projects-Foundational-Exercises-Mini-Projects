#DAY 1 — Strengthening Your Python Foundations

# Exercise 1 — Temperature Converter
# Convert Celsius ↔ Fahrenheit using functions.

print("Select the number to convert the temperature")
print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")

choose = int(input("Enter the number to convert the temperature"))

if choose == 1:
    f = float(input("Enter the temperature to convert: "))
    c = (f - 32) * 5/9
    print(f"{f}°F is equal to {c}°C.")
elif choose == 2:
    c = float(input("Enter the temperatre to convert: "))
    f = (c * 9/5) + 32
    print(f"{c}°C is equal to {f}°F.")

#----------------------------------------------------------------------------------------------

#Exercise 2 — List Processor
# Given a list of numbers:
# find max
# find min
# calculate sum
# calculate average

my_list = [73, 12, 58, 91, 4, 39, 67, 25, 84, 10]
max_num = max(my_list)
min_num = min(my_list)
sum_num = sum(my_list)
avg_num = sum_num/len(my_list)

print(f"Maximum number = {max_num}")
print(f"Minimum Number = {min_num}")
print(f"Sum of the list = {sum_num}")
print(f"Average number = {avg_num}")

#-----------------------------------------------------------------------------------------

#Exercise 3 — String Formatter
# Take a user’s name and return:
# uppercase
# lowercase
# reversed
# initials

user_name = input("Enter your name: ")
print("Uppercase = ",user_name.upper())
print("Lowercase = ",user_name.lower())
print("Reversed =", user_name[::-1])
parts = user_name.split()
initials = "".join([p[0].upper() for p in parts])
print("Initials = ",initials)

#-------------------------------------------------------------------------------------------

#Exercise 4 — Simple Calculator
# Add, subtract, multiply, divide using functions.

def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    if y == 0:
        return("Error: Value can not be divided by 0.")
    return(x/y)

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter the number of operation to perform:")

num1 = float(input("Enter the 1st Value: "))
num2 = float(input("Enter the 2nd value: "))

if choice == "1":
    print("Result = ",add(num1, num2))
elif choice == "2":
    print("Result = ",subtract(num1, num2))
elif choice == "3":
    print("Rsult = ",multiply(num1, num2))
elif choice == "4":
    print("Result = ",divide(num1, num2))
else:
    print("Invalid Selection!")

#-----------------------------------------------------------------------------------------------------------------------

#Example: Calculator for Multiple Numbers

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            return ("Error: Value can not be divided by 0.")
        result /= n
    return result

print("List Calculator")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

nums = input("Enter the numbers:\n")
numbers = [float(x) for x in nums.replace(",","").split()]

print("Numbers:", numbers)
print("Sum:", add(numbers))
print("Subtraction:", subtract(numbers))
print("Multiplication:", multiply(numbers))
print("Division:", divide(numbers))


#------------------------------------------------------------Re-Practice---------------------------------------------------------------------------

# Exercise 1 — Temperature Converter
# Write two functions:
# c_to_f(celsius)
# f_to_c(fahrenheit)

def c_to_f(celcius):
    return (celcius * 9/5) +32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) *5/9

def main():
    print("===Temperature Converter===")

    while True:
        print("\nSelect an option to perform:")
        print("1. Celcius to Fahrenheit")
        print("2. Fahrenheit to Celcius")
        print("3. Exit")

        choice = int(input("Enetr the selecetion: "))

        if choice == 1:
            try:
                c = float(input("Enter the temperature: "))
                f = c_to_f(c)
                print(f"{c:.2f}°C is equal to {f:.2f}°F")
            except ValueError:
                print("Invalid Input! Please enter a correct number.")

        elif choice == 2:
            try:
                f = float(input("Enter the temperature: "))
                c = f_to_c(f)
                print(f"{f:.2f}°F is equal to {c:.2f}°C")
            except ValueError:
                print("Invalid Input! Please enter a correct number.")
            
        elif choice == 3:
            print("Thanks for using our service.")
            break

        else:
            print("Invalid Input! Please enter a correct number.")

main()


#-------------------------------------------------------------------------------------------------------------------

# Exercise 2 — List Processor
# Your Task
# Write four functions that take a list of numbers and return:
# Maximum value
# Minimum value
# Sum of all values
# Average of values

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_sum(numbers):
    return sum(numbers)

def find_avg(numbers):
    return sum(numbers)/len(numbers)

def main():
    numbers = [73, 12, 58, 91, 4, 39, 67, 25, 84, 10]

    print(f"Maximum Valur = {find_max(numbers)}")
    print(f"Minimum Valur = {find_min(numbers)}")
    print(f"Sum = {find_sum(numbers)}")
    print(f"Average Number = {find_avg(numbers)}")

main()

#------------------------------------------------------------------------------------------------------------------------

# Exercise 3 — String Formatter
# Your Task
# Write a program that takes a user’s full name and outputs:
# Uppercase version
# Lowercase version
# Reversed string
# Initials (e.g., “Saif ur Rehman” → “S.R.”)

def upper_case(name):
    return name.upper()

def lower_case(name):
    return name.lower()

def reversed_case(name):
    return name[::-1]

def initials_case(name):
    parts = name.split()
    initials = ".".join([p[0].upper() for p in parts]) + "."
    return initials

def main():
    name = input("Enter your Name: ").strip()

    print(f"Uppercase Version = {upper_case(name)}")
    print(f"Lowercase Version = {lower_case(name)}")
    print(f"Reversed Name = {reversed_case(name)}")
    print(f"Initials of your name = {initials_case(name)}")

main()

#------------------------------------------------------------------------------------------------------------------------------

# Exercise 4 — Simple Calculator
# Your Task
# Write four functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b) → handle division by zero

def add(x,y):
    return (x + y)

def sub(x,y):
    return (x - y)

def multi(x,y):
    return (x * y)

def divide(x,y):
    if y == 0:
        return("Error! Cannot divided by 0. Try again")
    return (x / y)

def main():

    while True:

        print("\n===Simple Calculator===")
        print("\nSelect the number of operation to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter the selection:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 5:
            print("Thanks for using our service!")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid selection. Try again.")
            continue

        try:
            x  = float(input("Enter the 1st number: "))
            y = float(input("Enter the 2nd number: "))
        except ValueError:
            print("Invalid Number: Try againg!")
            continue


        if choice == 1:
            print(f"Sum = {add(x,y)}")
        
        elif choice == 2:
            print(f"Subtract = {sub(x,y)}")
        
        elif choice == 3:
            print(f"Multiple = {multi(x,y)}")

        elif choice == 4:
            print(f"Division = {divide(x,y)}")
        
if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------------------------------------------------

# Example: Calculator for Multiple Numbers

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result

def multiplication(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def division(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result /= n
    return result

def get_numbers(choice):
    numbers = []
    print("Enter the numbers one by one. Press ENTER to stop.")
    print("You can add ',' and/or SPACE to seperate the numbers.")

    while True:
        raw =  input("> ").strip()
        if raw == "":
            break

        raw = raw.replace(",", " ")

        parts = raw.split()

        for p in parts:
            try:
                n = float(p)
            except ValueError:
                print(f"Invalid number '{p}'. Try again")
                continue
        
            if choice == 4 and n == 0:
                print("Error! Cannot divided by 0. Enter another number.")
                continue

            numbers.append(n)

    return numbers

def main():

    while True:
        print("\n===Multi Number Calculator===")
        print("Select the number of operation to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter the number of operation: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 5:
            print("Thanks for using our service. Goodbye!")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid Selection. Enter correct selection.")
            continue

        numbers = get_numbers(choice)

        if len(numbers) < 2:
            print("Please enter at least 2 numbers.")
            continue

        if choice == 1:
            print(f"Total = {add(numbers)}")

        elif choice == 2:
            print(f"Total = {subtract(numbers)}")

        elif choice == 3:
            print(f"Total = {multiplication(numbers)}")

        elif choice == 4:
            print(f"Total = {division(numbers)}")

main()

#------------------------------------------------------------------------------------------------------------------------

# Start the mini‑project
# Personal Expense Logger step by step

# expense_logger/
#     main.py
#     expenses.txt   (this will be created automatically)

expenses = []

def add_expense():
    pass

def view_expenses():
    pass

def total_expenses():
    pass

def save_to_file():
    pass

def load_from_file():
    pass

def main():
    while True:
        print("\n=== Expense Logger ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")

        choice = input("Choose an option: ")

        # We will fill this later

if __name__ == "__main__":
    main()

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        expenses.append({"amount": amount, "category": category})
        print("Expense added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Your Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - {exp['amount']} PKR")

def total_expenses():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spent: {total} PKR")

def save_to_file():
    with open("expenses.txt", "w") as file:
        for exp in expenses:
            file.write(f"{exp['amount']},{exp['category']}\n")
    print("Expenses saved to file.")

def load_from_file():
    try:
        with open("expenses.txt", "r") as file:
            expenses.clear()
            for line in file:
                amount, category = line.strip().split(",")
                expenses.append({"amount": float(amount), "category": category})
        print("Expenses loaded from file.")
    except FileNotFoundError:
        print("No saved file found.")

def main():
    while True:
        print("\n=== Expense Logger ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            load_from_file()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
