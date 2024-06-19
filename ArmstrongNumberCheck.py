def is_armstrong_number(n):
    temp = n
    num_digits = len(str(n))
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
    return sum == n

number = 15
if is_armstrong_number(number):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")