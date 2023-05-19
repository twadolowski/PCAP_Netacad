def is_prime(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
