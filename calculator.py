# This function adds two numbers
def add(x, y):
    return x + y

# This function subtract two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function devides two numbers
def divide(x, y):
    return x / y

# This function calculate exponents
def power(x, y):
    return x ** y


print("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")

while True:
    # take input from the user
    choice = input("Enter Choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid Input. Please Enter a Number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**", num2, "=", power(num1, num2))

        # check if user wants another calculation
        # break the while loop if the answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")