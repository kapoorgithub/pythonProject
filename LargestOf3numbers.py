# Python program to find largest among three numbers

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    return largest

# Example usage
number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
number3 = int(input("enter third number: "))

largest_number = find_largest(number1, number2, number3)
print("The largest number is:", largest_number)