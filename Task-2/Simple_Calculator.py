def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number (or type 'exit' to quit): "))
        except ValueError:
            print("Exiting the calculator.")
            break

        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        operation = input("Enter the operation (1/2/3/4): ")

        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        else:
            print("Invalid operation choice. Please enter 1, 2, 3, or 4.")
            continue

        print(f"The result is: {result}")

if __name__ == "__main__":
    main()
