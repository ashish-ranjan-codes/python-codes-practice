# divisibility test functions

# Divisibility of 2
def divisible_by_2(n):
    last_digit = n%10
    return last_digit % 2 == 0

# Divisibility of 3
def divisible_by_3(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum % 3 == 0

# Divisibility of 4
def divisible_by_4(n):
    i = 2
    num = 0
    while i > 0 and n > 0:
        num = (n*10) + n % 10
        n = n // 2
        i = i - 1
    return num == 00 or num % 4 == 0 or n % 4 == 0

# Divisibility of 5
def divisible_by_5(n):
    last_digit = n%10
    return last_digit == 0 or last_digit == 5

# Divisibilty of 6
def divisible_by_6(n):
    return divisible_by_2(n) and divisible_by_3(n)

# Divisibility of 7
def divisible_by_7(n):
    last_digit = n%10
    if last_digit % 2 == 0:
        return True
    return False

# Divisibility of 8
def divisible_by_8(n):
    i = 3
    num = 0
    while i > 0 and n > 0:
        num = (n*10) + n % 10
        n = n // 2
        i = i - 1
    return num % 8 == 0

# Divisibility of 9
def divisible_by_9(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum % 9 == 0

# Divisibility of 10
def divisible_by_10(n):
    return n % 10 == 0

# Divisibility of 11
def divisible_by_11(n):
    num = str(n)
    even_sum = 0
    odd_sum = 0
    for i in range(len(num)):
        if i%2==0:
            even_sum += int(num[i])
        else:
            odd_sum += int(num[i])
    diff = odd_sum - even_sum
    return diff % 11 == 0

