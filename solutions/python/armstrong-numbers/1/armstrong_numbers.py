def is_armstrong_number(number):
    digits = []
    temp = number
    while temp > 0:
        digit = temp % 10
        digits.append(digit)
        temp = temp // 10  
    power = len(digits)
    total_sum = 0
    for digit in digits:
        total_sum += digit ** power
    return number == total_sum