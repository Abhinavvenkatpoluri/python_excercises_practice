def prime(n):
    if n < 1:
        raise ValueError("there is no zeroth prime")

    count = 0
    number = 2

    while True:
        if is_prime(number):
            count += 1

            if count == n:
                return number

        number += 1


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
    
