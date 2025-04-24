print("hello")
print("your name")
a = 195
b = 5
c = a**b
print(c)
x = int(input("Enter your first number"))
y = int(input("Enter your second number"))
c = x - y
print(c)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

if __name__ == "__main__": 
    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        sum_result = add(x, y)
        print(f"Sum: {sum_result}")

        difference_result = subtract(x, y)
        print(f"Difference: {difference_result}")

        product_result = multiply(x, y)
        print(f"Product: {product_result}")

        try:
            quotient_result = divide(x, y)
            print(f"Quotient: {quotient_result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

    except ValueError:
        print("Invalid input. Please enter integers only.")